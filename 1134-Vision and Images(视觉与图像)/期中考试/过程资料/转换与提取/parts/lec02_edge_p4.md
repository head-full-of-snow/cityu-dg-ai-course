# Thresholding edges

• Still some noise

• Only want strong edges

• 2 thresholds, 3 cases

• R > T: strong edge

• R < T but R > t: weak edge

• R < t: no edge

• Why two thresholds?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2Faf9b607a181648d085ebaebfd1d29536.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255773&Signature=t7Awlzidf6zTjMPGOMPlUaXpKKQ%3D)

# Connecting edges

• Strong edges are edges!

• Weak edges are edges

iff they connect to strong

• Look in some neighborhood (usually 8 closest)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2Fbf697e9aba41467588a2b7050efa35b8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255773&Signature=EXdJ1N4GetBG1EZgzqD3%2FvTXruc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2Fa9adcacb2e4248ecbc928655b1c8c0ee.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255774&Signature=TF04FpvCMNIM1rOZaAbAYZm77Q8%3D)

MATLAB: edge (image, 'canny')

Canny edge

detector

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2F58328026189c450088ed2b975aabee88.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255774&Signature=k%2FQyxwb3p3JbfFMMTV%2FdsRWd7Bw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2F154642f1ea474ed7ad92dfa5b7bead44.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255774&Signature=hBObzcCH866CuDNsN5HqosbtDjg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2F9f144d1df58b41f28398be14aabc19e0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255774&Signature=FkCO09IavvY2NwESsTUsn%2F3R0Z8%3D)

1. Filter image with derivative of Gaussian

2. Find magnitude and orientation of gradient

3. Non-maximum suppression

4. Linking and thresholding (hysteresis):

- Define two thresholds: low and high

– Use the high threshold to start edge curves and the low threshold to continue them

# Canny edge detector

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2Ff5a24cb51eaf434ab635ddf97ff2e9a4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255774&Signature=NekujsUFyfwFY1RLnlT%2B3XggUTE%3D)

original

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2F4ea46fa8d0e74089b85247730ccb0446.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255774&Signature=dPKaO%2BsAT0%2BhxdFjM%2BbKnrFXRqk%3D)

Canny with  $ \sigma = 1 $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2Faf42a733f59d4ae3a364b9b2ca714cd2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255774&Signature=tFR4Vv%2FOjmBryvNRHlp7t5yUx%2Bs%3D)

Canny with  $ \sigma = 2 $

• The choice of  $ \sigma $ depends on desired behavior

– small  $ \sigma $ detects fine edges

– large  $ \sigma $ detects "large-scale" edges

# Scale space [Witkin 83]

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F84a2ae7eec1e4b03a0607a95cab92bd3%2Fmedia%2F54dad6998d614498a18e81ed9768f510.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255774&Signature=OvtN12coOySVtcOJ9motmRjk6k0%3D)

• Properties of scale space (w/ Gaussian smoothing)

– edge position may shift with increasing scale ( $ \sigma $)

— two edges may merge with increasing scale

— an edge may not split into two with increasing scale

# Questions?
