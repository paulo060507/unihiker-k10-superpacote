import os, cv2

ON_K10 = os.environ.get("SIMULATE","0") != "1"

def detector(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    return frame

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Sem câmera."); return
    while True:
        ok, frame = cap.read()
        if not ok: break
        out = detector(frame)
        cv2.imshow("Detector de rosto (ESC para sair)", out)
        if cv2.waitKey(1) & 0xFF == 27: break
    cap.release(); cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
