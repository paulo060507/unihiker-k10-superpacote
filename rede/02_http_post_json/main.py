import os
try:
 import urequests as requests
except Exception:
 import requests
url=os.environ.get('POST_URL','https://httpbin.org/post')
r=requests.post(url,json={'msg':'hello K10'},timeout=10)
print('POST',r.status_code);print(r.text[:300])
