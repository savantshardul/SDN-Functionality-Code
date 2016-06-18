import requests   # We use Python "requests" module to do HTTP GET query
import json       # Import JSON encoder and decode module
import sys
requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3
device_ip = "40.0.1.6"

#Policy list preparation  
url = "https://sandboxapic.cisco.com" + "/api/v0/network-device/count"
resp= requests.get(url,verify=False)     # The response (result) from "GET /network-device/count" query
response_json = resp.json() # Get the json-encoded content from response with "response_json = resp.json()
count = response_json["response"]


if count>0 :
    device_list = []
    url = "https://sandboxapic.cisco.com" + "/api/v0/network-device/1/"+str(count)   # API base url, convert count to string
    resp= requests.get(url, verify=False)
    response_json = resp.json()

    for item in response_json["response"]:
        device_list.append([item["hostname"],item["type"],item["managementIpAddress"],item["id"]])
    device_list.sort()
else:
    print ("No network device found!")
    sys.exit(1)
# Find network device id for network device with ip


id = ""
for item in device_list:
    if item[2] == device_ip:
        id = item[3]
    # index 2 is ip, 3 is item id

    #get ios configuration for network device with ip 40.0.1.6
if id != "":
    url = "https://sandboxapic.cisco.com" + "/api/v0/interface/network-device/"+id   # API base url, convert count to string
    resp= requests.get(url, verify=False)
    response_json = resp.json()
    print ("Status:", resp.status_code)
    print (json.dumps(response_json["response"],indent = 4))
else:
    print ("No decvice was found for ip" + device_ip)
    

