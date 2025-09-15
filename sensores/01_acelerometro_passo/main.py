import os, time, math
THRESH=float(os.environ.get('THRESH','1.2'));DELAY=float(os.environ.get('DELAY','0.05'))
steps=0;prev=1.0
for i in range(120):
 m=1.0+0.5*math.sin(i/2)
 if prev<THRESH and m>=THRESH:
  steps+=1;print('Passos:',steps)
 prev=m;time.sleep(DELAY)
print('Total:',steps)
