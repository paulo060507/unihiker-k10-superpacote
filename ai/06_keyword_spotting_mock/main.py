import os, time, numpy as np

def pc_loop():
    try:
        import sounddevice as sd
        def callback(indata, frames, time_, status):
            vol = float(np.linalg.norm(indata)/len(indata))
            if vol > 0.2:
                print("\r[ATENÇÃO] pico de energia (mock keyword)...", end="")
        with sd.InputStream(callback=callback):
            print("Escutando... Ctrl+C para sair")
            while True: time.sleep(0.1)
    except Exception as e:
        print("Sem sounddevice:", e)

def main():
    if os.environ.get("SIMULATE","0") != "1":
        print("Integre API de microfone/SDK da K10 e um modelo TFLite de keywords aqui.")
    else:
        pc_loop()

if __name__ == "__main__":
    main()
