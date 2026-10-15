# lec07_transformations

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

Image transformations and image warping
CS5670: Computer Vision
Prof. Zhu Zhiyu

## Slide 2

Image alignment

## Slide 3

Image alignment
Why don’t these image line up exactly?

## Slide 4

What is the geometric relationship between
these two images?
?
Answer: Similarity transformation (translation, rotation, uniform scale)

## Slide 5

?
What is the geometric relationship between
these two images?

## Slide 6

Very important for creating mosaics!
First, we need to know what this transformation is.
Second, we need to figure out how to compute it using feature matches.
What is the geometric relationship between
these two images?

## Slide 7

Richard Szeliski
Image Stitching
7
Image Warping
• image filtering: change range of image
• g(x) = h(f(x))
• image warping: change domain of image
• g(x) = f(h(x))
f
x
h
g
x
f
x
h
g
x

## Slide 8

Richard Szeliski
Image Stitching
8
Image Warping
• image filtering: change range of image
• g(x) = h(f(x))
• image warping: change domain of image
• g(x) = f(h(x))
h
h
f
f
g
g

## Slide 9

Richard Szeliski
Image Stitching
9
Parametric (global) warping
• Examples of parametric warps:
translation
rotation
aspect

## Slide 10

Parametric (global) warping
• Transformation T is a coordinate-changing machine:
p’ = T(p)
• What does it mean that T is global?
– Is the same for any point p
– can be described by just a few numbers (parameters)
• Let’s consider linear xforms (can be represented by a 2x2 matrix):
T
p = (x,y)
p’ = (x’
,y’)

## Slide 11

Common linear transformations
• Uniform scaling by s:
(0,0)
(0,0)
What is the inverse?

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

均匀缩放：

$$S = \begin{bmatrix} s & 0 \\ 0 & s \end{bmatrix}, \qquad S^{-1} = \begin{bmatrix} 1/s & 0 \\ 0 & 1/s \end{bmatrix}$$
## Slide 12

Common linear transformations
• Rotation by angle θ (about the origin)
(0,0)
(0,0)
What is the inverse?
For rotations:
θ

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

绕原点旋转 $\theta$：

$$R = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}, \qquad R^{-1} = R^{\mathsf T} = R(-\theta)$$
## Slide 13

2x2 Matrices
• What types of transformations can be
represented with a 2x2 matrix?
2D mirror across Y axis?
2D mirror across line y = x?

## Slide 14

2x2 Matrices
• What types of transformations can be
represented with a 2x2 matrix?
2D mirror across Y axis?
2D mirror across line y = x?

## Slide 15

• What types of transformations can be
represented with a 2x2 matrix?
2D Translation?
2x2 Matrices

## Slide 16

Can a 2D translation by (tx,ty) be represented with a 2x2
matrix transformation?
ⓘ Start presenting to display the poll results on this slide.

## Slide 17

• What types of transformations can be
represented with a 2x2 matrix?
2D Translation?
Translation is not a linear operation on 2D coordinates
NO!
2x2 Matrices

## Slide 18

All 2D Linear Transformations
• Linear transformations are combinations of …
– Scale,
– Rotation,
– Shear, and
– Mirror
• Properties of linear transformations:
– Origin maps to origin
– Lines map to lines
– Parallel lines remain parallel
– Ratios are preserved
– Closed under composition



















y
x
d
c
b
a
y
x
'
'































y
x
l
k
j
i
h
g
f
e
d
c
b
a
y
x
'
'

## Slide 19

Homogeneous coordinates
Trick:  add one more coordinate:
homogeneous image
coordinates
Converting from homogeneous coordinates
x
y
w
(x, y, w)
w = 1
(x/w, y/w, 1)
homogeneous plane

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

齐次坐标：

$$\begin{bmatrix}x \\ y\end{bmatrix} \Rightarrow \begin{bmatrix}x \\ y \\ 1\end{bmatrix}, \qquad \begin{bmatrix}x \\ y \\ w\end{bmatrix} \Leftrightarrow \left(x/w,\ y/w\right)$$
## Slide 20

Translation
• Solution: homogeneous coordinates to the rescue

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

平移（齐次坐标实现）：

$$T = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix}, \qquad T\begin{bmatrix}x \\ y \\ 1\end{bmatrix} = \begin{bmatrix}x+t_x \\ y+t_y \\ 1\end{bmatrix}$$
## Slide 21

Affine transformations
any transformation
represented by a 3x3 matrix
with last row [ 0 0 1 ] we call
an affine transformation

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

仿射变换 = 末行 $[0\ 0\ 1]$ 的任意 3×3 矩阵：

$$\begin{bmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{bmatrix}$$
## Slide 22

Basic affine transformations
































1
1
0
0
0
cos
sin
0
sin
cos
1
'
'
y
x
y
x



































1
1
0
0
1
0
0
1
1
'
'
y
x
t
t
y
x
y
x































1
1
0
0
0
1
0
1
1
'
'
y
x
sh
sh
y
x
y
x
Translate
2D in-plane rotation
Shear































1
1
0
0
0
0
0
0
1
'
'
y
x
s
s
y
x
y
x
Scale

## Slide 23

• Affine transformations are combinations of …
– Linear transformations, and
– Translations
• Properties of affine transformations:
– Origin does not necessarily map to origin
– Lines map to lines
– Parallel lines remain parallel
– Ratios are preserved
– Closed under composition

























w
y
x
f
e
d
c
b
a
w
y
x
1
0
0
'
'
Affine transformations

## Slide 24

Is this an affine transformation?

## Slide 25

Where do we go from here?
affine transformation
what happens when we
mess with this row?

## Slide 26

Projective Transformations aka Homographies aka
Planar Perspective Maps
Called a homography
(or planar perspective map)

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

投影变换 / 单应（Homography）：放开末行限制（$g,h \ne 0$，平行线可相交）：

$$H = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & 1 \end{bmatrix}$$
## Slide 27

Homographies
What happens when the
denominator is 0?

## Slide 28

Homographies
What happens when the
denominator is 0?

## Slide 29

Points at infinity

## Slide 30

Image warping with homographies
image plane in front
image plane below
black area
where no pixel
maps to

## Slide 31

Homographies

## Slide 32

Homographies
• Homographies …
– Affine transformations, and
– Projective warps
• Properties of projective transformations:
– Origin does not necessarily map to origin
– Lines map to lines
– Parallel lines do not necessarily remain parallel
– Ratios are not preserved
– Closed under composition
• Key fact: homographies are only defined up to a scale factor (e.g., H and 2H
are equivalent homographies)

## Slide 33

Alternate formulation for homographies
where the length of the vector [h00 h01 … h22] is 1

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

单应的另一种参数化（单位范数约束）：

$$\begin{bmatrix}x_i' \\ y_i' \\ 1\end{bmatrix} \cong \begin{bmatrix} h_{00} & h_{01} & h_{02} \\ h_{10} & h_{11} & h_{12} \\ h_{20} & h_{21} & h_{22} \end{bmatrix}\begin{bmatrix}x_i \\ y_i \\ 1\end{bmatrix}, \qquad \|[h_{00},\dots,h_{22}]\| = 1$$

（$\cong$ 表示差一个尺度因子；每对点提供 2 个方程，**8 个自由度需 4 对点**。）
## Slide 34

2D image transformations
These transformations are a nested set of groups
• Closed under composition and inverse is a member

## Slide 35

Implementing image warping
• Given a coordinate xform (x’,y’) = T(x,y) and a source image f(x,y),
how do we compute a transformed image g(x’,y’) = f(T(x,y))?
f(x,y)
g(x’
,y’)
x
x’
T(x,y)
y
y’

## Slide 36

Forward Warping
• Send each pixel (x,y) to its corresponding location (x’,y’) =
T(x,y) in g(x’,y’)
x
x’
T(x,y)
• What if pixel lands “between” two pixels?
y
y’
f(x,y)
g(x’
,y’)

## Slide 37

Forward Warping
• Send each pixel (x,y) to its corresponding location (x’,y’) =
T(x,y) in g(x’,y’)
x
x’
T(x,y)
• What if pixel lands “between” two pixels?
• Answer: add “contribution” to several pixels,
normalize later (splatting)
• Can still result in holes
y
y’
f(x,y)
g(x’
,y’)

## Slide 38

Inverse Warping
• Get each pixel g(x’
,y’) from its corresponding location (x,y) =
T-1(x,y) in f(x,y)
x
x’
T-1(x,y)
• Requires taking the inverse of the transform
• What if pixel comes from “between” two pixels?
y
y’
f(x,y)
g(x’
,y’)

## Slide 39

Inverse Warping
• Get each pixel g(x’
,y’) from its corresponding location (x,y) =
T-1(x’
,y’) in f(x,y)
• What if pixel comes from “between” two pixels?
• Answer: resample color value from interpolated
(prefiltered) source image
x
x’
y
y’
f(x,y)
g(x’
,y’)
T-1(x,y)

## Slide 40

Interpolation
• Possible interpolation filters:
– nearest neighbor
– bilinear
– bicubic
– sinc
• Needed to prevent “jaggies”
and “texture crawl”
(with prefiltering)

## Slide 41

Questions?
