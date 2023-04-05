import numpy as np
import cv2 as cv

image = np.zeros((300, 400), np.uint8)
image.fill(200)

cv.imshow("Window title", image)
cv.waitKey(3000)
cv.destoryAllwindows()


