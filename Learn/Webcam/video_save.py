import cv2

camera = cv2.VideoCapture(0)

size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))

recorder = cv2.VideoWriter("output.mp4", cv2.VideoWriter.fourcc(*"mp4v"), 30, size)

while True:
    success, frame = camera.read()

    if not success:
        break

    recorder.write(frame)
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1) & 0XFF
    if key == ord('q'):
        print("QUITTING..............")
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()