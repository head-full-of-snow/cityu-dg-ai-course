# CS5187: Vision and Image

Binocular Stereo

What is this?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2Faecd13266e2d4132bab64524a6edf5cc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256883&Signature=WWTmsl0UhuE%2BM0gkz8Yv4jpeZs0%3D)

Single image stereogram,

https://en.wikipedia.org/wiki/Autostereogram

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2Fe0099907dddc4f94a4a46936449ec9f1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256883&Signature=oTsBnouESPNBQuvo9bep%2FqhJXJ0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2F918f3cf79be54d05961086ca6a710e4e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256883&Signature=P4Ap2ZV%2FHliDN0l5nFSVD9T6Xpk%3D)

https://giphy.com/gifs/wigglegram-706pNfSKyaDug

# Stereo Vision as Localizing Points in 3D

• An object point will project to some point in our image

• That image point corresponds to a ray in the world

• Two rays intersect at a single point, so if we want to localize points in 3D we need 2 eyes

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2F150e03ef314e4c43824987ac897a2f5e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256884&Signature=tHL8s5PsArPR6R0QX3ROBnc%2FOqg%3D)

# Stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2F0e3fa980da8d4abfb15104b4fb6b9770.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256884&Signature=DvuAb%2FkYi2JzzXjD1hqVLT8OXkc%3D)

• Given two images from different viewpoints

– How can we compute the depth of each point in the image?

– Based on how much each pixel moves between the two images

# Epipolar geometry

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2Fb7def55be4e84f69bdfb84db3d6220aa.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256884&Signature=rPSnItq76YTxh%2FXId0tZqFbjHr0%3D)

Two images captured by a purely horizontal translating camera (rectified stereo pair)

$ x_{2}-x_{1}=\text{the disparity of pixel }(x_{1},y_{1}) $

# Disparity = inverse depth

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2F2b63089298574954a0da255dbadc3bda.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256884&Signature=dASiTJGw143nKnYKvMW3097NU2Y%3D)

http://stereo.nypl.org/view/41729

(Or, hold a finger in front of your face and wink each eye in succession.)

# Your basic stereo matching algorithm

# • Match Pixels in Conjugate Epipolar Lines

— Assume brightness constancy

– This is a challenging problem

— Hundreds of approaches

• A good survey and evaluation: http://www.middlebury.edu/stereo/
# Your basic stereo matching algorithm

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F63995c4e872040d386e4f43051fe5bd3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256914&Signature=YGVBhgSgiTJWSs99iu9Gm1yjpH0%3D)

For each epipolar line

For each pixel in the left image

compare with every pixel on same epipolar line in right image

- pick pixel with minimum match cost

Improvement: match windows

# Stereo matching based on SSD

Leit

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F318c122a031c4278b02da07dd8a5bdb6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256914&Signature=tSPmPGTBtN1BZ7PBZ%2Fbg4HDSLs8%3D)

Right

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F5d3dff02053f4473a50c2f7ceefc1c79.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256914&Signature=qMyUquAutXIkDltnf5GTNzmDG4Q%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2Fbf6c18b0bd20479b9169955f6ad81874.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256914&Signature=ntAoQnN64IxfRt8wSpQe24Yfm3g%3D)

Best matching disparity

# Window size

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F73876f7dab5940269ca60e66f5bec34e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256914&Signature=kkg%2BSSWmO5jDRwVmsE3Ja5LMvcY%3D)

– Smaller window

+ more detail

- more noise

– Larger window

+ less noise

- less detail

# Effect of window size

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F1637772786004eef82243fecc00dbb20.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256914&Signature=6O4KrS%2BfvwMr6ByAhcSeSgc%2FnDg%3D)

$ W = 3 $

$ W = 20 $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2Fff2b251f62ea4254bbd0026afec7c289.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256915&Signature=0yB%2BSQwAHE6BnuDIsUyae4KEOK8%3D)

# Better results with adaptive window

T. Kanade and M. Okutomi, A Stereo Matching Algorithm with an Adaptive Window: Theory and Experiment, ICRA 1991.

D. Scharstein and R. Szeliski. Stereo matching with nonlinear diffusion. IJCV, July 1998

# Stereo results

– Data from University of Tsukuba

– Similar results on other images without ground truth

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2Fcdc96f70457643629c80c09cf0a3368e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256915&Signature=y%2FgFgzzRM3JrhhuAAv3UnxSmEeM%3D)

Scene

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F3877087e31dc40438873f2221efd214a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256915&Signature=%2FsV4ouiEL7JU04aiKH8DouAU1bk%3D)

Ground truth

# Results with window search

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F1d91563991ef445eb9ca49a813d09e3a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256915&Signature=triDDSSoyFf1RY3ikjzJfR7VAJU%3D)

Window-based matching (best window size)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F6ff64c54515e441a989d77756c4f79cf.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256915&Signature=qziqqH9UgFOB4P6KVtHQIwMO214%3D)

Ground truth

# Better methods exist

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F86963a6ee47b4462bf37fdd3d31ceb6a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256915&Signature=9fQMGour2ygbtRqp7U6FmQNPlRY%3D)

Graph cuts-based method

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F88ff7de54c374921b4129c624a30cd92.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256915&Signature=OEXDj%2BCixih66iEXLh28sxuZJYA%3D)

Boykov et al.,  $ \underline{\text{Fast Approximate Energy Minimization via Graph Cuts,}} $ International Conference on Computer Vision 1999.

Ground truth

For the latest and greatest: http://www.middlebury.edu/stereo/

# Stereo as energy minimization

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9efa0ea77c9c4828938a94e9cd7ab6b7%2Fmedia%2F8258ba962c334e4dacee8b4d595ecab2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256915&Signature=EMdEmMUEhz3flIhRZjcSV6G%2FhAs%3D)

• What defines a good stereo correspondence?

1. Match quality

- Want each pixel to find a good match in the other image

2. Smoothness

• If two pixels are adjacent, they should (usually) move about the same amount

# Stereo as energy minimization

• Find disparity map $d$ that minimizes an energy function

$$ E(d) $$

• Simple pixel / window matching

$$ E(d)=\sum_{(x,y)\in I}C(x,y,d(x,y)) $$

$$ C(x,y,d(x,y))=\begin{array}{l}SSD distance between windows\\I(x,y)and J(x+d(x,y),y)\end{array} $$
# Stereo as energy minimization

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2F0bf673d1eb89448ca5c7c9f7bb58a7d8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=B1LcJ8nn0a0YR6hhDL2kWLOPrA8%3D)

$ C(x, y, d) $; the disparity space image (DSI)

# Stereo as energy minimization

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2Ffe44726022ea4612bee73155643f00df.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=E3IWejIk1tCGpLZeLkEzp33HnwY%3D)

Simple pixel / window matching: choose the minimum of each column in the DSI independently:

$$ d(x,y)=\arg\min C(x,y,d^{\prime}) $$

# Greedy selection of best match

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2F58b4c35b23014e209632c0987c9cddc2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=T65XjzYzymd7boxQDyfKeeORskA%3D)

# Stereo as energy minimization

• Better objective function

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2F6dad668f8b3c4c08afa3ac490598405c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=npDAcpXOwpG3YZ77qvXho0nbt78%3D)

# Stereo as energy minimization

$$ E(d)=E_{d}(d)+\lambda E_{s}(d) $$

match cost:

$$ E_{d}(d)=\sum_{(x,y)\in I}C(x,y,d(x,y)) $$

smoothness cost:

$$ E_{s}(d)=\sum_{(p,q)\in\mathcal{E}}V(d_{p},d_{q}) $$

E : set of neighboring pixels

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2Fd3e63036f3f34712bf2045fc4e8433ac.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=f%2F%2FY6YNfDSW6VOsfLdnAFDXw5jY%3D)

Smoothness cost

$$ \begin{array}{r l r}&{}&{E_{s}(d)=\displaystyle\sum_{V(d_{p},d_{q})}}\\ &{}&{(p,q)\in\mathcal{E}}\\ &{}&{\mathrm{H o w~d o~w e~c h o o s e~}V?}\end{array} $$

$$ V(d_{p},d_{q})=|d_{p}-d_{q}| \quad \text{L}_{1}\text{distance} $$

$$ V(d_{p},d_{q})=\begin{cases}0&if d_{p}=d_{q}\\1&if d_{p}\neq d_{q}\end{cases} $$

# Smoothness cost

$$ E(d)=E_{d}(d)+\lambda E_{s}(d) $$

• If  $ \lambda = \infty $ is infinity, then we only consider smoothness

• Optimal solution is a surface of constant depth/disparity

– Fronto-parallel surface

• In practice, want to balance data term with smoothness term

# Depth from disparity

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2Fea244e9ea8924be491f1cea3056520f2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=r5HC4gZD4wFPGEuHfcqsXWXeUZo%3D)

$$ disparity=x-x^{\prime}=\frac{baseline*f}{z} $$
# Stereo reconstruction pipeline

# • Steps

— Calibrate cameras

— Rectify images

— Compute disparity

— Estimate depth

# What will cause errors?

• Camera calibration errors

• Poor image resolution

• Occlusions

• Violations of brightness constancy (specular reflections)

• Large motions

# Low-contrast image regions

# V ariants of stereo

# Real-time stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F34cc332de41748f6a435c99399ac177d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=kmoy76MZ6kPITgg4qBqDgC%2FAk8A%3D)

Nomad robot searches for meteorites in Antartica

• Used for robot navigation (and other tasks)

– Several real-time stereo techniques have been developed (most based on simple discrete search)

# Active stereo with structured light

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F0965f464d3f34077967d367af6d3b49e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=DxrR1ELZ0jbUGCMNIHvdD5tfhAU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Fc62f5398208a49c2b5ace425bcdd5fba.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=em92mxT7Pj5tivWqLD%2BJATz9D28%3D)

Li Zhang's one-shot stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Fda7878bd84a54b08a982728883c89140.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=ymFCIeJBTQ8DbX%2F6zPtVXFnNLVU%3D)

projector

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F8300bda86b2d47dda02d5908e52b1b1a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=Fa%2FT97aWJKSfrUxxTU9j8DpWP0I%3D)

projector

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F5b469ee085e54022b371210a3d511af3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=P48a57Y1IhcsOSuJXgfwA%2F74ptU%3D)

• Project "structured" light patterns onto the object

– simplifies the correspondence problem

– basis for active depth sensors, such as Kinect and iPhone X (using IR)

# Active stereo with structured light

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F9aabc093ed804c318615a6e0b13af75f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=UiC7impiir%2BVupQDs%2BzTz4Q0%2BxQ%3D)

https://ios.gadgethacks.com/news/watch-iphone-xs-30k-ir-dots-scan-your-face-0180944/

# Laser scanning

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Fb21c30ab12b44b269186c97e1183e088.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=aFDYDFyyj%2FNGApRRSY%2FWa6jUhqk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Ffc597e45bc60426ba6051460be7baaeb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=RQmDpJDx0N2dG77TjPHoz0h0kI0%3D)

Digital Michelangelo Project

http://graphics.stanford.edu/projects/mich/

• Optical triangulation

– Project a single stripe of laser light

– Scan it across the surface of the object

— This is a very precise version of structured light scanning

# Laser scanned models

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Fd4f975471665429293686eac7c1184ec.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256979&Signature=qvLpRmwEgVHngZivQiuOu1g7Lik%3D)

The Digital Michelangelo Project, Levoy et al.

# Laser scanned models

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F2ba0fea4246f4b20bb8ffe77dad44d5d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256979&Signature=thilrcyv17qsNe9HRE7VQ1%2BdzAA%3D)

The Digital Michelangelo Project, Levoy et al.
# Laser scanned models

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd3726f8d96394d3c93ab61bdbfa5e846%2Fmedia%2F118db9d474c14800bf7f0c7860dc3b44.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257004&Signature=bJXYUkTFZ7r%2B5OoS96wZIx%2BJy%2Bo%3D)

The Digital Michelangelo Project, Levoy et al.

# Laser scanned models

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd3726f8d96394d3c93ab61bdbfa5e846%2Fmedia%2F39919191805a461b9ee1aac737736e1a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257004&Signature=73%2B6hJB0zeX%2BrCj4GMiva44jHR4%3D)

The Digital Michelangelo Project, Levoy et al.

# 3 D Photography on your Desk

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd3726f8d96394d3c93ab61bdbfa5e846%2Fmedia%2Fd7872e5808234d0e9b4626968f3d3099.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257004&Signature=Y3Fdn%2Flcbi0L5fM6%2BRBtStDRq4c%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd3726f8d96394d3c93ab61bdbfa5e846%2Fmedia%2F93963f8507044f49944173ba401e8875.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257004&Signature=Xhw7gs2hBToIbuoDaWC9gZ813bM%3D)

http://www.vision.caltech.edu/bouguetj/ICCV98/

**Time-of-flight cameras**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd3726f8d96394d3c93ab61bdbfa5e846%2Fmedia%2Fe5b26f3451e64005935becc9920f029f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257004&Signature=lqVL023MNv4ZomLJYovL3LaoGEI%3D)

$$ d=\frac{c t}{2} $$

Questions?
