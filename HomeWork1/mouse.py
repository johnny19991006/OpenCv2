import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title


    if event == cv2.EVENT_RBUTTONDOWN:

        cv2.circle(img, (x, y), 20, (55, 234, 235), 2)

    if event == cv2.EVENT_LBUTTONDOWN:

        cv2.rectangle(img, (x, y), (x+30, y+30), (255, 122, 122), 2)

    cv2.imshow(title, img)

img = np.full((400, 300, 3), (255, 255, 255), np.uint8)
title = '1번문제'
cv2.imshow(title, img)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()