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
# Question: Noise reduction

• Given a camera and a still scene, how can you reduce noise?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Fae0e1da751dc4cadaf33c22e6517b597.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255593&Signature=vS03KwMG1FLP%2BuiLpfOILvpIIRI%3D)

Take lots of images and average them!

What's the next best thing?

# I mage filtering

• Modify the pixels in an image based on some function of a local neighborhood of each pixel

<table><tr><td>10</td><td>5</td><td>3</td></tr><tr><td>4</td><td>5</td><td>1</td></tr><tr><td>1</td><td>1</td><td>7</td></tr></table>

Local image data

Some function

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2F709263a81745425f97bc6195b33ffae0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255593&Signature=%2F5F%2BzIKINqubJqyovW14PSocdE0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2F9c0c3b880fd5420bb07b80188fd96c12.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255593&Signature=zQnGnKCm%2FMPVDt8iRXPX0fdkgKk%3D)

Modified image data

# Linear filtering

• One simple version of filtering: linear filtering (cross-correlation, convolution)

– Replace each pixel by a linear combination (a weighted sum) of its neighbors

• The prescription for the linear combination is called the "kernel" (or "mask", "filter")

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Fa8a3e2fcd8184c54b1f802d263a62a29.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255593&Signature=R5ja5kcoCx5eD84Gs1fBD3tvhXs%3D)

# Convolution

Let F be the image, H be the kernel (of size  $ 2k+1 \times 2k+1 $), and G be the output image

$$ G[i,j]=\sum_{u=-k}^{k}\sum_{v=-k}^{k}H[u,v]F[i-u,j-v] $$

This is called a convolution operation:

$$ G=H*F $$

- Can think of as a "dot product" between local neighborhood and kernel for each pixel

# Convolution

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2F7ca83d1700144ebe8a4c43da48d6c9bd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255594&Signature=1yKbicWgNrhxxIQYAKAfz6MqKec%3D)

<table><tr><td>$ \overline{H} $</td><td></td></tr><tr><td></td><td>F</td></tr></table>

# Mean filtering

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Fd342b853b2d742a19ea131dd3cc2dc04.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255594&Signature=pE69UZGRa2%2B8f7V3a9jZepxJzw0%3D)

H

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

F

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>10</td><td>20</td><td>30</td><td>30</td><td>30</td><td>20</td><td>10</td><td></td></tr><tr><td></td><td>0</td><td>20</td><td>40</td><td>60</td><td>60</td><td>60</td><td>40</td><td>20</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>60</td><td>90</td><td>90</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>50</td><td>80</td><td>80</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>50</td><td>80</td><td>80</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>20</td><td>30</td><td>50</td><td>50</td><td>60</td><td>40</td><td>20</td><td></td></tr><tr><td></td><td>10</td><td>20</td><td>30</td><td>30</td><td>30</td><td>30</td><td>20</td><td>10</td><td></td></tr><tr><td></td><td>10</td><td>10</td><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

G

# Mean filtering / Moving average

<table><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

$ F[x, y] $

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

$ G[x, y] $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Fee3528eaf7bf4128ba964be860075334.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255594&Signature=13Ntju4RA2HceqLs0ux8ZYyN6DI%3D)

# Mean filtering / Moving average

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

$ G[x, y] $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Ff959174cfd9d4b4a8525775c8dafdd27.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255594&Signature=H6v11PdlMIlVUxmDAml16N9G0cw%3D)
# Mean filtering / Moving average

<table><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

$ G[x, y] $

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>10</td><td>20</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# Mean filtering / Moving average

<table><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

$ G[x, y] $

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>10</td><td>20</td><td>30</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# Mean filtering / Moving average

<table><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

$ G[x, y] $

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>10</td><td>20</td><td>30</td><td>30</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# Mean filtering / Moving average

$ G[x, y] $

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>0</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>10</td><td>20</td><td>30</td><td>30</td><td>30</td><td>20</td><td>10</td><td></td></tr><tr><td></td><td>0</td><td>20</td><td>40</td><td>60</td><td>60</td><td>60</td><td>40</td><td>20</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>60</td><td>90</td><td>90</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>50</td><td>80</td><td>80</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>50</td><td>80</td><td>80</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>20</td><td>30</td><td>50</td><td>50</td><td>60</td><td>40</td><td>20</td><td></td></tr><tr><td></td><td>10</td><td>20</td><td>30</td><td>30</td><td>30</td><td>30</td><td>20</td><td>10</td><td></td></tr><tr><td></td><td>10</td><td>10</td><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# Linear filters: examples

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F9a812967eac64a87a57b9a10a5f95660.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255617&Signature=NSyzWG26NlCGb4fl%2FmAu%2FTVbeEI%3D)

Original

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F9e14debb33dd40858637b1043c1bb7a2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=IkbhDkUGRJZFjhTSrPFFkUiGEZM%3D)

<table><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td></tr></table>

# Linear filters: examples

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F638138f230ae47d49ebd0fee53d928f8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=NzKJWn0wAIkfdNYQnNpgpxovBn4%3D)

Original

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F0e8e9e7fd0f2404682ac4b4a3e2e0f29.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=5xf9Fry6ge6vi4amvQevoLtTdRA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2Ffca93fefac5e43de80698f013b3c9f08.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=rMfLex%2FCX4eVEl8XMIrVEjUDrR0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F39a9ba3ff58d41b8adf546928e06def7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=9NS43WkmlarbtDb44kI2M0pitXY%3D)

Identical image

# Linear filters: examples

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F620e2b7cdb4740db90975d19a1402de6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=P5btKDFZ1QnfRRRERu5ohiSBhRg%3D)

Original

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F028e83c733d949a89b8f71e9f40ea854.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=qXKLTZoPcsrIHDb%2Bvtnf9BBYl3M%3D)

<table><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td></tr></table>

# Linear filters: examples

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F0ae31cc8a3d34e708c4605928c56f9ae.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=iRBotEXnp4F65MR5s4m3ltKUtk4%3D)

Original

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F0000870d08b541d698adbb9708db8be8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255618&Signature=RiyLWMBse2%2FzF6CFyhYcknVH1p4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F1afec455acf34042abf965c131679269%2Fmedia%2F298400314ec84fa5bec4017d56123022.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255619&Signature=USwXaSzmUOyqYI7W8WEd2s9%2FcLs%3D)

Shifted left by 1 pixel
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
