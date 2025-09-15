import numpy as np
try:
 import simpleaudio as sa
except Exception:
 print('Instale simpleaudio para tocar no PC');raise SystemExit(0)
fs=44100;t=np.linspace(0,0.5,int(fs*0.5),False)
note=(np.sin(2*np.pi*440*t)*0.2).astype(np.float32)
audio=(note*32767).astype(np.int16).tobytes()
sa.play_buffer(audio,1,2,fs).wait_done();print('Reprodução OK')
