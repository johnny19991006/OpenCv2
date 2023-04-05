import cv2
import numpy as np

# Read image file
logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None:
    raise Exception("영상파일 읽기 오류")

# Split RGB color channels
blue, green, red = cv2.split(logo)
blue_img = cv2.merge((blue, np.zeros_like(blue), np.zeros_like(blue)))
green_img = cv2.merge((np.zeros_like(green), green, np.zeros_like(green)))
red_img = cv2.merge((np.zeros_like(red), np.zeros_like(red), red))

# Display each color channel as a separate image
cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
