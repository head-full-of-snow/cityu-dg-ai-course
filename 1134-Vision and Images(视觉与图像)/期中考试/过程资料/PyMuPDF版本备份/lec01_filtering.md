# lec01_filtering

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

Lecture 1: Images and image filtering
Hybrid Images, Oliva et al., http://olivalab.mit.edu/hybridimage.htm
Zhu Zhiyu
CS5187: Vision & Image

## Slide 2

What is an image?

## Slide 3

Digital Camera
The Eye
Source: A. Efros
We’ll focus on these in this class
(More on this process later)
What is an image?

## Slide 4

• A grid (matrix) of intensity values
(common to use one byte per value: 0 = black, 255 = white)
=
255 255 255 255 255 255 255 255 255 255 255 255
255 255 255 255 255 255 255 255 255 255 255 255
255 255 255
20
0 255 255 255 255 255 255 255
255 255 255
75
75
75 255 255 255 255 255 255
255 255
75
95
95
75 255 255 255 255 255 255
255 255
96 127 145 175 255 255 255 255 255 255
255 255 127 145 175 175 175 255 255 255 255 255
255 255 127 145 200 200 175 175
95 255 255 255
255 255 127 145 200 200 175 175
95
47 255 255
255 255 127 145 145 175 127 127
95
47 255 255
255 255
74 127 127 127
95
95
95
47 255 255
255 255 255
74
74
74
74
74
74 255 255 255
255 255 255 255 255 255 255 255 255 255 255 255
255 255 255 255 255 255 255 255 255 255 255 255
What is an image?

## Slide 5

• Can think of a (grayscale) image as a function f from R2 to R:
– f (x,y) gives the intensity at position (x,y)
– A digital image is a discrete (sampled, quantized) version of this function
x
y
f (x, y)
snoop
3D view
What is an image?

## Slide 6

• As with any function, we can apply operators to an image
• Today we’ll talk about a special kind of operator, convolution
(linear filtering)
g (x,y) = f (x,y) + 20
g (x,y) = f (-x,y)
Image transformations

## Slide 7

Filters
• Filtering
– Form a new image whose pixel values are a combination of the original
pixel values
• Why?
– To get useful information from images
• E.g., extract edges or contours (to understand shape)
– To enhance the image
• E.g., to remove noise
• E.g., to sharpen and “enhance image” a la CSI
– A key operator in Convolutional Neural Networks

## Slide 8

Canonical Image Processing problems
• Image Restoration
– denoising
– deblurring
• Image Compression
– JPEG, HEIF, MPEG, …
• Locating Structural Features
– corners
– edges

## Slide 9

Question: Noise reduction
• Given a camera and a still scene, how can you reduce noise?
Take lots of images and average them!
What’s the next best thing?
Source: S. Seitz

## Slide 10

Image filtering
• Modify the pixels in an image based on some function of a
local neighborhood of each pixel
5
1
4
1
7
1
5
3
10
Local image data
7
Modified image data
Some function
Source: L. Zhang

## Slide 11

Linear filtering
• One simple version of filtering:  linear filtering (cross-correlation,
convolution)
– Replace each pixel by a linear combination (a weighted sum) of its neighbors
• The prescription for the linear combination is called the “kernel” (or
“mask”
, “filter”)
0.5
0.5
0
0
1
0
0
0
0
kernel
8
Modified image data
Source: L. Zhang
Local image data
6
1
4
1
8
1
5
3
10

## Slide 12

Let       be the image,      be the kernel (of size
2k+1 x 2k+1), and      be the output image
•
Can think of as a “dot product” between local
neighborhood and kernel for each pixel
Convolution
This is called a convolution operation:

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

$$G[i,j] = \sum_{u=-k}^{k}\sum_{v=-k}^{k} H[u,v]\,F[i-u,\ j-v]$$

即卷积运算 $G = H * F$（可视为局部邻域与 kernel 的"点积"）。
## Slide 13

Convolution
Adapted from F. Durand

## Slide 14

Mean filtering
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
90
90
90
90
90
0
0
0
0
0
90
90
90
90
90
0
0
0
0
0
90
90
90
90
90
0
0
0
0
0
90
0
90
90
90
0
0
0
0
0
90
90
90
90
90
0
0
0
0
0
0
0
0
0
0
0
0
0
0
90
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1 *
=
0
10
20
30
30
30
20
10
0
20
40
60
60
60
40
20
0
30
60
90
90
90
60
30
0
30
50
80
80
90
60
30
0
30
50
80
80
90
60
30
0
20
30
50
50
60
40
20
10
20
30
30
30
30
20
10
10
10
10
0
0
0
0
0

## Slide 15

Mean filtering / Moving average

## Slide 16

Mean filtering / Moving average

## Slide 17

Mean filtering / Moving average

## Slide 18

Mean filtering / Moving average

## Slide 19

Mean filtering / Moving average

## Slide 20

Mean filtering / Moving average

## Slide 21

Linear filters: examples
0
0
0
0
1
0
0
0
0
Original
Source: D. Lowe
*

## Slide 22

Linear filters: examples
0
0
0
0
1
0
0
0
0
Original
Identical image
Source: D. Lowe
*
=

## Slide 23

Linear filters: examples
0
0
0
0
0
1
0
0
0
Original
Source: D. Lowe
*

## Slide 24

Linear filters: examples
0
0
0
0
0
1
0
0
0
Original
Shifted left by 1 pixel
Source: D. Lowe
*
=

## Slide 25

Linear filters: examples
Original
1
1
1
1
1
1
1
1
1
Blur (with a mean filter)
Source: D. Lowe
*
=

## Slide 26

Linear filters: examples
Original
1
1
1
1
1
1
1
1
1
0
0
0
0
2
0
0
0
0
-
Sharpening filter
(accentuates edges)
Source: D. Lowe
=
*

## Slide 27

Sharpening
Source: D. Lowe

## Slide 28

Smoothing with box filter revisited
Source: D. Forsyth

## Slide 29

Gaussian kernel
Source: C. Rasmussen

## Slide 30

Gaussian filters
= 30 pixels
= 1 pixel
= 5 pixels
= 10 pixels

## Slide 31

Mean vs. Gaussian filtering

## Slide 32

Gaussian filter
• Removes “high-frequency” components from the image
(low-pass filter)
• Convolution with self is another Gaussian
– Convolving twice with Gaussian kernel of width
= convolving once with kernel of width
Source: K. Grauman
*
=

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

$$G_{\sigma_1} * G_{\sigma_2} = G_{\sqrt{\sigma_1^2+\sigma_2^2}}$$

与自身卷积两次宽度为 $\sigma$ 的 Gaussian kernel $=$ 用宽度 $\sqrt{2}\,\sigma$ 的 kernel 卷积一次。

二维高斯核（标准形式，同 Tutorial 02）：

$$h_\sigma(u,v) = \frac{1}{2\pi\sigma^2}\, e^{-\frac{u^2+v^2}{2\sigma^2}}$$
## Slide 33

Sharpening revisited
• What does blurring take away?
original
smoothed (5x5)
–
detail
=
sharpened
=
Let’s add it back:
original
detail
+ α
(This “detail extraction” operation is also
called a high-pass filter)
Photo credit: https://www.flickr.com/photos/geezaweezer/16089096376/

## Slide 34

Sharpen filter
Gaussian
scaled impulse
Sharpen filter
image
blurred
image
unit impulse
(identity kernel
with single 1 in
center, zeros
elsewhere)
+

## Slide 35

Sharpen filter
unfiltered
filtered

## Slide 36

Source: https://www.diyphotography.net/diy_create_your_own_bokeh/
Bokeh: Blur in out-of-focus regions of an image.
Camera shake
*
=
Source: Fergus, et al. “Removing Camera Shake from a Single Photograph”
, SIGGRAPH 2006
“Optical” convolution

## Slide 37

Filters: Thresholding

## Slide 38

Linear filters
• Can thresholding be implemented with a linear filter?

## Slide 39

Questions?
