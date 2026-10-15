# lec14_mvs

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

CS5187: Vision and Image
Multi-view stereo
Multi-Camera Array

## Slide 2

Before: Binocular (Two-View) Stereo
Left-right (rectified) stereo pair
Computed disparity map
Useful for robot perception and navigation, video effects, etc.

## Slide 3

Now: Multi-view Stereo
Binocular Stereo
Multi-view stereo
Problem formulation: given several images of the same
object or scene, compute a representation of its 3D
shape

## Slide 4

Multi-view Stereo
Point Grey’s Bumblebee XB3
Point Grey’s ProFusion 25
CMU’s Panoptic Studio

## Slide 5

Multi-view Stereo
Figures by Carlos Hernandez
Input: calibrated images from several viewpoints (known
intrinsics and extrinsics /
projection matrices)
Output: 3D object model
We’ll talk more about
how to calibrate
multiple cameras soon

## Slide 6

Applications

## Slide 7

（纯图片页，无文本层）

## Slide 8

（纯图片页，无文本层）

## Slide 9

https://renderpeople.com/about-us/

## Slide 10

Application: Virtual Reality Video
Broxton, et al. Immersive Light Field Video with a
Layered Mesh Representation. SIGGRAPH 2020.
Anderson, et al. Jump: Virtual Reality Video.
SIGGRAPH Asia 2016.

## Slide 11

Multi-view stereo: Basic
idea
reference view
neighbor views
Source: Y.
Furukawa

## Slide 12

reference view
neighbor views
Source: Y.
Furukawa
Multi-view stereo: Basic
idea

## Slide 13

Multi-view stereo: Basic
idea
reference view
neighbor views
Source: Y.
Furukawa

## Slide 14

reference view
neighbor views
Source: Y.
Furukawa
In this manner, solve for a depth map
over the whole reference view
Multi-view stereo: Basic
idea

## Slide 15

Multi-view stereo: advantages
• Can match windows using more than 1 neighbor, giving a
stronger match signal
• If you have lots of potential neighbors, can choose the best
subset of neighbors to match per reference image
• Can reconstruct a depth map for each reference frame, and
the merge into a complete 3D model

## Slide 16

width of
a pixel
Choosing a single stereo baseline
Large Baseline
Small Baseline
What’s the optimal baseline?
– Too small: large depth error
– Too large: difficult search problem
all of these
points project
to the same
pair of pixels

## Slide 17

The Effect of Baseline on Depth Estimation
I1
I2
I10

## Slide 18

z
pixel matching score
width of
a pixel
width of
a pixel
z
•
For larger baselines, must search larger area
in second image
M. Okutomi and T.Kanade, “A Multiple-Baseline Stereo System,” IEEE Trans. on Pattern
Analysis and Machine Intelligence, 15(4):353-363 (1993).
•
For short baselines, estimated depth will be less
precise due to narrow triangulation
Multiple-baseline stereo – all
cameras in a row

## Slide 19

（纯图片页，无文本层）

## Slide 20

I1
I2
I10
Multiple-baseline stereo results
M. Okutomi and T
.
Kanade, A Multiple-Baseline Stereo System, IEEE Trans. on Pattern
Analysis and Machine Intelligence, 15(4):353-363 (1993).

## Slide 21

Multibaseline Stereo
Basic Approach
– Choose a reference view
– Use your favorite stereo algorithm BUT
• replace two-view SSD with SSSD over all baselines
• SSSD: the SSD values are computed first for each pair of stereo images,
and then add all together from multiple stereo pairs.
Limitations
– Only gives a depth map (not an “object model”)
– Won’t work for widely distributed views.

## Slide 22

Some Solutions
•
Match only nearby photos [Narayanan 98]
•
Use NCC instead of SSD,
Ignore NCC values > threshold [Hernandez &
Schmitt 03]
Problem: visibility

## Slide 23

Popular matching scores
• SSD (Sum of Squared Differences)
• SAD (Sum of Absolute Differences)
• ZNCC (Zero-mean Normalized Cross Correlation)
– where
– what advantages might NCC have?

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

常用匹配代价（$W$ 为窗口）：

$$\mathrm{SSD} = \sum_{(i,j)} W(i,j)\big[I_1(i,j)-I_2(i,j)\big]^2, \qquad \mathrm{SAD} = \sum_{(i,j)} W(i,j)\big|I_1(i,j)-I_2(i,j)\big|$$

$$\mathrm{ZNCC} = \frac{\sum_{(i,j)} W(i,j)\big[(I_1-\overline{I_1})(I_2-\overline{I_2})\big]}{\sigma_{I_1}\,\sigma_{I_2}}$$

（NCC/ZNCC 对线性光照变化更鲁棒。）
## Slide 24

Questions?

## Slide 25

Plane-Sweep Stereo
Camera 1
R1,t1
Camera 2
R2,t2
Camera 3
R3,t3

## Slide 26

Plane-Sweep Stereo
Camera 1
R1,t1
Camera 2
R2,t2
Camera 3
R3,t3
Proposed point
at correct depth
Photo-consistent projections

## Slide 27

Plane-Sweep Stereo
Camera 1
R1,t1
Camera 2
R2,t2
Camera 3
R3,t3
Proposed point at
incorrect depth
Photo-inconsistent projections

## Slide 28

Plane-Sweep Stereo
• Sweep family of planes parallel to the reference camera
image plane
• Reproject neighbors onto each plane (via homography) and
compare reprojections
reference camera
neighbor camera 1
neighbor camera 2

## Slide 29

Plane-Sweep Stereo
Reference image
Right neighbor
Left neighbor
Left neighbor projected into
reference image
Right neighbor projected into
reference image
Average images on each plane

## Slide 30

Reference image
Right neighbor
Left neighbor
Planar image reprojections swept
over depth (averaged)
Another example

## Slide 31

Reference image
depth
Single pixel’s
cost profile
cost
Plane sweep
Full cost volume
Depth map
solver
(Belief propagation,
graph cuts, etc.)
Cost Volumes ->
Depth Maps

## Slide 32

Fusing multiple depth maps
• Compute depth map per image
• Fuse the depth maps into a 3D model
Figures by Carlos Hernandez

## Slide 33

Another approach: NeRF
• Represent scenes as functions from (x, y, z) to RGB and alpha
(transparency), use volume rendering to render images
NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis, ECCV
2020
https://www.matthewtancik.com/nerf

## Slide 34

Questions?
