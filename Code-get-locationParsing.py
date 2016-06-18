import requests   # We use Python "requests" module to do HTTP GET query
import json       # Import JSON encoder and decode module
import sys
#from apicem_config import * # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

location_list = []

url = "https://sandboxapic.cisco.com"+"/api/v0/location"
resp = requests.get(url,verify=False)
response_json = resp.json()

for item in response_json["response"]:
    location_list.append({"location_id":item["id"],"location_name":item["locationName"]})
   
for item in location_list:
    print ("id: %s, location name: %s" % (item["location_id"],item["location_name"]))
