import time,random,os
DELAY=float(os.environ.get('DELAY','1'))
while True:
 t=24+random.random()*3;h=50+random.random()*10;lux=200+random.random()*120
 print(f'T={t:.1f}C H={h:.0f}% Lux={lux:.0f}')
 time.sleep(DELAY)
