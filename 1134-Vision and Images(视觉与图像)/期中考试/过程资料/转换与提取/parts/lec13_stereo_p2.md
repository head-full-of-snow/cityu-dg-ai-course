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
