import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt


    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
            cv2.circle(image, pt, 1, 0, 2)
        else:
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            pt = (-1, -1)


    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
            cv2.circle(image, pt, 1, 0, 2)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx * dx + dy * dy))
            cv2.circle(image, pt, radius, (0, 0, 255), 2)
            pt = (-1, -1)


    elif flags == cv2.EVENT_FLAG_MBUTTON:
        if pt[0] < 0:
            pt = (x, y)
            cv2.circle(image, pt, 1, 0, 2)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx * dx + dy * dy))
            cv2.ellipse(image, pt, (100, radius), 0, 0, 360, (0, 255, 0), 2)
            pt = (-1, -1)

    cv2.imshow(title, image)


image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)

title = "4번문제"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)