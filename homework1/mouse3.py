import numpy as np
import cv2

def onChange(value):
    global image, title


    image[:] = cv2.getTrackbarPos('Brightness', title)
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)

title = '3번문제'
cv2.imshow(title, image)
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break


    if key == 2424832:
        value = cv2.getTrackbarPos('Brightness', title)
        cv2.setTrackbarPos('Brightness', title, value - 1)

    elif key == 2555904:
        value = cv2.getTrackbarPos('Brightness', title)
        cv2.setTrackbarPos('Brightness', title, value + 1)

    image[:] = cv2.getTrackbarPos('Brightness', title)
    cv2.imshow(title, image)

cv2.destroyAllWindows()