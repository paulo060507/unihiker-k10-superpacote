import cv2
from pyzbar.pyzbar import decode

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Sem câmera."); return
    while True:
        ok, frame = cap.read()
        if not ok: break
        codes = decode(frame)
        for c in codes:
            x,y,w,h = c.rect
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            txt = c.data.decode("utf-8", errors="ignore")
            cv2.putText(frame, txt, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0), 1)
            print("QR:", txt)
        cv2.imshow("qr (ESC sai)", frame)
        if cv2.waitKey(1) & 0xFF == 27: break
    cap.release(); cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
