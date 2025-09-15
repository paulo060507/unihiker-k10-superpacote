import time
colors=[(255,0,0),(0,255,0),(0,0,255),(255,255,0)];idx=0;on=False
for _ in range(10):
 idx=(idx+1)%len(colors);on=not on
 print('LED',('ON' if on else 'OFF'),'cor:',colors[idx]);time.sleep(0.5)
