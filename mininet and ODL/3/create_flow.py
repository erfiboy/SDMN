import os 
import json
import shutil
from send_flows import add_flow


def clean_directory():

  base = os.path.dirname(os.path.abspath(__file__))
  directory= "switches_flows"
  path = os.path.join(base, directory) 
  if os.path.isdir(path):
    shutil.rmtree(path)

def log_flows(flow, switch_id):

  base = os.path.dirname(os.path.abspath(__file__))
  directory= "switches_flows"
  path = os.path.join(base, directory) 

  if not os.path.isdir(path):
    os.mkdir(path) 

  flow = json.loads(flow)

  f = open(path+"/switch_"+str(switch_id)+"_flow.json", "a")
  json.dump(flow, f, indent=4)
  f.write("\n")
  f.close()

def create_url(config):
  base_url = "http://localhost:8181/restconf/config/opendaylight-inventory:nodes/node/"
  node_id = "openflow:"+str(config['node_id'])+"/"
  flow_table = "flow-node-inventory:table/"+str(config['table_id'])+"/"
  flow_id = "flow/"+str(config['flow_id'])
  request_url = base_url + node_id + flow_table + flow_id

  return request_url

def create_payload(config):
  payload = {}
  payload["id"] = config["flow_id"]
  payload["table_id"] = config["table_id"]
  payload["idle-timeout"] = 30
  payload["priority"] = 500

  if "in-port" in config.keys():
    payload["match"] = {"in-port": config["in-port"]}

  if "in-port" in config.keys() and "ipv4-destination" in config.keys():
    payload["match"] = {"in-port": config["in-port"], "ipv4-destination": config["ipv4-destination"], "ethernet-match": {"ethernet-type": {"type": 0x800}}}

  if "in-port" in config.keys() and "arp-dst" in config.keys():
    payload["match"] = {"in-port": config["in-port"], "arp-target-transport-address": config["arp-dst"], "ethernet-match": {"ethernet-type": {"type": 0x806}}}

  if "ethernet-source" in config.keys():
    payload["match"] = {"ethernet-match":{"ethernet-source":{"address": config["ethernet-source"]}}}

  action = []
  order = 0
  if "dec-nw-ttl"in config.keys():
    action.append({"order": order,  "dec-nw-ttl": {}})
    order += 1

  if "out-port" in config.keys():
    action.append({"order": order, "output-action":{"output-node-connector": config["out-port"], "max-length": 65535}})
    order += 1

  if "FLOOD" in config.keys():
    payload["match"] = {}
    action.append({"order": 0, "output-action":{"output-node-connector": "FLOOD", "max-length": 65535}})
  
  instruction = []
  instruction.append({"order": 0, "apply-actions":{"action": action}})

  payload["instructions"] = {"instruction": instruction}
  payload ={"flow-node-inventory:flow":[payload]} 

  return json.dumps(payload)

matrix_size = int(input("Enter the matrix size: "))
shortest_path = input("Enter a list contains switches from host 1 to n: ").split()
clean_directory()
shortest_path = [int(i) for i in shortest_path]

for index, switches in enumerate(shortest_path):
    if index == 0:
        ## ip flow
        config = {"node_id": switches, "table_id": 0, "flow_id": 0, "ipv4-destination":"10.0.2.1/32", "in-port": 1, "out-port": matrix_size*shortest_path[index]+shortest_path[index+1]}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        
        ## arp flow
        
        config = {"node_id": switches, "table_id": 0, "flow_id": 1, "arp-dst":"10.0.2.1/32", "in-port": 1, "out-port": matrix_size*shortest_path[index]+shortest_path[index+1]}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        continue
        
    if index == len(shortest_path)-1:
        ## ip flow

        config = {"node_id": switches, "table_id": 0, "flow_id": 0, "ipv4-destination":"10.0.2.1/32", "in-port": matrix_size*shortest_path[index-1]+shortest_path[index], "out-port": 1}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        
        ## arp flow
        
        config = {"node_id": switches, "table_id": 0, "flow_id": 1, "arp-dst":"10.0.2.1/32", "in-port": matrix_size*shortest_path[index-1]+shortest_path[index], "out-port": 1}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        continue
    
    else:
        ## ip flow

        config = {"node_id": switches, "table_id": 0, "flow_id": 0, "ipv4-destination":"10.0.2.1/32", "in-port": matrix_size*shortest_path[index-1]+shortest_path[index], "out-port": matrix_size*shortest_path[index]+shortest_path[index+1]}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        
        ## arp flow
        
        config = {"node_id": switches, "table_id": 0, "flow_id": 1, "arp-dst":"10.0.2.1/32", "in-port": matrix_size*shortest_path[index-1]+shortest_path[index], "out-port": matrix_size*shortest_path[index]+shortest_path[index+1]}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)


### back route to 1 from n

shortest_path = input("Enter a list contains switches from host n to 1: ").split()
shortest_path = [int(i) for i in shortest_path]

for index, switches in enumerate(shortest_path):
    if index == 0:
        ## ip flow

        config = {"node_id": switches, "table_id": 0, "flow_id": 2,"ipv4-destination":"10.0.1.1/32", "in-port": 1, "out-port": matrix_size*shortest_path[index]+shortest_path[index+1]}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        
        ## arp flow

        config = {"node_id": switches, "table_id": 0, "flow_id": 3,"arp-dst":"10.0.1.1/32", "in-port": 1, "out-port": matrix_size*shortest_path[index]+shortest_path[index+1]}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        continue
        
    if index == len(shortest_path)-1:
        ## ip flow
        config = {"node_id": switches, "table_id": 0, "flow_id": 2,"ipv4-destination":"10.0.1.1/32", "in-port": matrix_size*shortest_path[index-1]+shortest_path[index], "out-port": 1}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        
        ## arp flow
        
        config = {"node_id": switches, "table_id": 0, "flow_id": 3,"arp-dst":"10.0.1.1/32", "in-port": matrix_size*shortest_path[index-1]+shortest_path[index], "out-port": 1}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        continue
    
    else:
        ## ip flow

        config = {"node_id": switches, "table_id": 0, "flow_id": 2,"ipv4-destination":"10.0.1.1/22", "in-port": matrix_size*shortest_path[index-1]+shortest_path[index], "out-port": matrix_size*shortest_path[index]+shortest_path[index+1]}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
        
        ## arp flow
        
        config = {"node_id": switches, "table_id": 0, "flow_id": 3,"arp-dst":"10.0.1.1/22", "in-port": matrix_size*shortest_path[index-1]+shortest_path[index], "out-port": matrix_size*shortest_path[index]+shortest_path[index+1]}
        add_flow(create_url(config), create_payload(config))
        log_flows(create_payload(config), switches)
