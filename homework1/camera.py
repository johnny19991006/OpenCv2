import cv2



capture = cv2.VideoCapture(0)


capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

title = "6번문제"
cv2.namedWindow(title)

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(100) == 27: break

    blue, green, red = cv2.split(frame)

    cv2.add(green[100:300, 200:300], 50, green[100:300, 200:300])

    frame = cv2.merge([blue, green, red])

    cv2.rectangle(frame, (200, 200), (300, 300), (0, 0, 255), 2)

    cv2.imshow(title, frame)

capture.release()