import time
import random
import requests

from config import HUE_API_URL

url = HUE_API_URL + "/lights/2/state"

red = {"xy": [.6, .3]}
green = {"xy": [.4, .5]}
blue = {"xy": [.22, .15]}

color = green
while True:
    requests.put(url, json=color)
    if color == green:
        color = red
    elif color == red:
        color = blue
    else:
        color = green
    time.sleep(random.randint(1, 60))
