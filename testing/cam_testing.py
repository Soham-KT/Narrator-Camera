import cv2
import time

cap = cv2.VideoCapture(0)
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('camera', frame)

    if time.time() - start_time >= 5:
        print('5 seconds passed')
        start_time = time.time()

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()