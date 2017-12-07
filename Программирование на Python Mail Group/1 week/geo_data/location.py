import requests
import pprint

def get_location_info():
  r = requests.get('https://freegeoip.net/json/')
  return r.json()

if __name__=="__main__":
  pprint.pprint(get_location_info())