# lec03_resample

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

Image Resampling , Interpolation
CS4186: Vision & Image
Prof. Zhu Zhiyu

## Slide 2

Image scaling
This image is too big to fit on the
screen.  How can we generate a
half-sized version?
Source: S. Seitz

## Slide 3

Image sub-sampling
Throw away every other row and
column to create a 1/2 size image
- called image sub-sampling
1/4
1/8
Source: S. Seitz

## Slide 4

Image sub-sampling
1/4  (2x zoom)
1/8  (4x zoom)
Why does this look so crufty?
1/2
Source: S. Seitz

## Slide 5

Image sub-sampling – another example
Source: F. Durand

## Slide 6

Even worse for synthetic images
Source: L. Zhang

## Slide 7

Aliasing
• Occurs when your sampling rate is not high enough to capture the amount of
detail in your image
• Can give you the wrong signal/image—an alias
• To do sampling right, need to understand the structure of your signal/image
• Enter Monsieur Fourier…
– “But what is the Fourier Transform? A visual introduction.”
To avoid aliasing:
– sampling rate ≥ 2 * max frequency in the image
• said another way: ≥ two samples per cycle
– This minimum sampling rate is called the Nyquist rate
Source: L. Zhang

## Slide 8

Wagon-wheel effect
(See http://www.michaelbach.de/ot/mot-wagonWheel/index.html)
Source: L. Zhang

## Slide 9

Wagon-wheel effect
https://en.wikipedia.org/wiki/Wagon-wheel_effect

## Slide 10

Temporal aliasing – helicopter blades
https://www.youtube.com/watch?v=yr3ngmRuGUc

## Slide 11

Aliasing in practice

## Slide 12

Aliasing
• When downsampling by a factor of two
– Original image has frequencies that are too high
• How can we fix this?

## Slide 13

Gaussian pre-filtering
G 1/4
G 1/8
Gaussian 1/2
• Solution: filter the image, then subsample
Source: S. Seitz

## Slide 14

Subsampling with Gaussian pre-filtering
G 1/4
G 1/8
Gaussian 1/2
• Solution: filter the image, then subsample
Source: S. Seitz

## Slide 15

Compare with...
1/4  (2x zoom)
1/8  (4x zoom)
1/2
Source: S. Seitz

## Slide 16

Gaussian pre-
filtering
•
Solution: filter
the image, then
subsample
blur
F0   H
*
subsample
blur
subsample …
F1
F1   H
*
F2
F0

## Slide 17

blur
F0   H
*
subsample
blur
subsample …
F1
F1   H
*
F2
F0
{
Gaussian
pyramid

## Slide 18

（纯图片页，无文本层）

## Slide 19

Gaussian pyramids [Burt and Adelson, 1983]
• In computer graphics, a mip map
[Williams, 1983]
• A precursor to wavelet transform
Gaussian Pyramids have all sorts of
applications in computer vision
Source: S. Seitz

## Slide 20

Q: How much space does a
Gaussian pyramid take compared
to the original image?
Source: S. Seitz
Gaussian pyramids [Burt and Adelson, 1983]

## Slide 21

Gaussian pyramid

## Slide 22

Gaussian pyramid
Answer: 4/3 the amount of space as the original image alone
See https://en.wikipedia.org/wiki/Geometric_series

## Slide 23

Back to the checkerboard
• What should happen when you make the
checkerboard smaller and smaller?
Naïve subsampling
Proper prefiltering
(“antialiasing”)
Image turns grey!
(Average of black and
white squares,
because each pixel
contains both.)

## Slide 24

Questions?

## Slide 25

Upsampling
• This image is too small for this screen:
• How can we make it 10 times as big?
• Simplest approach:
repeat each row
and column 10 times
• (“Nearest neighbor
interpolation”)

## Slide 26

Image interpolation
Recall that a digital images is formed as follows:
•
It is a discrete point-sampling of a continuous function
•
If we could somehow reconstruct the original function, any new
image could be generated, at any resolution and scale
1
2
3
4
5
Adapted from: S. Seitz
d = 1 in this
example

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

数字图像 = 连续函数的点采样 + 量化：

$$F[x,y] = \text{quantize}\big(f(xd,\ yd)\big) \quad (d\ \text{为采样间隔，本例 } d=1)$$
## Slide 27

Image interpolation
1
2
3
4
5
d = 1 in this
example
Recall that a digital images is formed as follows:
•
It is a discrete point-sampling of a continuous function
•
If we could somehow reconstruct the original function, any new
image could be generated, at any resolution and scale
Adapted from: S. Seitz

## Slide 28

Image interpolation
1
2
3
4
5
2.5
1
•
Convert      to a continuous function:
•
Reconstruct by convolution with a reconstruction filter, h
• What if we don’t know    ?
•
Guess an approximation:
•
Can be done in a principled way: filtering
d = 1 in this
example
Adapted from: S. Seitz

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

重建：把离散样本转成连续函数，再与重建滤波器 $h$ 卷积：

$$\tilde{f} = h * \tilde{f}_F$$

（$\tilde{f}_F$ 为离散样本脉冲串；不知道真实 $f$ 时用其近似。）
## Slide 29

Image interpolation
“Ideal” reconstruction
Nearest-neighbor
interpolation
Linear interpolation
Gaussian reconstruction
Source: B. Curless

## Slide 30

Reconstruction filters
• What does the 2D version of this hat function look like?
Often implemented without cross-correlation
•
E.g., http://en.wikipedia.org/wiki/Bilinear_interpolation
Better filters give better resampled images
•
Bicubic is common choice
performs
linear interpolation
(tent function) performs
bilinear interpolation
Cubic reconstruction filter

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

- 帽函数 hat（1D）→ 线性插值；2D 帐篷函数 tent → **双线性插值**（常直接实现，不用显式卷积）。
- 三次重建滤波 → **bicubic**，重建质量更好，是常用选择。
## Slide 31

Image interpolation
Nearest-neighbor interpolation
Bilinear interpolation
Bicubic interpolation
Original image:          x 10

## Slide 32

Also used for resampling
Image interpolation

## Slide 33

Modern methods
From Romano, et al: RAISR: Rapid and Accurate Image Super Resolution,
https://arxiv.org/abs/1606.01299

## Slide 34

Super-resolution with multiple images
• Can do better upsampling if you have multiple images of the
scene taken with small (subpixel) shifts
• Some cellphone cameras (like the Google Pixel line) capture a
burst of photos
• Can we use that burst for upsampling?

## Slide 35

Google Pixel 3 Super Res Zoom
Effect of hand tremor as seen in a cropped
burst of photos, after global alignment
https://ai.googleblog.com/2018/10/see-better-and-further-with-super-res.html
Example photo with and without super res
zoom (smart burst align and merge)

## Slide 36

Image interpolation
Recall that a digital images is formed as follows:
•
It is a discrete point-sampling of a continuous function
•
If we could somehow reconstruct the original function, any new
image could be generated, at any resolution and scale
1
2
3
4
5
d = 1 in this
example

## Slide 37

Summary
• Key points:
– Subsampling an image can cause aliasing. Better is to blur (“pre-
filter”) to remove high frequencies then downsample
– If you repeatedly blur and downsample by 2x, you get a Gaussian
pyramid
– Upsampling an image requires interpolation. This can be posed
as convolution with a “reconstruction kernel”

## Slide 38

Questions?
