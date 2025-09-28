import cv2

face_cascade = cv2.CascadeClassifier("Learn/Face_detection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Learn/Face_detection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("Learn/Face_detection/haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    
        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]

        eye = eye_cascade.detectMultiScale(face_gray, 1.1, 5)

        if len(eye) > 0:
            cv2.putText(frame, "Eye detected", (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255), 2)

        smile = smile_cascade.detectMultiScale(face_gray, 1.1, 9)
        if len(smile) > 0:
            cv2.putText(frame, "Smile detected", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255), 2)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    cv2.imshow("Face Smile Eye Detector", frame)

cap.release()
cv2.destroyAllWindows()