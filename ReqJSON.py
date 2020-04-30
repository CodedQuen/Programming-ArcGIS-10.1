import requests
import json

agisurl = "http://server.arcgisonline.com/arcgis/rest/services?f=pjson"
r = requests.get(agisurl)
decoded = json.loads(r.text)
print(decoded)
#print(r.text)
