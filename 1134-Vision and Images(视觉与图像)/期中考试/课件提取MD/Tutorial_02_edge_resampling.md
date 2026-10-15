Zhu Zhiyu

Tutorial 02: Edge Detection & Image Resampling

(1) Visualize the Gaussian Kernel and its derivative

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F196bd88d02bc473a9b7af4a943c2dd5a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253908&Signature=Y3FesEVTr9CifD8HllfDu9afmlk%3D)

Gaussian

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2Fa82273be741b46ddbd81e98b46dfe6e9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253908&Signature=1X51ad6bbsvosaY%2BwTHWR5z%2Ba7o%3D)

$$ h_{\sigma}(u,v)=\frac{1}{2\pi\sigma^{2}}e^{-\frac{u^{2}+v^{2}}{2\sigma^{2}}} $$

import numpy as np

import matplotlib.pyplot as plt

from mpl_tools.mplot3d import Axes3D

def generate_gaussian_plots():

# 1. Setup the grid

# Creating a coordinate grid from -3 to 3

x = np.linspace(-3, 3, 100)

y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

# 2. Define Parameters

sigma = 1.0

# 3. Calculate Gaussian (h_sigma)

# Formula: (1 / (2*pi*sigma^2)) * exp(-(u^2 + v^2) / (2*sigma^2))

gaussian = (1 / (2 * np.pi * sigma**2)) * np.exp(-(X**2 + Y**2) / (2 * sigma**2))

# 4. Calculate Derivative with respect to x (u direction)

# Analytical derivative: -x / sigma^2 * Gaussian

derivative_x = -(X / sigma**2) * gaussian

# 5. Visualization

fig = plt.figure(figsize=(14, 6))

# Plot 1: The Gaussian

ax1 = fig.add_subplot(1, 2, 1, projection='3d')

surf1 = ax1.plot_surface(X, Y, gaussian, cmap='gray', edgecolor='none', rstride=3, cstride=3, alpha=0.9)

ax1.set_title(r"Gaussian $h_\sigma(u, v)$", fontsize=14, y=1.02)

ax1.set_zlim(0, np.max(gaussian))

ax1.axis('off') # Turn off axes for a cleaner textbook look

# Plot 2: The Derivative of Gaussian (DoG)

ax2 = fig.add_subplot(1, 2, 2, projection='3d')

surf2 = ax2.plot_surface(X, Y, derivative_x, cmap='gray', edgecolor='none', rstride=3, cstride=3, alpha=0.9)

ax2.set_title(r"Derivative of Gaussian $\frac{\partial}{\partial x}$")

ax2.set_zlim(np.min(derivative_x), np.max(derivative_x))

ax2.axis('off')

plt.tight_layout()

plt.show()

if __name__ == "__main__":

generate_gaussian_plots()

(2) Sobel filtering the edges in the image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F5b4b1925ce074046b8c9aacdcd908fc7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253908&Signature=3Wp0R3Nnr5EoIHzhN151cPGTg6c%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F34585bcab4f843eca638d6eb8517e9e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253908&Signature=CnSxNwRXL58FEqJ83gYPFy3JPss%3D)

# 4. Create the HSV Image

# We create a blank image with 3 channels (Hue, Saturation, Value)

hsv = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

(2) Sobel filtering the edges in the image

Original Grayscale

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F6afe41a25c334980bab49fd51f8ae80e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253908&Signature=NOnkGQEccetL7xye9pa3A6IB9BE%3D)

Gradient Orientation (Colorized)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F06969f5d3d064f61bc8e15417fbe43e4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253908&Signature=2%2BqLwGZtvEFxfN0WwaexsH4QmB4%3D)

(3) Question: visualize the edge orientation

Edge Orientation

V.S. Gradient Orientation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F0129bdf650f74f98b452382649bd8d38.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253908&Signature=fVCXMbDVLKt9Q3lCuoTofLqpEjU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F943048e9a9994a1b8cb39fa7a17bab0a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253909&Signature=UKGw7ugXzuQaf5SiXEmkdaFac%2Fs%3D)

(4) Image Resampling: Visualizing Aliasing

Original Image (Smooth Curves)

Aliased Image (Downsampled 8x)

Note the jagged edges and Moiré patterns

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F9d988ce56336422d852751e564b7ec27.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253909&Signature=58Seu8mIP0fBqahdHEbubHTu%2BUA%3D)

import matplotlib.pyplot as plt

from PIL import Image

def create_aliasing_effect(image_path, factor=5):

Introduces aliasing by downsampling without a filter (Nearest Neighbor) and then upsampling back to original size to visualize the artifacts.

# Load the original image

img = Image.open(image_path)

original_width, original_height = img.size

# Calculate new "low res" dimensions

# We shrink the image significantly to force sampling errors

small_width = original_width // factor

small_height = original_height // factor

# Step 1: Downsample using Nearest Neighbor

# This is where the aliasing happens. We act as if we are sampling

# the signal at a rate too low for the frequency of the checks.

img_small = img.resize((small_width, small_height), resample=Image.NEAREST)

# Step 2: Upsample back to original size

# We do this so you can compare it side-by-side with the original.

# We use NEAREST again to keep the "blocky" aliased look sharp.

img_aliased = img_small.resize((original_width, original_height), resample=Image.NEAREST)

# Visualization

fig, axes = plt.subplots(1, 2, figsize=(15, 8))

axes[0].imshow(img)

axes[0].set_title("Original Image (Smooth Curves)")

axes[0].axis('off')

axes[1].imshow(img_aliased)

axes[1].set_title(f"Aliased Image (Downsampled {factor}x)\nNote the jagged edges and Moir $ \underline{\text{e patterns})\naxes[1].axis('off')} $

plt.tight_layout()

plt.show()

return img_aliased

except FileNotFoundError:

print(f"Error: The file 'image_path}' was not found.")

except Exception as e:

print(f"An error occurred: {e}")

# Run the function

# You can increase the 'factor' to make the effect more extreme

create_aliasing_effect('./Example_Image_04.png', factor=8)

(5) Robust Resampling with Gaussian Blur

Original Image

Aliased (Jagged)

Downsampled 4x directly

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F814bb1db665a4e1e984a88eb2005e8f5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253909&Signature=pRcGBahiHQo%2FGZoGrdfNbur%2BV9M%3D)

Anti-Aliased (Smooth)

Gaussian Blur (r=2.0) -> Downsampled

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F14b6f517c00d4764ba31ab0bb389902c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253909&Signature=gna4DezNZvjQJYHqi8b%2B2Q8TojY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F66cbaffdf03c43e98edb9e817549b6ff%2Fmedia%2F5df490b0b7d947c4a12fbc51bc052f50.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253909&Signature=RUGk1iBjbbd4UKBwvMRfvMsT%2BxQ%3D)

(5) Robust Resampling with Gaussian Blur

import matplotlib.pyplot as plt

from PIL import Image, ImageFilter

def create_antialiasing_effect(image_path, factor=4):

.....

Demonstrates Anti-Aliasing by applying a Gaussian Blur before downsampling.

try:

# Load the original image

img = Image.open(image_path)

original_width, original_height = img.size

# Calculate new "low res" dimensions

small_width = original_width // factor

small_height = original_height // factor

# --- 1. Create the ALIASED version (Bad) ---

# Just downsample directly with Nearest Neighbor.

# This causes the jagged edges and Moin patterns.

img_aliased_small = img.resize((small_width, small_height), resample=Image.NEAREST)

img_aliased = img_aliased_small.resize((original_width, original_height), resample=Image.NEAREST)

# --- 2. Create the ANTI-ALIASED version (Good) ---

# Step A: Low-pass filter (Gaussian Blur).

# We blur the image to remove high frequencies that the small resolution can't handle.

# A radius roughly half the downsampling factor is a good rule of thumb.

blur_radius = factor/2

img_blurred = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

# Step B: Downsample the blurred image.

img_aa_small = img_blurred.resize((small_width, small_height), resample=Image.NEAREST)

# Step C: Upsample back for visualization

img_antialiased = img_aa_small.resize((original_width, original_height), resample=Image.NEAREST)

# --- Visualization ---

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot Original

axes[0].imshow(img)

axes[0].set_title("Original Image")

axes[0].axis('off')

axes[1].imshow(img_aliased)

axes[1].set_title(f"Aliased (Jagged)\nDownsampled {factor}x directly")

axes[1].axis('off')

# Plot Anti-Aliased

axes[2].imshow(img_antialiased)

axes[2].set_title(f"Anti-Aliased (Smooth)\nGaussian Blur (r={blur_radius}) -> Downsampled")

axes[2].axis('off')

plt.tight_layout()

plt.show()

except FileNotFoundError:

print(f"Error: The file 'image_path}' was not found.")

except Exception as e:

print(f"An error occurred: {e}")

# Run the function

# Using a factor of 4 makes the difference very obvious

create_antialiasing_effect()./Example_Image_04.png', factor=4)

**Questions?**
