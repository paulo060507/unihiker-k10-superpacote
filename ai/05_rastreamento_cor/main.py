import cv2, numpy as np

LOW  = (20, 100, 100)  # amarelo-ish
HIGH = (30, 255, 255)

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Sem câmera."); return
    while True:
        ok, frame = cap.read()
        if not ok: break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, LOW, HIGH)
        cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if cnts:
            c = max(cnts, key=cv2.contourArea)
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 2)
        cv2.imshow("mask", mask)
        cv2.imshow("track (ESC sai)", frame)
        if cv2.waitKey(1) & 0xFF == 27: break
    cap.release(); cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
