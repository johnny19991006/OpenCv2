import cv2
from Common.utils import put_string

def bright_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS, value)

def cont_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST, value)

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 0)

title = "5번문제"
cv2.namedWindow(title)
cv2.createTrackbar("brightness", title, 0, 100, bright_bar)
cv2.createTrackbar("contrast", title, 0, 100, cont_bar)

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(100) == 27: break

    bright = int(capture.get(cv2.CAP_PROP_BRIGHTNESS))
    cont = int(capture.get(cv2.CAP_PROP_CONTRAST))
    put_string(frame, "brightness : ", (10, 240), bright)
    put_string(frame, "contrast : ", (10, 270), cont)
    cv2.imshow(title, frame)

capture.release()