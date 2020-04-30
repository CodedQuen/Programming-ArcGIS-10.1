import requests
import json

agisurl = "http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/Specialty/ESRI_StateCityHighway_USA/MapServer/export"


payload = { 'bbox': '-115.8,30.4,-85.5,50.5','size': '800,600', \
            'imageSR': '102004', 'format': 'gif', 'transparent':'false', \
            'f': 'pjson'}

r = requests.get(agisurl, params=payload)
print(r.text)



