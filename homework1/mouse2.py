import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title, line, radius


    if event == cv2.EVENT_RBUTTONDOWN:

        cv2.circle(img, (x, y), radius, (120,30, 255), line)

    if event == cv2.EVENT_LBUTTONDOWN:

        cv2.rectangle(img, (x, y), (x+30, y+30), (235, 231, 32), line)

    cv2.imshow(title, img)

def line_bar(value):
    global line
    line = value
def radius_bar(value):
    global radius
    radius = value

title = '2번문제'
img = np.full((400, 300, 3), (255, 255, 255), np.uint8)

cv2.imshow(title, img)

line = 3
radius = 15


cv2.createTrackbar('line', title, 3, 12, line_bar)
cv2.setTrackbarMin('line', title, 1)

cv2.createTrackbar('radius', title, 15, 55, radius_bar)
cv2.setTrackbarMin('radius', title, 1)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)