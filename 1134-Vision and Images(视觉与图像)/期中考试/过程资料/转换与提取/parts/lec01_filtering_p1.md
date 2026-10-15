# CS5187: Vision & Image

Zhu Zhiyu

# Lecture 1: Images and image filtering

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2F7d87da2c960f450ca1faf5f5fe6cb6ee.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=nNvSohxT%2B8Ra50vgpFJDu1n1BT8%3D)

Hybrid Images, Oliva et al.,  $ \underline{\text{http://olivalab.mit.edu/hybridimage.htm}} $

# What is an image?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2F5f1980307cd747a6a1780c5ca615b599.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=I8yH2ZmulbcQmL8SxU3CRpBdKp0%3D)

# What is an image?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2F96bb6c8535cf44dc8dbebea56f68ce52.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=sAsQfzXsnj3TKbD1r6fkyXiLpUs%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2F8f1d20e3879b401dac4039f2e932d376.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=t4gZz79FTKJxO2AmwSeT7RdO4jA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2Ff144eceafa8b420ab443d294e70e966f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=OEJx83q2oS8fmWWKeGNl2QmNP0I%3D)

# What is an image?

• A grid (matrix) of intensity values

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2F9d6dc88f8f9a4a3a9c309e777a0492df.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=nGFFtkyTpjzQKK7xgrOQ3jdBtsY%3D)

<table><tr><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>255</td><td>20</td><td>0</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>255</td><td>75</td><td>75</td><td>75</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>75</td><td>95</td><td>95</td><td>75</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>96</td><td>127</td><td>145</td><td>175</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>127</td><td>145</td><td>175</td><td>175</td><td>175</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>127</td><td>145</td><td>200</td><td>200</td><td>175</td><td>175</td><td>95</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>127</td><td>145</td><td>200</td><td>200</td><td>175</td><td>175</td><td>95</td><td>47</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>127</td><td>145</td><td>145</td><td>175</td><td>127</td><td>127</td><td>95</td><td>47</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>74</td><td>127</td><td>127</td><td>127</td><td>95</td><td>95</td><td>95</td><td>47</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>255</td><td>74</td><td>74</td><td>74</td><td>74</td><td>74</td><td>74</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr><tr><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td><td>255</td></tr></table>

(common to use one byte per value: 0 = black, 255 = white)

# What is an image?

• Can think of a (grayscale) image as a function f from R² to R:

- f(x,y) gives the intensity at position (x,y)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2F4f16bcdcab3546729cb24b9b46fefc55.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=rxurFnVoZ%2FZnmmaKwhqns6JXCtI%3D)

snoop

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2Fbc7071077a3e41ecbf42deb8319bc577.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=0HbiaFMgcwaRGQB2Cobevmz%2BKHc%3D)

3D view

– A digital image is a discrete (sampled, quantized) version of this function

# I mage transformations

• As with any function, we can apply operators to an image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2F8ecef921d87d4087bf3b90343373ab87.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255574&Signature=RAxQn%2FTkn1EO8cQd0fHHBv9DQ%2BA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7a5f20f606d44ce28c104bb65b10a52f%2Fmedia%2Fe3618443c3304475969b2af831d9727a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255575&Signature=XxMo1mj69qU6gv9w60kAHJuvgiA%3D)

$ g(x,y) = f(-x,y) $

• Today we'll talk about a special kind of operator, convolution (linear filtering)

# Filters

# • Filtering

– Form a new image whose pixel values are a combination of the original pixel values

• Why?

– To get useful information from images

• E.g., extract edges or contours (to understand shape)

— To enhance the image

• E.g., to remove noise

• E.g., to sharpen and "enhance image" a la CSI

— A key operator in Convolutional Neural Networks

# Canonical Image Processing problems

• Image Restoration

– denoising

– deblurring

- Image Compression

- JPEG, HEIF, MPEG, ...

• Locating Structural Features

– corners

– edges
