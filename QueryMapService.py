import requests
import json

agisurl = "http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/Demographics/ESRI_Census_USA/MapServer/1/query"
payload = { 'where': 'STATE_FIPS = \'48\' and CNTY_FIPS = \'021\'','returnCountyOnly': 'false',
            'returnIdsOnly': 'false', 'returnGeometry': 'false', 'outFields':'POP2000,POP2007,BLKGRP',
            'f': 'pjson'}


r = requests.get(agisurl, params=payload)
#print(r.text)

decoded = json.loads(r.text)
#print(decoded)


for rslt in decoded['features']:
    print("Block Group: " + str(rslt['attributes']['BLKGRP']))
    print("Population 2000: " + str(rslt['attributes']['POP2000']))
    print("Population 2007: " + str(rslt['attributes']['POP2007']))

