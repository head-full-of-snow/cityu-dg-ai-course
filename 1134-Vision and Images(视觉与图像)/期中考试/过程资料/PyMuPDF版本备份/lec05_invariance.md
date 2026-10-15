# lec05_invariance

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

CS5187: Vision & Image
Feature invariance

## Slide 2

Local features: main components
1) Detection: Identify the interest points
2) Description: Extract vector feature
descriptor surrounding each interest
point.
3) Matching: Determine correspondence
between descriptors in two views
]
,
,
[
)
1
(
)
1
(
1
1
d
x
x


x
]
,
,
[
)
2
(
)
2
(
1
2
d
x
x


x
Kristen Grauman

## Slide 3

Harris features (in red)

## Slide 4

Image transformations
• Geometric
Rotation
Scale
• Photometric
Intensity change

## Slide 5

Invariance and equivariance
•
We want corner locations to be invariant to
photometric transformations and equivariant to
geometric transformations
– Invariance: image is transformed and corner
locations do not change
– Equivariance: if we have two transformed
versions of the same image, features should
be detected in corresponding locations
– (Sometimes “invariant” and “equivariant” are
both referred to as “invariant”)
– (Sometimes “equivariant” is called “covariant”)

## Slide 6

Harris detector invariance properties:
image translation
•  Derivatives and window function are equivariant
Corner location is equivariant w.r.t. translation

## Slide 7

Harris detector invariance properties:
image rotation
Second moment ellipse rotates but its shape (i.e.
eigenvalues) remains the same
Corner location is equivariant w.r.t. image rotation

## Slide 8

Harris detector invariance properties:
Affine intensity change
•   Only derivatives are used to compute Harris scores 
invariance to intensity shift I  I + b
•   Intensity scaling: I  a I
R
x (image coordinate)
threshold
R
x (image coordinate)
Partially invariant to affine intensity change
I  a I + b

## Slide 9

Harris detector invariance properties: scaling
All points will be
classified as edges
Corner
Neither invariant nor equivariant to scaling

## Slide 10

Scale invariant detection
Suppose you’re looking for corners
Key idea:  find scale that gives local maximum of f
– in both position and scale
– One definition of f: the Harris operator

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

尺度不变检测关键思想：在**位置和尺度**上都取 $f$ 的局部最大：

$$f = \text{Harris 算子（一种 } f \text{ 的定义）}$$

对每个候选点，画 $f$–尺度曲线，取峰值对应的尺度为该特征的代表尺度。
## Slide 11

Slide from Tinne Tuytelaars
Lindeberg et al, 1996
Slide from Tinne Tuytelaars
Lindeberg et al., 1996

## Slide 12

（纯图片页，无文本层）

## Slide 13

（纯图片页，无文本层）

## Slide 14

（纯图片页，无文本层）

## Slide 15

（纯图片页，无文本层）

## Slide 16

（纯图片页，无文本层）

## Slide 17

（纯图片页，无文本层）

## Slide 18

（纯图片页，无文本层）

## Slide 19

Implementation
• Instead of computing f for larger and larger windows, we can
implement using a fixed window size with a Gaussian
pyramid
(sometimes need to create in-
between levels, e.g. a ¾-size image)

## Slide 20

Feature extraction: Corners and blobs

## Slide 21

Another common definition of f
• The Laplacian of Gaussian (LoG)
2
2
2
2
2
y
g
x
g
g







(very similar to a Difference of Gaussians (DoG) –
i.e. a Gaussian minus a slightly smaller Gaussian)

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

Laplacian of Gaussian（LoG，$f$ 的另一种常用定义；blob 检测）：

$$\nabla^2 g = \frac{\partial^2 g}{\partial x^2} + \frac{\partial^2 g}{\partial y^2}$$

LoG ≈ DoG（Difference of Gaussians，大高斯减小高斯），DoG 计算更快（SIFT 采用）。
## Slide 22

Laplacian of Gaussian
• “Blob” detector
• Find maxima and minima of LoG operator in
space and scale
*
=
maximum
minima

## Slide 23

Scale selection
• At what scale does the Laplacian achieve a maximum
response for a binary circle of radius r?
r
image
Laplacian

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

尺度选择：半径 $r$ 的圆形 blob，LoG 响应在与 $r$ 成比例的尺度上达到峰值（峰值尺度 $\sigma \propto r$，标准结果 $\sigma = r/\sqrt{2}$）。该峰值尺度即特征尺度（characteristic scale）。
## Slide 24

Characteristic scale
• We define the characteristic scale as the scale that produces
peak of Laplacian response
characteristic scale
T. Lindeberg (1998). "Feature detection with automatic scale selection."
International Journal of Computer Vision 30 (2): pp 77--116.

## Slide 25

Find local maxima in 3D position-scale space
K. Grauman, B. Leibe
)
(
)
(


yy
xx
L
L


2
3
4
5
 List of
(x, y, s)

## Slide 26

Scale-space blob detector: Example

## Slide 27

Scale-space blob detector: Example

## Slide 28

Scale-space blob detector: Example

## Slide 29

covariant
Note: The LoG and DoG operators
are both rotation equivariant
Scale Invariant Detection

## Slide 30

Questions?

## Slide 31

Feature descriptors
We know how to detect good points
Next question: How to match them?
Answer: Come up with a descriptor for each point, find
similar descriptors between the two images
?
