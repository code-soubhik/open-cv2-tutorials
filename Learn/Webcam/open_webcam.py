import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam not opened")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Something went wrong")
        break
    key = cv2.waitKey(1)
    if key & 0XFF == ord('q'):
        print("quiting....")
        break
    cv2.imshow("Video", frame)


cap.release()
cv2.destroyAllWindows()