import cv2

camera = cv2.VideoCapture(0)

size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))

recorder = cv2.VideoWriter("output_save.mp4", cv2.VideoWriter.fourcc(*"mp4v"), 30, size)

isRecording = False
isPaused = False
while True:
    success, image = camera.read()
    if not success:
        break

    key = cv2.waitKey(1) & 0XFF

    if key == ord('s'):
        cv2.rectangle(image, (10,10),(30,30), (0,0 ,255), -1)
        print("Recording started")
        isRecording = True
    if key == ord('e'):
        print("Recoring ended")
        isRecording = False
    if key == ord('p'):
        print(f"Recording {'paused' if isPaused else 'resume'}")
        isPaused = not isPaused

    if key == ord('q'):
        print("QUITTING..............")
        break
    
    if isRecording:
        recorder.write(image)
        cv2.imshow("Webcam", image)
    else:
        cv2.imshow("Webcam", image)

camera.release()
recorder.release()
cv2.destroyAllWindows()