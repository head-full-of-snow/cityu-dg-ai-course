Zhu Zhiyu

Tutorial 03: Feature Detection

(1) Implementing the Harris Corner Response

Objective: Manually compute the Harris response function to identify interest points.

**Experiment:**

•Compute image derivatives $I_x$ and $I_y$ using Sobel filters.

•Construct the second moment matrix $H$ by computing the weighted sums of $I_x^2$, $I_y^2$, and $I_x I_y$ using a Gaussian window.

•Calculate the cornerness score $R = \det(H) - k \cdot \det(\text{trace}(H))^2$ for each pixel.

• Visualization: Display the $R$ values as a heatmap where red represents high cornerness and blue represents low cornerness.

(1) Implementing the Harris Corner Response

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2ad282de6ca84037bfbf02cb6e5e2875%2Fmedia%2F51a7153a2c49487e89bd2203c71fd840.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253929&Signature=PylT4UWgwUT02kGNB0XwNR%2F0UNk%3D)

import cv2

import numpy as np

import matplotlib.pyplot as plt

def harris_response(img, k=0.04, window_size=21):

# 1. Image derivatives using Sobel

Ix = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=31)

Iy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=31)

# 2. Square of derivatives

Ix2 = Ix**2

Iy2 = Iy**2

Ixy = Ix * Iy

# 3. Gaussian filter to weight the derivatives

Sxx = cv2.GaussianBlur(Ix2, (window_size, window_size), 1)

Syy = cv2.GaussianBlur(Iy2, (window_size, window_size), 1)

Sxy = cv2.GaussianBlur(Ixy, (window_size, window_size), 1)

# 4. Cornerness function: R = det(H) - k * (trace(H))^2 [cite: 23, 24]

det_H = (Sxx * Syy) - (Sxy**2)

trace_H = Sxx + Syy

R = det_H - k * (trace_H**2)

# threshold = 0.05 * R.max()

R_visual = cv2.normalize(R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

return R_visual

# Load and visualize the heatmap

img = cv2.imread('example_image_02.jpg', 0)

R_map = harris_response(img)

plt.imshow(R_map, cmap='jet')

plt.title("Harris Response Heatmap (f-value)"

plt.colorbar()

plt.show()

(2) Non-Maximum Suppression (NMS) and Thresholding

Detected Harris Features

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2ad282de6ca84037bfbf02cb6e5e2875%2Fmedia%2Fa533544f234448e886264b6d29d5a578.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253929&Signature=oltSPM8IeDDZGS3X3eJpWcwMMhY%3D)

Detected Harris Features

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2ad282de6ca84037bfbf02cb6e5e2875%2Fmedia%2F0d90bd3cf74a4102b87943a6e5be4c80.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253929&Signature=lhNzNvYHw1x5OK%2F38K2IVJp1vMc%3D)

(2) Non-Maximum Suppression (NMS) and Thresholding import cv2 import numpy as np import matplotlib.pyplot as plt

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2ad282de6ca84037bfbf02cb6e5e2875%2Fmedia%2F3e08fc56133b4e3bb1f82bec0fa9ee08.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253930&Signature=DYZJ7s6td1uIHhotikv%2Bb86fvhM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2ad282de6ca84037bfbf02cb6e5e2875%2Fmedia%2Fbebd33fb12134b8682da8dbb11edb364.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253930&Signature=9OAOewDwxFRe1dkIOe1pavsahcI%3D)

You can change the ratio

# (3) Invariance Testing: Rotation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2ad282de6ca84037bfbf02cb6e5e2875%2Fmedia%2F46c124d84fcf4be5bcc316d9898c4b23.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253930&Signature=M9ptKX1cs2vayTOL13KmSkpoTlA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2ad282de6ca84037bfbf02cb6e5e2875%2Fmedia%2F0339b08df3e3446f84091c21126121e1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253930&Signature=lcUngwaK0amVaRyXlKaFOI506Kk%3D)

def harris_response(img, k=0.04, window_size=5):

# Use a smaller ksize for local gradients

Ix = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

Iy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

Ix2, Iy2, Ixy = Ix**2, Iy**2, Ix*Iy

# Use a smaller window (e.g., 5x5) for better localization

Sxx = cv2.GaussianBlur(Ix2, (window_size, window_size), 0)

Syy = cv2.GaussianBlur(Iy2, (window_size, window_size), 0)

Sxy = cv2.GaussianBlur(Ixy, (window_size, window_size), 0)

det_H = (Sxx * Syy) - (Sxy**2)

trace_H = Sxx + Syy

R = det_H - k * (trace_H**2)

# Load and visualize the heatmap

img = cv2.imread('example_image.jpg', 0)

R_map = harris_response(img)

# plt.imshow(R_map, cmap='jet')

# plt.title("Harris Response Heatmap (f-value)")

# plt.colorbar()

# plt.show()

def detect_corners(R, threshold_ratio=0.7):

# Thresholding: Keep only values above a certain percentage of max R

threshold = threshold_ratio * R.max()

R_thresholded = np.copy(R)

R_thresholded[R < threshold] = 0

# Non-maximum suppression: find local maxima

# Dilate replaces each pixel with the maximum in its neighborhood

local_max = cv2.dilate(R_thresholded, None)

corners = (R_thresholded == local_max) & (R_thresholded > 0)

return corners

def rotate_image(image, angle):

(h, w) = image.shape[:2]

center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, angle, 1.0)

return cv2.warpAffine(image, M, (w, h))

# Compare original vs rotated

img_rotated = rotate_image(img, 45)

R_rotated = harris_response(img_rotated)

corners = detect_corners(R_map)

corners_rotated = detect_corners(R_rotated)

# Visualization: Students should see that corners "follow" the rotation [cite: 253]

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title("Original")

y, x = np.where(corners)

plt.scatter(x, y, s=10, c='red', marker='x')

plt.subplot(122), plt.imshow(img_rotated, cmap='gray'), plt.title("Rotated 45")

y, x = np.where(corners_rotated)

plt.scatter(x, y, s=10, c='red', marker='x')

plt.show()

**Questions?**
