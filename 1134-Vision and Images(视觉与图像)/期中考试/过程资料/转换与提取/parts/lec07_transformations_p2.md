# Parametric (global) warping

• Examples of parametric warps:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2F8e7a52d5975546c0824ea470922c888c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=MDWtvKpcIE8zUurknLqrSC3mWBE%3D)

translation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2F5e6b1b56ca154290a6b1f0cf8abef5ae.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=O%2BgQxT7DrIfMyFpGHy5po9wUMSI%3D)

rotation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2F183379792257461a8daf52f876f68821.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=37Nb%2F4dtdrDcRZSDKMVm5q9616c%3D)

aspect

# Parametric (global) warping

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2Fcc69e46ce5a940d2b48ca23fd202414c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=HH3UrSWFrrUY1iuZ%2BovGPg%2B3Bcg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2Fa35613ff694147f3b729a620f3b0ffd4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=tnkhHpM28X7ypvvCg%2BQczDu4ahI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2F7822243d61ba4c3a8a2c0cc1ed474636.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=IZ4QWvSQHx4oCgG09ivwBShV2r0%3D)

• Transformation T is a coordinate-changing machine:

$$ \mathbf{p}^{\prime}=T(\mathbf{p}) $$

• What does it mean that T is global?

— Is the same for any point p

— can be described by just a few numbers (parameters)

• Let's consider linear xforms (can be represented by a 2x2 matrix):

$$ \mathbf{p}^{\prime}=\mathbf{T}\mathbf{p}\quad\left[\begin{array}{l}x^{\prime}\\ y^{\prime}\end{array}\right]=\mathbf{T}\left[\begin{array}{l}x\\ y\end{array}\right] $$

# Common linear transformations

• Uniform scaling by s:

$ (0,0) $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2F3b20257dd48a42ca87bae80b5c3afcba.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=kAYcIQRivl6JuoCKWhY5%2FFZGpnk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2Feff7a30086ff46639ecef5854c106915.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=px11M6BrMUPIeaF4T%2FAN7M%2BNrGQ%3D)

$$ \mathbf{S}={\left[\begin{array}{l l}{s}&{0}\\ {0}&{s}\end{array}\right]} $$

What is the inverse?

# Common linear transformations

• Rotation by angle  $ \theta $ (about the origin)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2F4095764a6aac4b8e983a2df8f981fe4e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=r5%2B0NVjEexYf22FHuN%2FLEWGagxc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ffb804d3e475240759dcc667e8b1ecf32%2Fmedia%2F9b2887be4e6342c8802d602fa9fbafcb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256689&Signature=i%2BYzZ5zMDW%2Bh%2FURMFcFW67cZq7Q%3D)

$$ \mathbf{R}=\left[\begin{array}{cc}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{array}\right] $$

What is the inverse?

For rotations:

$ \mathbf{R}^{-1} = \mathbf{R}^{T} $

# 2 x2 Matrices

• What types of transformations can be represented with a 2x2 matrix?

2D mirror across Y axis?

$$ x^{\prime}\quad=\quad-x $$

$$ y^{\prime}=y $$

2D mirror across line y = x?

$$ x^{\prime}\quad=\quad y $$

$$ y^{\prime}=x $$

# 2 x2 Matrices

• What types of transformations can be represented with a 2x2 matrix?

2D mirror across Y axis?

$$ \begin{array}{r l r}{x^{\prime}}&{{}=}&{-x}\\ {y^{\prime}}&{{}=}&{y}\end{array}\quad\begin{array}{r r}{\mathbf{T}=\left[\begin{array}{c c}{-1}&{0}\\ {0}&{1}\end{array}\right]} $$

2D mirror across line y = x?

$$ \begin{array}{r l r}{x^{\prime}}&{{}=}&{y}\\ {y^{\prime}}&{{}=}&{x}\end{array}\quad\begin{array}{r r}{}&{{}}&{\mathbf{T}=\left[\begin{array}{l l}{0}&{1}\\ {1}&{0}\end{array}\right]}\end{array} $$

# 2 x2 Matrices

• What types of transformations can be represented with a 2x2 matrix?

2D Translation?

$$ \begin{array}{rcl}x^{\prime}&=&x+t_{x}\\y^{\prime}&=&y+t_{y}\\\end{array} $$

**slido**

**Can a 2D translation by (tx,ty) be represented with a 2x2 matrix transformation?**
