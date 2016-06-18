import requests   # We use Python "requests" module to do HTTP GET query
import json       # Import JSON encoder and decode module
#from apicem_config import * # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

url = "https://sandboxapic.cisco.com" + "/api/v0/network-device/count"   # API base url
resp= requests.get(url,verify=False)     # The response (result) from "GET /network-device/count" query
response_json = resp.json() # Get the json-encoded content from response with "response_json = resp.json()
count = response_json["response"]    # Total count of network-device and convert it to string

print ("\nTotal Device Number", count)

print ("Devices = ")

url = "https://sandboxapic.cisco.com" + "/api/v0/network-device/1/" + str(count)   # API base url
resp= requests.get(url,verify=False)     # The response (result) from "GET /network-device/count" query
response_json = resp.json() # Get the json-encoded content from response with "response_json = resp.json()
parent = response_json["response"]    # Total count of network-device and convert it to string

for item in parent:
    print ("id = " + item["id"] + " macAddress: = " + item["macAddress"] + " type = " + item["type"])
  
