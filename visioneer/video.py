import sys
import cv2
import urllib

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
capture = cv2.VideoCapture(f'rtsp://192.168.1.20:554/user=admin&password=&channel={sys.argv[1]}&stream=0')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1920, 1080))

while capture.isOpened():
    ret, frame = capture.read()

    cv2.imshow('Capturing', frame)

    if ret:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out.release()
cv2.destroyAllWindows()
