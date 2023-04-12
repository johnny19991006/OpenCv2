import cv2
import numpy as np

def nothing(x):
    pass


img = cv2.imread('images/topgun.jpg')

cv2.namedWindow('Changed')


cv2.createTrackbar('brightness', 'Changed', 0, 100, nothing)
cv2.createTrackbar('color', 'Changed', 0, 100, nothing)
cv2.createTrackbar('sharpness', 'Changed', 0, 100, nothing)

while True:

    brightness = cv2.getTrackbarPos('brightness', 'Changed')
    color = cv2.getTrackbarPos('color', 'Changed')
    sharpness = cv2.getTrackbarPos('sharpness', 'Changed')

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    hsv[..., 2] += brightness
    hsv[..., 1] += color
    hsv[..., 2] += sharpness


    img_changed = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


    cv2.imshow('Changed', img_changed)


    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()