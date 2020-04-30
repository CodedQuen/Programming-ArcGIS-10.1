import requests
import json

agisurl = "http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/Demographics/ESRI_Census_USA/MapServer/1"
payload = { 'where': 'STATE_FIPS = \'48\' and CNTY_FIPS = \'021\'','returnCountyOnly': 'false', 
            'returnIdsOnly': 'false', 'returnGeometry': 'false',  
            'f': 'pjson'}

r = requests.get(agisurl, params=payload)
#r = requests.get(agisurl)
#print(r.text)

decoded = json.loads(r.text)
print("The layer name is: " + decoded['name'])
print("The xmin: " + str(decoded['extent']['xmin']))
print("The xmax: " + str(decoded['extent']['xmax']))
print("The ymin: " + str(decoded['extent']['ymin']))
print("The ymax: " + str(decoded['extent']['xmax']))
print("The fields in this layer: ")
for rslt in decoded['fields']:
    print(rslt['name'])
