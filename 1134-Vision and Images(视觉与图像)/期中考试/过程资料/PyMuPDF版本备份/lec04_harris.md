# lec04_harris

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

Local features & Harris corner detection
CS5187: Vision & Image

## Slide 2

Today: Feature extraction—Corners and blobs

## Slide 3

Motivation: Automatic panoramas
Credit: Matt Brown

## Slide 4

Panorama stitching
Panorama captured by Perseverence Rover, Feb. 20, 2021
https://www.space.com/nasa-perseverance-rover-first-panorama-mars

## Slide 5

GigaPan:
http://gigapan.com/
Also see Google Zoom Views:
https://www.google.com/culturalinstitute/beta/project/gigapixels
Motivation: Automatic panoramas

## Slide 6

Why extract features?
• Motivation: panorama stitching
– We have two images – how do we combine them?

## Slide 7

Why extract features?
• Motivation: panorama stitching
– We have two images – how do we combine them?
Step 1: extract features
Step 2: match features

## Slide 8

Why extract features?
• Motivation: panorama stitching
– We have two images – how do we combine them?
Step 1: extract features
Step 2: match features
Step 3: align images

## Slide 9

Application: Visual SLAM
• (aka Simultaneous Localization and Mapping)

## Slide 10

Do these images overlap?

## Slide 11

NASA Mars Rover images
with SIFT feature matches
Answer below (look for tiny colored squares…)

## Slide 12

Feature matching for object search

## Slide 13

Feature matching

## Slide 14

Invariant local features
Find features that are invariant to transformations
– geometric invariance:  translation, rotation, scale
– photometric invariance:  brightness, exposure, …
Feature Descriptors

## Slide 15

Advantages of local features
Locality
– features are local, so robust to occlusion and clutter
Quantity
– hundreds or thousands in a single image
Distinctiveness:
– can differentiate a large database of objects
Efficiency
– real-time performance achievable

## Slide 16

More motivation…
Feature points are used for:
– Image alignment (e.g., mosaics)
– 3D reconstruction
– Motion tracking (e.g. for AR)
– Object recognition
– Image retrieval
– Robot/car navigation
– … other

## Slide 17

Approach
1. Feature detection: find it
2. Feature descriptor: represent it
3. Feature matching: match it
Feature tracking: track it, when motion

## Slide 18

Local features: main components
1) Detection: Identify the
interest points
2) Description: Extract vector
feature descriptor surrounding
each interest point
3) Matching: Determine
correspondence between
descriptors in two views
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
Credit: Kristen Grauman

## Slide 19

Snoop demo
What makes a good feature?

## Slide 20

Want uniqueness
Look for image regions that are unusual
– Lead to unambiguous matches in other images
How to define “unusual”?

## Slide 21

Local measures of uniqueness
Suppose we only consider a small window of pixels
– What defines whether a feature is a good or bad candidate?
Credit: S. Seitz, D. Frolova, D. Simakov

## Slide 22

Local measures of uniqueness
“flat” region:
no change in all
directions
“edge”:
no change along the
edge direction
“corner”:
significant change in
all directions
• How does the window change when you shift it?
• Shifting the window in any direction causes a big change
Credit: S. Seitz, D. Frolova, D. Simakov

## Slide 23

Consider shifting the window W by (u,v)
• how do the pixels in W change?
• compare each pixel before and after by
summing up the squared differences (SSD)
• this defines an SSD “error” E(u,v):
• We are pretty happy if this error is high for some offset (u, v)
• We are very happy if this error is high for all offsets (u,v)
• But, slow to compute exactly for each pixel and each offset (u,v)
Harris corner detection:  the math
W
(u,v)
Chris Harris and Mike Stephens (1988). "A Combined
Corner and Edge Detector". Alvey Vision Conference.

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

窗口 $W$ 平移 $(u,v)$ 的 SSD 误差：

$$E(u,v) = \sum_{(x,y)\in W}\big[I(x+u,\ y+v) - I(x,y)\big]^2$$

（$E$ 对所有偏移都大 → 角点。）
## Slide 24

Taylor Series expansion of I:
If the motion (u, v) is small, then first order approximation is good
Plugging this into the formula on the previous slide…
Small motion assumption

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

小运动假设下的泰勒一阶展开：

$$I(x+u,\ y+v) \approx I(x,y) + u\,I_x + v\,I_y, \qquad I_x = \tfrac{\partial I}{\partial x},\ I_y = \tfrac{\partial I}{\partial y}$$
## Slide 25

Corner detection:  the math
Consider shifting the window W by (u,v)
• define an SSD “error” E(u,v):
W
(u,v)

## Slide 26

Corner detection:  the math
Consider shifting the window W by (u,v)
• define an SSD “error” E(u,v):
• Thus, E(u,v) is locally approximated as a quadratic error function
W
(u,v)

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

代入得二次型近似：

$$E(u,v) \approx \sum_{(x,y)\in W}\big[u\,I_x + v\,I_y\big]^2 = \begin{bmatrix}u & v\end{bmatrix} H \begin{bmatrix}u \\ v\end{bmatrix} = Au^2 + 2Buv + Cv^2$$

二阶矩矩阵（结构张量）：

$$H = \sum_{(x,y)\in W}\begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix}, \qquad A=\sum I_x^2,\ B=\sum I_x I_y,\ C=\sum I_y^2$$
## Slide 27

The surface E(u,v) is locally approximated by a quadratic form.
The second moment matrix
Let’s try to understand its shape.

## Slide 28

Horizontal edge:
u
v
E(u,v)

## Slide 29

Vertical edge:
u
v
E(u,v)

## Slide 30

General case
We can visualize H as an ellipse with axis lengths
determined by the eigenvalues of H and orientation
determined by the eigenvectors of H
direction of the
slowest change
direction of the
fastest change
(max)-1/2
(min)-1/2
const
]
[







v
u
H
v
u
Ellipse equation:
max, min : eigenvalues of H

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

椭圆等值线方程：

$$\begin{bmatrix}u & v\end{bmatrix} H \begin{bmatrix}u \\ v\end{bmatrix} = \text{const}$$

轴长由特征值决定（半轴 $\propto 1/\sqrt{\lambda}$），方向由特征向量决定：$\lambda_{\max}$=最快变化方向的变化量，$\lambda_{\min}$=最慢方向的变化量。
## Slide 31

Quick eigenvalue/eigenvector review
The eigenvectors of a matrix A are the vectors x that satisfy:
The scalar  is the eigenvalue corresponding to x
– The eigenvalues are found by solving:
– In our case, A = H is a 2x2 matrix, so we have
– The solution:
Once you know , you find x by solving

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

特征值回顾（$H$ 为 2×2）：

$$\det(A-\lambda I) = 0 \;\Rightarrow\; \lambda^2 - (h_{11}+h_{22})\lambda + (h_{11}h_{22}-h_{12}^2) = 0$$

$$\lambda = \tfrac{1}{2}\Big[(h_{11}+h_{22}) \pm \sqrt{(h_{11}-h_{22})^2 + 4h_{12}^2}\Big]$$

求得 $\lambda$ 后解 $(A-\lambda I)x = 0$ 得特征向量。
## Slide 32

Corner detection:  the math
Eigenvalues and eigenvectors of H
•
Define shift directions with the smallest and largest change in error
•
xmax = direction of largest increase in E
•
max = amount of increase in direction xmax
•
xmin = direction of smallest increase in E
•
min = amount of increase in direction xmin
xmin
xmax

## Slide 33

Corner detection:  the math
How are max, xmax, min, and xmin relevant for feature detection?
•
What’s our feature scoring function?

## Slide 34

Corner detection:  the math
How are max, xmax, min, and xmin relevant for feature detection?
•
What’s our feature scoring function?
Want E(u,v) to be large for small shifts in all directions
•
the minimum of E(u,v) should be large, over all unit vectors [u v]
•
this minimum is given by the smaller eigenvalue (min) of H

## Slide 35

Interpreting the eigenvalues
1
2
“Corner”
1 and 2 are large,
1 ~ 2;
E increases in all
directions
1 and 2 are small;
E is almost constant
in all directions
“Edge”
1 >> 2
“Edge”
2 >> 1
“Flat”
region
Classification of image points using eigenvalues of M:

## Slide 36

Corner detection summary
Here’s what you do:
•
Compute the gradient at each point in the image
•
For each pixel:
•
Create the H matrix from nearby gradient values
•
Compute the eigenvalues.
•
Find points with large response (min > threshold)
•
Choose those points where min is a local maximum as features

## Slide 37

Corner detection summary
Here’s what you do:
•
Compute the gradient at each point in the image
•
For each pixel:
•
Create the H matrix from nearby gradient values
•
Compute the eigenvalues.
•
Find points with large response (min > threshold)
•
Choose those points where min is a local maximum as features

## Slide 38

The Harris operator
min is a variant of the “Harris operator” for feature detection
•
The trace is the sum of the diagonals, i.e., trace(H) = h11 + h22
•
Very similar to min but less expensive (no square root)
•
Called the Harris Corner Detector or Harris Operator
•
Lots of other detectors, this is one of the most popular

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

Harris 算子（本页定义，$\lambda_{\min}$ 的变体，无开方）：

$$f = \frac{\lambda_1 \lambda_2}{\lambda_1 + \lambda_2} = \frac{\det(H)}{\operatorname{trace}(H)}$$

（trace$(H)=h_{11}+h_{22}$。）
## Slide 39

Alternate Harris operator
• will use an alternate definition of the Harris operator:

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

**课程将采用的另一种 Harris 算子定义**（Tutorial 03 同款）：

$$R = \lambda_1\lambda_2 - k\,(\lambda_1+\lambda_2)^2 = \det(M) - k\cdot\operatorname{tr}(M)^2, \quad k \approx 0.04\text{~}0.06$$
## Slide 40

The Harris operator
Harris
operator

## Slide 41

Harris detector example

## Slide 42

f value (red high, blue low)

## Slide 43

Threshold (f > value)

## Slide 44

Find local maxima of f (non-max suppression)

## Slide 45

Harris features (in red)

## Slide 46

Weighting the derivatives
• In practice, using a simple window W doesn’t work too well
• Instead, we’ll weight each derivative value based on its
distance from the center pixel

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

实际用高斯窗加权（而非简单方块窗 $W$）：

$$H = \sum_{(x,y)\in W} w_{x,y}\begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix}, \qquad w_{x,y} = \text{高斯权重（按距中心距离衰减）}$$
## Slide 47

Harris Detector – Recap [Harris88]
Second moment matrix










)
(
)
(
)
(
)
(
)
(
)
,
(
2
2
D
y
D
y
x
D
y
x
D
x
I
D
I
I
I
I
I
I
I
g








47
1. Image
derivatives
2. Square of
derivatives
3. Gaussian
filter g(sI)
Ix
Iy
Ix2
Iy2
IxIy
g(Ix2)
g(Iy2)
g(IxIy)
4. Cornerness function – both eigenvalues are strong
har
5. Non-maxima suppression
1
2
1
2
det
trace
M
M






0. Input image

## Slide 48

Harris Corners – Why so complicated?
• Can’t we just check for regions with lots of gradients in the
x and y directions?
– No! A diagonal line would satisfy that criteria
Current
Window

## Slide 49

Questions?
