# lec06_descriptors_matching

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

Feature descriptors and feature matching
CS5670: Computer Vision
Prof. Zhu Zhiyu

## Slide 2

Local features: main components
1) Detection: Identify the
interest points
2) Description: Extract vector
feature descriptor
surrounding each interest
point.
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
Kristen Grauman

## Slide 3

The surface E(u,v) is locally approximated by a quadratic form.
Review of the last lecture
Let’s try to understand its shape.

## Slide 4

Review of the last lecture
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

## Slide 5

Feature descriptors
We know how to detect good points
Next question: How to match them?
Answer: Come up with a descriptor for each point, find
similar descriptors between the two images
?

## Slide 6

We know how to detect good points
Next question: How to match them?
Lots of possibilities
– Simple option:  match square windows around the point
– State of the art approach:  SIFT
•
David Lowe, UBC  http://www.cs.ubc.ca/~lowe/keypoints/
?
Feature descriptors

## Slide 7

Invariance vs. discriminability
• Invariance:
– Descriptor shouldn’t change even if image is transformed
• Discriminability:
– Descriptor should be highly unique for each point

## Slide 8

Image transformations revisited
• Geometric
Rotation
Scale
• Photometric
Intensity change

## Slide 9

Invariance
Suppose we are comparing two images I1 and I2
– I2 may be a transformed version of I1
– What kinds of transformations are we likely to encounter in practice?

## Slide 10

Invariant descriptors
• We looked at invariant / equivariant detectors
• Most feature descriptors are also designed to be invariant
to:
– Translation, 2D rotation, scale
• They can usually also handle
– Limited 3D rotations (SIFT works up to about 60 degrees)
– Limited affine transforms (some are fully affine invariant)
– Limited illumination/contrast changes

## Slide 11

How to achieve invariance
Need both of the following:
1. Make sure your detector is invariant
2.  Design an invariant feature descriptor
– Simplest descriptor: a single 0
• What’s this invariant to?
– Next simplest descriptor:  a square, axis-aligned 5x5 window of pixels
• What’s this invariant to?
– Let’s look at some better approaches…

## Slide 12

• Find dominant orientation of the image patch (this orientation
should be equivariant to image rotation)
– E.g., given by xmax, the eigenvector of the second moment matrix H
corresponding to max (the larger eigenvalue)
– Or (better) simply the orientation of the (smoothed) gradient
– Rotate the patch according to this angle
Rotation invariance for feature descriptors
Figure by Matthew Brown

## Slide 13

Take 40x40 square window around
detected feature
– Scale to 1/5 size (using
prefiltering)
– Rotate to horizontal
– Sample 8x8 square window
centered at feature
– Intensity normalize the window
by subtracting the mean,
dividing by the standard
deviation in the window (why?)
CSE 576: Computer Vision
Multiscale Oriented PatcheS descriptor
8 pixels
40 pixels
Adapted from slide by Matthew Brown

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

MOP（Multiscale Oriented Patches）参数：

- 特征点周围取 $40\times40$ 窗口 → 缩小到 $1/5$ → 旋转对齐 → 采样 $8\times8$ 窗口
- 强度归一化：窗口内减均值、除以标准差（光度不变性）
## Slide 14

Detections at multiple scales

## Slide 15

Basic idea:
•
Take 16x16 square window around detected feature
•
Compute edge orientation (angle of the gradient - 90) for each pixel
•
Throw out weak edges (threshold gradient magnitude)
•
Create histogram of surviving edge orientations
•
Shift the bins so that the biggest one is first
Scale Invariant Feature Transform
Adapted from slide by David Lowe
0
2
angle histogram

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

SIFT 基本思想（方向直方图）：

- $16\times16$ 窗口内每像素计算梯度方向 $\theta(x,y)$（幅值小者剔除）
- 关键点主方向：$36\text{ bins}\times10^\circ$ 的梯度方向直方图取峰值（旋转归一基准）
## Slide 16

SIFT descriptor
Full version
•
Divide the 16x16 window into a 4x4 grid of cells (2x2 case shown below)
•
Compute an orientation histogram for each cell
•
16 cells * 8 orientations = 128 dimensional descriptor
Adapted from slide by David Lowe

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

SIFT 完整版：

- $16\times16$ 窗口分成 $4\times4$ cell，每 cell 做 $8$ 方向直方图
- 描述子维度 $= 16\ \text{cells} \times 8\ \text{orientations} = 128$
## Slide 17

Properties of SIFT
Extraordinarily robust matching technique
– Can handle changes in viewpoint (up to about 60 degree out of plane rotation)
– Can handle significant changes in illumination (sometimes even day vs. night (below))
– Pretty fast—hard to make real-time, but can run in <1s for moderate image sizes
– Lots of code available

## Slide 18

SIFT Example
sift
868 SIFT features

## Slide 19

Other descriptors
• HOG: Histogram of Gradients (HOG)
– Dalal/Triggs
– Sliding window, pedestrian detection
• FREAK (Fast Retina Keypoint) or ORB features
– Can run in real-time; used in Visual SLAM on-device
• LIFT: Learned Invariant Feature Transform
– Learned via deep learning – along with many other recent features
https://arxiv.org/abs/1603.09114

## Slide 20

Other descriptors
• HOG: Histogram of Gradients (HOG)
– Dalal/Triggs
– Sliding window, pedestrian detection
1. Gradient Computation
- Compute horizontal and vertical gradients using [-1, 0, 1] filters
- Calculate gradient magnitude and orientation at each pixel
2. Cell Histograms
- Divide image into small cells (e.g., 8×8 pixels)
- Create histogram of gradient orientations (typically 9 bins, 0-
180°)
- Weight votes by gradient magnitude
3. Block Normalization
- Group cells into overlapping blocks (e.g., 2×2 cells)
- Normalize histograms within each block (L2-norm)
- Provides invariance to illumination changes

## Slide 21

Other descriptors
• FREAK (Fast Retina Keypoint) or ORB features
– Can run in real-time; used in Visual SLAM on-device
1. oFAST: Oriented FAST Keypoint Detection
- Uses FAST corner detector to find keypoints
- Computes intensity centroid to determine orientation
- Applies Harris corner measure to rank keypoints
2. rBRIEF: Rotated BRIEF Descriptor
- Binary descriptor: compares intensity of pixel pairs
- 256 bits (256 binary tests)
- Rotates sampling pattern according to keypoint orientation
- Uses learned sampling patterns for better performance

## Slide 22

Questions?

## Slide 23

Summary
• Keypoint detection: repeatable and
distinctive
– Corners, blobs
– Harris, DoG
• Descriptors: robust and selective
– spatial histograms of orientation
– SIFT and variants are typically good for
stitching and recognition
– But, need not stick to one

## Slide 24

Which features match?

## Slide 25

Feature matching
Given a feature in I1, how to find the best match in I2?
1. Define distance function that compares two descriptors
2. Test all the features in I2, find the one with min distance
(can be accelerated with a nearest neighbors search data
structure, like a kd-tree)

## Slide 26

Feature distance
How to define the difference between two features f1, f2?
–
Simple approach: L2 distance, || f1 - f2 ||
–
can give small distances for ambiguous (incorrect) matches
I1
I2
f1
f2

## Slide 27

f1
f2
f2'
Feature distance
How to define the difference between two features f1, f2?
•
Better approach:  ratio distance = || f1 - f2 || / || f1 - f2’ ||
•
f2 is the best SSD match to f1 in I2
•
f2’ is the 2nd best SSD match to f1 in I2
•
gives large values for ambiguous matches
I1
I2

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

比值距离（ratio distance）：

$$\text{ratio} = \frac{\|f_1 - f_2\|}{\|f_1 - f_2'\|}$$

（$f_2$ = 最近邻，$f_2'$ = 次近邻。）比值小 → 匹配置信度高；讲义阈值示例 $0.8$；Tutorial 04 代码用 $0.75$。
## Slide 28

• Does the SSD vs “ratio distance” change the best match to a
given feature in image 1?
• No, but it changes the distance, and it can change the
ordering of matches from good to bad
• After we compute a set of matches, we threshold by distance
(that is, throw out matches with distance > threshold)
Feature distance

## Slide 29

Feature matching example
58 matches (thresholded by ratio score)

## Slide 30

Feature matching example
51 matches (thresholded by ratio score)
We’ll deal with
outliers later

## Slide 31

Evaluating the results
How can we measure the performance of a feature matcher?
50
75
200
feature distance

## Slide 32

True/false positives
The distance threshold affects performance
– True positives = # of detected matches that survive the threshold that are correct
– False positives = # of detected matches that survive the threshold that are incorrect
50
75
200
false match
true match
feature distance
How can we measure the performance of a feature matcher?

## Slide 33

True/false positives
Suppose we want to maximize true positives. How do we set the threshold?
(Note: we keep all matches with distance below the threshold.)
50
75
200
false match
true match
feature distance
How can we measure the performance of a feature matcher?

## Slide 34

True/false positives
Suppose we want to minimize false positives. How do we set the threshold?
(Note: we keep all matches with distance below the threshold.)
50
75
200
false match
true match
feature distance
How can we measure the performance of a feature matcher?

## Slide 35

Example
• Suppose our matcher computes 1,000 matches between two
images
– 800 are correct matches, 200 are incorrect (according to an oracle
that gives us ground truth matches)
– A given threshold (e.g., ratio distance = 0.6) gives us 600 correct
matches and 100 incorrect matches that survive the threshold
– True positive rate = 600 / 800 = ¾
– False positive rate = 100 / 200 = ½

## Slide 36

0.7
Evaluating the results
0
1
1
false positive rate
true
positive
rate
0.1
How can we measure the performance of a feature matcher?
recall
1 - specificity
# true positives surviving threshold
# total correct matches (positives)
# false positives surviving threshold
# total incorrect matches (negatives)

## Slide 37

0.7
0
1
1
false positive rate
true
positive
rate
# true positives surviving threshold
# total correct matches (positives)
0.1
# false positives surviving threshold
# total incorrect matches (negatives)
ROC curve  (“Receiver Operator Characteristic”)
How can we measure the performance of a feature matcher?
recall
1 - specificity
Single number: Area Under
the Curve (AUC)
E.g. AUC = 0.87
1 is the best
Evaluating the results

## Slide 38

ROC curves – summary
• By thresholding the match distances at different thresholds,
we can generate sets of matches with different true/false
positive rates
• ROC curve is generated by computing rates at a set of
threshold values swept through the full range of possible
thresholds
• Area under the ROC curve (AUC) summarizes the
performance of a feature pipeline (higher AUC is better)

## Slide 39

Lots of applications
Features are used for:
– Image alignment (e.g., mosaics)
– 3D reconstruction
– Motion tracking
– Object recognition
– Indexing and database retrieval
– Robot navigation
– … other

## Slide 40

Object recognition (David Lowe)

## Slide 41

3D Reconstruction
Internet Photos (“Colosseum”)
Reconstructed 3D cameras and points

## Slide 42

WildGaussians: first reconstruct cameras using
feature matching, then create dense model
Kulhanek, et al. WildGaussians. NeurIPS 2024

## Slide 43

Augmented Reality

## Slide 44

Learned feature matchers
LoFTR: Detector-Free Local Feature Matching with Transformers
CVPR 2021 [Sun, Shen, Wang, et al.]

## Slide 45

Learned feature matchers
RoMa: Robust Dense Feature Matching, CVPR 2024

## Slide 46

Questions?
