import re
import json
import time
from copy import copy,deepcopy
import logging
import requests
from spf import find_shortest_path
from create_flow import create_flows

logging.basicConfig(filename='./link.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

def get_topo():
    url = "http://localhost:8181/restconf/operational/network-topology:network-topology"

    payload={}
    headers = {
    'Authorization': 'Basic YWRtaW46YWRtaW4=',
    'Cookie': 'JSESSIONID=6fv6mu0zvlmw1es8kbx5piu6z',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)

def find_links_from_topo(topology, network_size):
    nodes = topology["network-topology"]["topology"][0]["node"]    

    links = []

    host_switch_links = ["openflow:1:1", "openflow:"+str(network_size)+":1"]

    for node in nodes:
        for link in node["termination-point"]:
            if re.search("openflow:.*:LOCAL", link["tp-id"]) or link["tp-id"] in host_switch_links:
                continue
            else:
                name = int(link["tp-id"].split(":")[-1])
                if int(name%network_size) == 0:
                    extract_endpoints = (int(name/network_size)-1, network_size, node["node-id"], link["tp-id"], 'active')
                    links.append(extract_endpoints)
                else:
                    extract_endpoints = (int(name/network_size), int(name%network_size), node["node-id"], link["tp-id"], 'active')
                    links.append(extract_endpoints)

    return links


def get_link_status(link):
    node_name = link[2]
    link_name = link[3]
    url = f"http://localhost:8181/restconf/operational/opendaylight-inventory:nodes/node/{node_name}/node-connector/{link_name}"

    payload={}
    headers = {
    'Authorization': 'Basic YWRtaW46YWRtaW4=',
    'Cookie': 'JSESSIONID=6fv6mu0zvlmw1es8kbx5piu6z',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)

    new_link = copy(link)

    state = response["node-connector"][0]["flow-node-inventory:state"]
    if state["link-down"] == True:
        new_link = (link[0], link[1], link[2], link[3], 'inactive')

    if state["live"] == True:
        new_link = (link[0], link[1], link[2], link[3],  'active')

    return new_link

def change_flows(matrix, changed_matrix, changed_links):
    links = set()
    for link in changed_links:
        logging.warning('change in link'+str(link[0]) +" to "+ str(link[1]) +" changed to " + str(link[4])+' occurs!')
        links.add((link[0], link[1], link[4]))

    for link in links:
        ## link is back online again
        if link[2] == 'active':
            changed_matrix[link[0]-1][link[1]-1] = matrix[link[0]-1][link[1]-1] 
        
        ## link is ofline now
        else:
            changed_matrix[link[0]-1][link[1]-1] = 0
    try:
        path_1_n, path_n_1= find_shortest_path(matrix_size, changed_matrix)
        print("shortest path form 1 n is: ", path_1_n)
        logging.warning("shortest path form 1 n is: " + str(path_1_n))

        print("shortest path form n 1 is: ", path_n_1)
        logging.warning("shortest path form 1 n is: " + str(path_1_n))
        create_flows(matrix_size, path_1_n, path_n_1)
    except:
        logging.warning('no path found!')

    return changed_matrix


def watcher(links_last_queried):
    links_changed = set()

    for link in links_last_queried:
        new_link_stat = get_link_status(link)
        if new_link_stat == link:
            continue

        links_changed.add(new_link_stat)

    return links_changed

if __name__ == '__main__':

    ## initialize 
    matrix_size = int(input("Enter matrix size: "))
    print("Enter matrix element followed by enter: ")

    initial_matrix = [[] for i in range(0,matrix_size)]
    try:
        for i in range(0, matrix_size):
            for j in range(0, matrix_size):
                initial_matrix[i].append(int(input()))

    except Exception as e:
        print ("Exception:",e)
        print ("Error: please enter an integer")
        exit()

    path_1_n, path_n_1= find_shortest_path(matrix_size, initial_matrix)

    create_flows(matrix_size, path_1_n, path_n_1)
    topology = get_topo()
    links = find_links_from_topo(topology,matrix_size) 

    changed_matrix = deepcopy(initial_matrix)

    while True:
        time.sleep(10)  
        changes = watcher(links)

        if changes:
            changed_matrix = change_flows(initial_matrix, changed_matrix, changes)
            
            for index,link in enumerate(links):
                for change in changes:
                    if change[0] == link[0] and change[1] == link[1] and change[2] == link[2] and change[3] == link[3]:
                        links[index] = change