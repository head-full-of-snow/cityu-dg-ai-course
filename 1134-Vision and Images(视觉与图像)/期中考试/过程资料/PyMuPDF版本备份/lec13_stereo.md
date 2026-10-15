# lec13_stereo

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

Binocular Stereo
CS5187: Vision and Image
Single image stereogram,
https://en.wikipedia.org/wiki/Autostereogram
What is this?

## Slide 2

“Mark Twain at Pool Table", no date, UCR Museum of Photography

## Slide 3

https://giphy.com/gifs/wigglegram-706pNfSKyaDug

## Slide 4

• An object point will project to
some point in our image
• That image point corresponds to
a ray in the world
• Two rays intersect at a single
point, so if we want to localize
points in 3D we need 2 eyes
Stereo Vision as
Localizing Points in 3D

## Slide 5

Stereo
• Given two images from different viewpoints
– How can we compute the depth of each point in the image?
– Based on how much each pixel moves between the two images

## Slide 6

epipolar
lines
Epipolar geometry
(x1, y1)
(x2, y1)
x2 - x1 = the disparity of pixel (x1, y1)
Two images captured by a purely horizontal translating camera
(rectified stereo pair)

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

校正立体对（纯水平平移相机）的视差定义：

$$x_2 - x_1 = \text{the disparity of pixel }(x_1, y_1)$$

（对应点在同一水平极线上搜索。）
## Slide 7

Disparity = inverse depth
http://stereo.nypl.org/view/41729
(Or, hold a finger in front of your face and wink each eye in succession.)

## Slide 8

Your basic stereo matching algorithm
• Match Pixels in Conjugate Epipolar Lines
– Assume brightness constancy
– This is a challenging problem
– Hundreds of approaches
• A good survey and evaluation:  http://www.middlebury.edu/stereo/

## Slide 9

Your basic stereo matching algorithm
For each epipolar line
For each pixel in the left image
•
compare with every pixel on same epipolar line in right image
•
pick pixel with minimum match cost
Improvement: match windows

## Slide 10

Stereo matching based on SSD
SSD
dmin
d
Best matching disparity

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

SSD 立体匹配：对每个候选视差 $d$ 计算窗口 SSD 代价曲线，取最小：

$$\hat{d} = \arg\min_{d}\ \mathrm{SSD}(d)$$
## Slide 11

Window size
– Smaller window
+  more detail
-   more noise
– Larger window
+  less noise
-    less detail
W = 3
W = 20
Better results with adaptive window
•
T. Kanade and M. Okutomi, A Stereo Matching Algorithm with an
Adaptive Window: Theory and Experiment, ICRA 1991.
•
D. Scharstein and R. Szeliski. Stereo matching with nonlinear diffusion.
IJCV, July 1998
Effect of window size

## Slide 12

Stereo results
– Data from University of Tsukuba
– Similar results on other images without ground truth
Ground truth
Scene

## Slide 13

Results with window search
Window-based matching
(best window size)
Ground truth

## Slide 14

Better methods exist...
Graph cuts-based method
Boykov et al., Fast Approximate Energy Minimization via Graph Cuts,
International Conference on Computer Vision 1999.
Ground truth
For the latest and greatest:  http://www.middlebury.edu/stereo/

## Slide 15

Stereo as energy minimization
• What defines a good stereo correspondence?
1. Match quality
•
Want each pixel to find a good match in the other image
2. Smoothness
•
If two pixels are adjacent, they should (usually) move about the same amount

## Slide 16

Stereo as energy minimization
• Find disparity map d that minimizes an energy function
• Simple pixel / window matching
SSD distance between windows
I(x, y) and J(x + d(x,y), y)
=

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

立体匹配 = 能量最小化。数据项形式：

$$E(d) = \sum_{(x,y)\in I} C\big(x,\ y,\ d(x,y)\big)$$

（$C$ = 左 $(x,y)$ 与右 $(x+d,\ y)$ 窗口间的 SSD/匹配代价；一般形式再加平滑项 $+\lambda\sum\rho(d(x,y)-d(x{+}1,y))$。）
## Slide 17

Stereo as energy minimization
y = 141
C(x, y, d); the disparity space image (DSI)
x
d

## Slide 18

Stereo as energy minimization
y = 141
x
d
Simple pixel / window matching: choose the minimum of each
column in the DSI independently:

## Slide 19

Greedy selection of best match

## Slide 20

Stereo as energy minimization
• Better objective function
{
{
match cost
smoothness cost
Want each pixel to find a good
match in the other image
Adjacent pixels should (usually)
move about the same amount

## Slide 21

Stereo as energy minimization
match cost:
smoothness cost:
4-connected
neighborhood
8-connected
neighborhood
: set of neighboring pixels

## Slide 22

Smoothness cost
“Potts model”
L1 distance
How do we choose V?

## Slide 23

Smoothness cost
• If λ = infinity, then we only consider smoothness
• Optimal solution is a surface of constant depth/disparity
– Fronto-parallel surface
• In practice, want to balance data term with smoothness term

## Slide 24

Depth from disparity
f
x
x’
baseline
z
C
C’
X
f

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

相似三角形得深度-视差关系：

$$\text{disparity} = x - x'' = \frac{B\,f}{z} \quad\Longrightarrow\quad z = \frac{f\,B}{\text{disparity}}$$

（$f$=焦距，$B$=基线。视差与深度成反比：越近视差越大。）
## Slide 25

•
Camera calibration errors
•
Poor image resolution
•
Occlusions
•
Violations of brightness constancy (specular reflections)
•
Large motions
•
Low-contrast image regions
Stereo reconstruction pipeline
• Steps
– Calibrate cameras
– Rectify images
– Compute disparity
– Estimate depth
What will cause errors?

## Slide 26

Variants of stereo

## Slide 27

Real-time stereo
• Used for robot navigation (and other tasks)
– Several real-time stereo techniques have been developed (most
based on simple discrete search)
Nomad robot searches for meteorites in Antartica

## Slide 28

Active stereo with structured light
• Project “structured” light patterns onto the object
– simplifies the correspondence problem
– basis for active depth sensors, such as Kinect and iPhone X (using IR)
camera 2
camera 1
projector
camera 1
projector
Li Zhang’s one-shot stereo

## Slide 29

Active stereo with structured light
https://ios.gadgethacks.com/news/watch-iphone-xs-30k-ir-dots-scan-your-face-0180944/

## Slide 30

Laser scanning
•
Optical triangulation
– Project a single stripe of laser light
– Scan it across the surface of the object
– This is a very precise version of structured light scanning
Digital Michelangelo Project
http://graphics.stanford.edu/projects/mich/

## Slide 31

Laser scanned models
The Digital Michelangelo Project, Levoy et al.

## Slide 32

Laser scanned models
The Digital Michelangelo Project, Levoy et al.

## Slide 33

Laser scanned models
The Digital Michelangelo Project, Levoy et al.

## Slide 34

Laser scanned models
The Digital Michelangelo Project, Levoy et al.

## Slide 35

3D Photography on your Desk
http://www.vision.caltech.edu/bouguetj/ICCV98/

## Slide 36

Time-of-flight cameras
https://en.wikipedia.org/wiki/Time-of-flight_camera

## Slide 37

Questions?
