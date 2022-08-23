import requests

def add_flow(url, flow):

  url = url

  payload = flow

  headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Cookie': 'JSESSIONID=17tdq3dvhgohw137fr1fvblck'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  return response
