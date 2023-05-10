import numpy as np, cv2
from Common.interpolation import bilinear_value
from Common.utils import contain


def rotate_color(img, degree, center):
    height, width = img.shape[:2]

    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    dst = np.zeros((height, width, 3), dtype=img.dtype)
    for i in range(height):
        for j in range(width):
            jj, ii = np.subtract((j, i), center)
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x, y = np.add((x, y), center)

            if contain((y, x), (height, width)):
                for k in range(3):
                    dst[i, j, k] = bilinear_value(img[..., k], [x, y])

    return dst


image = cv2.imread('images/rotate.jpg', cv2.IMREAD_COLOR)
if image is None:raise Exception("에러")

center = (image.shape[1] // 2, image.shape[0] // 2)
dst = rotate_color(image, 30, center)

cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey()