import requests
import json

agisurl = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find"

payload = { 'text': '1202 Sand Wedge, San Antonio, TX, 78258', 'f': 'pjson'}

r = requests.get(agisurl, params=payload)

decoded = json.loads(r.text)
print("The geocoded address: " + decoded['locations'][0]['name'])
print("The longitude: " + str(decoded['locations'][0]['feature']['geometry']['x']))
print("The latitude: " + str(decoded['locations'][0]['feature']['geometry']['y']))
print("The geocode score: " + str(decoded['locations'][0]['feature']['attributes']['Score']))
print("The address type: " + decoded['locations'][0]['feature']['attributes']['Addr_Type'])


