# Sharpening revisited

• What does blurring take away?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F618aa5ff1c0f480798c4825f08220b15.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255674&Signature=HBH4tBBj6DlmejI0gjkGtxV8O3k%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F7859d9fd0578437f9a3a934b5e990422.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255674&Signature=qj93uSSQfmQG5%2FFGVeFTslpXwX0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F6f25e31a18584bf885a59bc8d6cfe223.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255674&Signature=GI%2Fi0o2r8kSMQppB4OxnzlW7K7E%3D)

Let's add it back:

(This "detail extraction" operation is also called a high-pass filter)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F8c42ac12e7e64e469392696187bd524d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255674&Signature=GFzHoUqdgc9SjKJJcx66%2FfF9XcA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F335cb3693fab48e8be070f7dca43aa8a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=saNxTB8XooMgf9AbGrukQ9X4eSM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F2a35932cd6b44664ac5b4fe9bd7f7ec4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=r5tBjE3DZ4Sfw0Wvqe5K%2F9uzqTw%3D)

Photo credit: https://www.flickr.com/photos/geezaweezer/16089096376/

# Sharpen filter

$ F + \alpha (F - \underbrace{F * H}_{blurred}) = $

image

image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F6a994ee7120744db83c334b7c1975dbb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=TpfGTNKUln%2Fr1bOiDnos1aCu7t0%3D)

unit impulse

(identity kernel

with single 1 in

center, zeros

elsewhere)

# Sharpen filter

unfiltered

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2Fe0e90e01175d4cf5abf8ede5913bc33c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=w40deY%2F4vx56%2F%2BqYgGBv1nKZ%2BiU%3D)

filtered

# "Optical" convolution

Camera shake

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F776ad73e30ef4fc7a5f1746bc0d67b91.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=pXJoNI%2BSLzYvfFl%2BLHG7IJI6yrc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F68f8bc1f40c949d097b7a22889670d95.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=SOzzQNf3TrGaJV1jte%2Bmwv6ORiM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F04f0a8e84416435386fed05ca3e7d30d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=WXOtC9c%2Bbxd6g66EMOljgO5dZKU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F83df4bf4121d4875851460d2bda96ef3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=SzFTfmWb%2FlPZxaWtoeIL3B%2Fnhmk%3D)

Source: Fergus, et al. "Removing Camera Shake from a Single Photograph", SIGGRAPH 2006

Bokeh: Blur in out-of-focus regions of an image.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F1d222c532961484d8da1f3c6fdba4829.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255675&Signature=rvQG%2FD7nNaiuT5xtk5CI5g%2BSyI4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F0f5c73f3116f4384aa9aa51703d0a2df.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255676&Signature=IEUM2roZqwwVRLBS3TVLVrIzWFE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F140960eac16740d88e1415d732457ca7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255676&Signature=%2B04VBc24m65u8TYJYazNRG7oMPU%3D)

Source: https://www.diyphotography.net/diy_create_your_own_bokeh/

# Filters: Thresholding

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F65e924f949b949cf8733e6bcfba2bb13.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255676&Signature=cNjWm18EAN2wb6nO9dkRvKhLoDU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9fef968ebb174b4495b9eac730dadb73%2Fmedia%2F70660c75237f44db83b91827e0d3ecbf.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255676&Signature=KKLnNzkVlFJtQDvWTFFf7aFOXvU%3D)

$$ g(m,n)=\left\{\begin{array}{cc}255,&f(m,n)>A\\ 0&otherwise\end{array}\right. $$

# Linear filters

• Can thresholding be implemented with a linear filter?

# Questions?
