import asyncio,os,websockets
URI=os.environ.get('WS_URI','wss://echo.websocket.events')
async def main():
 try:
  async with websockets.connect(URI) as ws:
   await ws.send('hello from K10');print('echo:',await ws.recv())
 except Exception as e:
  print('WS erro:',e)
asyncio.run(main())
