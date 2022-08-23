import os 
import json
import shutil
import requests

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

  if "tun_id" in config.keys():
    if "ipv4-destination" in config.keys():
      payload["match"] = {"tunnel": {"tunnel-id": config["tun_id"]}, "ipv4-destination": config["ipv4-destination"]}

    if "ethernet-dst" in config.keys():
      payload["match"] = {"tunnel": {"tunnel-id": config["tun_id"]}, "ethernet-match":{"ethernet-destination":{"address": config["ethernet-dst"]}}}

  if "ipv4-destination" in config.keys():
    payload["match"] = {"ipv4-destination": config["ipv4-destination"]}

  if "ethernet-source" in config.keys():
    payload["match"] = {"ethernet-match":{"ethernet-source":{"address": config["ethernet-source"]}}}

  action = []
  order = 0
  if "dec-nw-ttl"in config.keys():
    action.append({"order": order,  "dec-nw-ttl": {}})
    order += 1

  if "vlan" in config.keys():
    action.append({"order": order,  "push-vlan-action": {"ethernet-type": 33024}})
    order += 1
    action.append({"order": order,  "set-field": {"vlan-match": {"vlan-id":{"vlan-id-present": True, "vlan-id": config["vlan"]}}}})
    order += 1
    action.append({"order": order,  "output-action": {"output-node-connector": "table:1", "max-length": 65535}})
    order += 1

  if "out-port" in config.keys():
    action.append({"order": order, "output-action":{"output-node-connector": config["out-port"], "max-length": 65535}})
    order += 1

  if "go-table" in config.keys():
    payload["match"] = {}
    action.append({"order": order,  "output-action": {"output-node-connector": "table:1", "max-length": 65535}})

  if "FLOOD" in config.keys():
    payload["match"] = {}
    action.append({"order": 0, "output-action":{"output-node-connector": "FLOOD", "max-length": 65535}})

  if "drop" in config.keys():
    action.append({"order": order, "drop-action": {}})
  
  instruction = []
  instruction.append({"order": 0, "apply-actions":{"action": action}})

  payload["instructions"] = {"instruction": instruction}
  payload ={"flow-node-inventory:flow":[payload]} 

  return json.dumps(payload)


def add_flow(config):

  url = create_url(config=config)

  payload = create_payload(config=config)

  headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Cookie': 'JSESSIONID=17tdq3dvhgohw137fr1fvblck'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  return response

# s1
configs = []
configs.append({"node_id": 1, "table_id": 0, "flow_id": 1, "in-port": 1, "vlan":100})
configs.append({"node_id": 1, "table_id": 0, "flow_id": 2, "in-port": 2, "vlan":200})
configs.append({"node_id": 1, "table_id": 0, "flow_id": 3, "go-table": True})

configs.append({"node_id": 1, "table_id": 1, "flow_id": 4, "tun_id": 100, "ethernet-dst": "00:00:00:00:00:01","out-port": 1})
configs.append({"node_id": 1, "table_id": 1, "flow_id": 5, "tun_id": 200, "ethernet-dst": "00:00:00:00:00:01","out-port": 2})

configs.append({"node_id": 1, "table_id": 1, "flow_id": 6, "tun_id": 100, "ipv4-destination": "10.0.0.1/32","out-port": 1})
configs.append({"node_id": 1, "table_id": 1, "flow_id": 7, "tun_id": 200, "ipv4-destination": "10.0.0.1/32","out-port": 2})

configs.append({"node_id": 1, "table_id": 1, "flow_id": 8, "tun_id": 100, "ethernet-dst": "00:00:00:00:00:02","out-port": 3})
configs.append({"node_id": 1, "table_id": 1, "flow_id": 9, "tun_id": 200, "ethernet-dst": "00:00:00:00:00:02","out-port": 3})

configs.append({"node_id": 1, "table_id": 1, "flow_id": 10, "tun_id": 100, "ipv4-destination": "10.0.0.2/32","out-port": 1})
configs.append({"node_id": 1, "table_id": 1, "flow_id": 11, "tun_id": 200, "ipv4-destination": "10.0.0.2/32","out-port": 2})

configs.append({"node_id": 1, "table_id": 1, "flow_id": 12, "drop": True})


# s2
configs.append({"node_id": 2, "table_id": 0, "flow_id": 1, "in-port": 1, "vlan":100})
configs.append({"node_id": 2, "table_id": 0, "flow_id": 2, "in-port": 2, "vlan":200})
configs.append({"node_id": 2, "table_id": 0, "flow_id": 3, "go-table": True})

configs.append({"node_id": 2, "table_id": 1, "flow_id": 4, "tun_id": 100, "ethernet-dst": "00:00:00:00:00:02","out-port": 1})
configs.append({"node_id": 2, "table_id": 1, "flow_id": 5, "tun_id": 200, "ethernet-dst": "00:00:00:00:00:02","out-port": 2})

configs.append({"node_id": 2, "table_id": 1, "flow_id": 6, "tun_id": 100, "ipv4-destination": "10.0.0.2/32","out-port": 1})
configs.append({"node_id": 2, "table_id": 1, "flow_id": 7, "tun_id": 200, "ipv4-destination": "10.0.0.2/32","out-port": 2})

configs.append({"node_id": 2, "table_id": 1, "flow_id": 8, "tun_id": 100, "ethernet-dst": "00:00:00:00:00:01","out-port": 3})
configs.append({"node_id": 2, "table_id": 1, "flow_id": 9, "tun_id": 200, "ethernet-dst": "00:00:00:00:00:01","out-port": 3})

configs.append({"node_id": 2, "table_id": 1, "flow_id": 10, "tun_id": 100, "ipv4-destination": "10.0.0.1/32","out-port": 1})
configs.append({"node_id": 2, "table_id": 1, "flow_id": 11, "tun_id": 200, "ipv4-destination": "10.0.0.1/32","out-port": 2})

configs.append({"node_id": 2, "table_id": 1, "flow_id": 12, "drop": True})



for config in configs:
  log_flows(create_payload(config), config["node_id"])
  a= add_flow(config)
  print(a.text)