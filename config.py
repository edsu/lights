import sys

HUE_BRIDGE_IP = "192.168.1.155"
HUE_API_KEY = sys.environ.get('HUE_API_KEY')

if not HUE_API_KEY:
    sys.exit('Please set HUE_API_KEY in your environment')

HUE_API_URL = "https://{}/api/{}/lights/2/state".format(HUE_BRIDGE_IP, HUE_API_KEY)
