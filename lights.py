import os
import sys
import requests

hue_api_key = os.environ.get('HUE_API_KEY')
if not hue_api_key:
    sys.exit('Please set HUE_API_KEY in your environment')

hue_bridge_ip = os.environ.get('HUE_BRIDGE_IP')
if not hue_bridge_ip:
    sys.exit('Please set HUE_BRIDGE_IP in your environment')
    
hue_api_url = "http://{}/api/{}".format(hue_bridge_ip, hue_api_key)

outside = 1
kitchen = 2

red = {"xy": [.6, .3]}
green = {"xy": [.4, .5]}
blue = {"xy": [.22, .15]}

def set_color(light, color):
    url = "{}/lights/{}/state".format(hue_api_url, light)
    return requests.put(url, json=color)

def outside_color(color):
    return set_color(1, color)

def kitchen_color(color):
    return set_color(2, color)
