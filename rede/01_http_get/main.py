import os
try:
 import urequests as requests
except Exception:
 import requests
url=os.environ.get('URL','https://api.github.com/zen')
r=requests.get(url,timeout=10)
print('GET',r.status_code);print(r.text[:300])
