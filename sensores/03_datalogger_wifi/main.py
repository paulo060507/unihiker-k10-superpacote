import os,time,random
try:
 import urequests as requests
except Exception:
 import requests
URL=os.environ.get('POST_URL','https://httpbin.org/post')
while True:
 p={'temp':round(24.5+random.random()*3,2),'hum':round(50+random.random()*10,1),'lux':int(200+random.random()*150)}
 try:
  r=requests.post(URL,json=p,timeout=10);print('POST',r.status_code,p)
 except Exception as e:
  print('Falha',e)
 time.sleep(5)
