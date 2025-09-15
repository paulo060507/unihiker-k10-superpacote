import cv2, numpy as np

THRESH = 25

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Sem câmera."); return
    ret, prev = cap.read()
    if not ret: print("Falha inicial."); return
    prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    while True:
        ok, frame = cap.read()
        if not ok: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(prev_gray, gray)
        _, mask = cv2.threshold(diff, THRESH, 255, cv2.THRESH_BINARY)
        area = int(np.sum(mask>0))
        if area > 5000: print("Movimento! área:", area)
        prev_gray = gray
        cv2.imshow("mov (ESC sai)", mask)
        if cv2.waitKey(1) & 0xFF == 27: break
    cap.release(); cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
