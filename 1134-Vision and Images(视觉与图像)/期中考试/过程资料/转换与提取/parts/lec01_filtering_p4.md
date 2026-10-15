# Linear filters: examples

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Fbd52216472d34ad89b88d30975456736.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255643&Signature=ec69zh18yohFYt3%2FXGAdrXR3AiQ%3D)

Original

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F8177c2f31e94458bb6924924d0336d3d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255643&Signature=S0S4LXlB%2FZcgE9Cr2WnJL1O1iFg%3D)

Blur (with a mean filter)

# Linear filters: examples

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F3aff3c8993b54d7589579eec5fe51aaf.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255643&Signature=xDkUAtwvqyr4avoQdAk1A%2BS1t9E%3D)

Original

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F3f47cee0be794ea0b75890c5669651cb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255643&Signature=Pp0ww430CBNYkYn4TGyoC7rwxVA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F378c9dda30b04182874140fadef44631.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255643&Signature=Rt8igRgJmREXg7cdY%2By7tW4samc%3D)

Sharpening filter (accentuates edges)

# Sharpening

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F34a9a0f20328450f8dc28ae18ce99bb3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255643&Signature=cTwl1uCi8dfFLfMzyyOEaE88NiQ%3D)

before

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F44486149cacc41e5b4b7966bb50d7929.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255643&Signature=I6RBq95UWBmL776pEXXzLImwObM%3D)

after

# Smoothing with box filter revisited

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Fb5597fda58c04f1b9c0e67f8e9721d74.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255643&Signature=69tYwlwbLfMue31ESFvRJlA7cS0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Ff2e843fd9677470191f9840a9d35e965.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=rnR39aF5QAW882Hf3Ezem9MbPMU%3D)

# Gaussian kernel

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Ff94bf5b74458468b921f4752e53f2afe.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=B3REBsfUIyeVFEBhXO4IbvUWfmI%3D)

$$ G_{\sigma}=\frac{1}{2\pi\sigma^{2}}e^{-\frac{(x^{2}+y^{2})}{2\sigma^{2}}} $$

# Gaussian filters

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F23882a516eb34c838765900b046a807f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=lLWgYRzMhagCATCDCz9LqRs2j2c%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F38c6aa22b53e422d9718899e82442407.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=RlFzdvD2ao76Av%2BhkNhy5Q%2FjTWw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F1ae4aab67fbb4056bad328b5dfb759dc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=rgXRui8yW7M5Ua2e1ST71KFPMJk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Ff8513b551f494df886461a2b57fd7e85.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=ayCvmcec9dEVJ3DwvcCxnmY45Bk%3D)

$ \sigma = 1 \text{ pixel} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Fc9fcf24948224ce190ca9dc3f92679ed.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=U9nr3K8TnBIg3WYFmfoFekTp2xo%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F25b37c70bd324727964d4f85f2651d2b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=kj8hw4xfzLY8728CsWi%2BT4EPHpE%3D)

$ \sigma = 5 $ pixels

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F62f39a53bb6b4295a058c8e279ef0996.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255644&Signature=X3HI8BuvxguW25LQHs6KVW8fSTk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F126b955f00404a9d9e61054ed2c3c852.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255645&Signature=eDfUXeDMeTfxmIvGVBz5dzdwD%2Bk%3D)

$ \sigma = 10 \text{ pixels} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Fc262ac06ad9c45eabf08b1fe6aafb5e2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255645&Signature=%2BLUC6gsaW%2Fwodazj%2FtNUU4C9H0M%3D)

$ \sigma = 30 \text{ pixels} $

## Mean vs. Gaussian filtering

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2F6f0bea59eee9414e8a54ac14694859f7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255645&Signature=breZMXSndVKFrz93BJve9B6wV68%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Fc2d82cc779204f57bbaf6de50150e224.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255645&Signature=nfq9PjzqtTao1liS6uQo3pytMxE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Fd62bfaa2170649a286c5fcaed1d75291.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255645&Signature=yb5rAm8PVPMjCv0T9Ll47VYOkMQ%3D)

# Gaussian filter

• Removes "high-frequency" components from the image (low-pass filter)

• Convolution with self is another Gaussian

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F33f19873b470429ebe258fcaef143953%2Fmedia%2Fbb69c56916e24a9eaaa79eaefcb46cf9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255645&Signature=yqTT%2BsYmbRRwsZEjm4LR57fcg4Q%3D)

– Convolving twice with Gaussian kernel of width $\sigma$

= convolving once with kernel of width $\sigma\sqrt{2}$
