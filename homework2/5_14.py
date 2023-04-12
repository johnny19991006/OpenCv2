import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image file
img = cv2.imread('images/castle.jpg')

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define histogram parameters
h_bins = 180
s_bins = 256
hist_size = [h_bins, s_bins]
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges
hist = np.zeros((h_bins, s_bins), dtype=np.float32)

# Calculate 2D histogram
hist = cv2.calcHist([hsv], [0, 1], None, hist_size, ranges, accumulate=False)

# Display histogram
plt.imshow(hist, interpolation='nearest')
plt.show()
