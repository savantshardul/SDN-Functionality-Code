import requests   # We use Python "requests" module to do HTTP GET query
import json       # Import JSON encoder and decode module
#from apicem_config import * # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

url = "https://sandboxapic.cisco.com" + "/api/v0/host"   # API base url
ip_list = []

resp= requests.get(url,verify=False)     # The response (result) from "GET /network-device/count" query
response_json = resp.json() # Get the json-encoded content from response with "response_json = resp.json()

for item in response_json["response"]:
    ip_list.append(item["hostIp"])
ip_list.sort()
print (ip_list)

    

    


