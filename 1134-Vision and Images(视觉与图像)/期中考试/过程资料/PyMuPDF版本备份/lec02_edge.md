# lec02_edge

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

Lecture 2: Edge detection
CS4186: Computer Vision
Prof. Zhu Zhiyu

## Slide 2

Edge detection
• Convert a 2D image into a set of curves
– Extracts salient features of the scene
– More compact than pixels

## Slide 3

Origin of edges
• Edges are caused by a variety of factors
depth discontinuity
surface color discontinuity
illumination discontinuity
surface normal discontinuity

## Slide 4

Images as functions…
• Edges look like steep cliffs

## Slide 5

Characterizing edges
• An edge is a place of rapid change in the image intensity
function
image
intensity function
(along horizontal scanline)
first derivative
edges correspond to
extrema of derivative
Source: L. Lazebnik

## Slide 6

The gradient points in the direction of most rapid increase in intensity
Image gradient
• The gradient of an image:
The edge strength is given by the gradient magnitude:
The gradient direction is given by:
•
how does this relate to the direction of the edge?
Source: Steve Seitz

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

$$\nabla f = \left[\frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y}\right], \qquad \|\nabla f\| = \sqrt{\left(\tfrac{\partial f}{\partial x}\right)^2+\left(\tfrac{\partial f}{\partial y}\right)^2}, \qquad \theta = \tan^{-1}\!\left(\frac{\partial f/\partial y}{\partial f/\partial x}\right)$$

梯度方向 = 强度增加最快的方向；**边缘方向与梯度方向正交**。
## Slide 7

• How can we differentiate a digital image F[x,y]?
– Option 1:  reconstruct a continuous image, f, then
compute the derivative
– Option 2:  take discrete derivative (finite difference)
1
-1
How would you implement this as a linear filter?
Image derivatives
-1
1
:
:
Source: S. Seitz

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

有限差分求导（Option 2，离散导数）= 线性滤波：

$$\frac{\partial}{\partial x} \approx \begin{bmatrix}-1 & 0 & 1\end{bmatrix}, \qquad \frac{\partial}{\partial y} \approx \begin{bmatrix}-1 \\ 0 \\ 1\end{bmatrix}$$

写成 3×3 滤波核：

$$H_x = \begin{bmatrix} 0 & 0 & 0 \\ -1 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}, \qquad H_y = \begin{bmatrix} 0 & -1 & 0 \\ 0 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$
## Slide 8

Image gradient
Source: L. Lazebnik

## Slide 9

Effects of noise
Where is the edge?
Source: S. Seitz
Noisy input image

## Slide 10

Solution: smooth first
f
h
f * h
Source: S. Seitz
To find edges, look for peaks in

## Slide 11

• Differentiation is convolution, and convolution is associative:
• This saves us one operation:
Associative property of convolution
f
Source: S. Seitz
�
��  �∗ℎ = �
��∫� � ⋅ℎ �−� ��= ∫� � ⋅�
��ℎ �−� ��= �∗�
��ℎ

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

求导是卷积、卷积满足结合律：

$$\frac{\partial}{\partial x}(f * h) = \left(\frac{\partial}{\partial x} f\right) * h = f * \left(\frac{\partial}{\partial x} h\right)$$

→ "先平滑再求导"可合并为"直接用高斯导数核卷积"，省一次运算。
## Slide 12

The 1D Gaussian and its derivatives

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

一维高斯及其导数（解析式）：

$$G_\sigma(x) = \frac{1}{\sqrt{2\pi}\,\sigma} e^{-\frac{x^2}{2\sigma^2}}, \qquad G_\sigma'(x) = -\frac{x}{\sigma^2}\,G_\sigma(x)$$
## Slide 13

2D edge detection filters
Gaussian
derivative of Gaussian (x)

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

二维高斯：

$$h_\sigma(u,v) = \frac{1}{2\pi\sigma^2}\, e^{-\frac{u^2+v^2}{2\sigma^2}}$$
## Slide 14

Derivative of Gaussian filter
x-direction
y-direction

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

高斯导数（DoG）滤波核，x 方向：

$$\begin{pmatrix} 1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1 \end{pmatrix}$$

y 方向为其转置。符号约定（正负方向）与 Sobel 相同，仅差系数。
## Slide 15

The Sobel operator
• Common approximation of derivative of Gaussian
-1
0
1
-2
0
2
-1
0
1
1
2
1
0
0
0
-1
-2
-1
• The standard definition of the Sobel operator omits the 1/8 term
– doesn’t make a difference for edge detection
– the 1/8 term is needed to get the right gradient magnitude

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

Sobel 算子（高斯导数的常用近似）：

$$s_x = \frac{1}{8}\begin{pmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{pmatrix}, \qquad s_y = \frac{1}{8}\begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ -1 & -2 & -1 \end{pmatrix}$$

标准定义省略 $\tfrac{1}{8}$（不影响边缘检测）；要得到正确的梯度幅值需保留 $\tfrac{1}{8}$。
## Slide 16

Sobel operator: example
Source: Wikipedia

## Slide 17

（纯图片页，无文本层）

## Slide 18

Example
original image
Demo:  http://bigwww.epfl.ch/demo/ip/demos/edgeDetector/
Image credit: Joseph Redmon

## Slide 19

smoothed gradient magnitude
Finding edges

## Slide 20

thresholding
Finding edges
where is the edge?

## Slide 21

Get Orientation at Each Pixel
• Get orientation (below, threshold at minimum gradient magnitude)
θ = atan2(gy, gx)
0
360
Gradient orientation angle

## Slide 22

•
Check if pixel is local maximum along gradient direction
– requires interpolating pixels p and r
Non-maximum supression

## Slide 23

Before Non-max Suppression

## Slide 24

After Non-max Suppression

## Slide 25

Thresholding edges
• Still some noise
• Only want strong edges
• 2 thresholds, 3 cases
• R > T: strong edge
• R < T but R > t: weak
edge
• R < t: no edge
• Why two thresholds?

## Slide 26

Connecting edges
• Strong edges are edges!
• Weak edges are edges
iff they connect to strong
• Look in some neighborhood
(usually 8 closest)

## Slide 27

Canny edge
detector
1.
Filter image with derivative of Gaussian
2.
Find magnitude and orientation of gradient
3.
Non-maximum suppression
4.
Linking and thresholding (hysteresis):
–
Define two thresholds: low and high
–
Use the high threshold to start edge curves and the
low threshold to continue them
Source: D. Lowe, L. Fei-Fei, J. Redmon
MATLAB:  edge(image,‘canny’)

## Slide 28

Canny edge detector
Canny with
Canny with
original
•
The choice of         depends on desired behavior
– large       detects “large-scale” edges
– small       detects fine edges
Source: S. Seitz

## Slide 29

Scale space [Witkin 83]
•
Properties of scale space (w/ Gaussian smoothing)
– edge position may shift with increasing scale ()
– two edges may merge with increasing scale
– an edge may not split into two with increasing scale
larger
Gaussian filtered signal
first derivative peaks

## Slide 30

Questions?
