# Upsampling

• This image is too small for this screen:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F2f6fcbe23c234145846a2c4f2731e1f3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255864&Signature=PdEAjNqtA6FtyL1rgJZ1e2l5QEY%3D)

• How can we make it 10 times as big?

• Simplest approach:

repeat each row

and column 10 times

• ("Nearest neighbor interpolation")

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fdc30d009ff6f4fbea43e6f6f432d512c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255864&Signature=K5b8j0oMx66ccDbO055lM0qDk4Q%3D)

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F889287fabe304308bfc850a52dc570b7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255864&Signature=D6tJghxvQdO7p8ghQelyW2ZqDcA%3D)

d = 1 in this example

Recall that a digital images is formed as follows:

$$ F[x,y]=quantize\{f(xd,yd)\} $$

• It is a discrete point-sampling of a continuous function

- If we could somehow reconstruct the original function, any new image could be generated, at any resolution and scale

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fd53dfe6f3a2d4c38b760d7490c5be49b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=CTt8t%2FrxIArwYf3S25E81PD4O38%3D)

d = 1 in this example

Recall that a digital images is formed as follows:

$$ F[x,y]=quantize\{f(xd,yd)\} $$

• It is a discrete point-sampling of a continuous function

- If we could somehow reconstruct the original function, any new image could be generated, at any resolution and scale

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fc75dacc4c8e3449fa3db69ea45ab89c3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=XLTTDm7xH7vdnf8npQ5bqssMU%2FM%3D)

d = 1 in this example

• What if we don't know f ?

• Guess an approximation:  $ \tilde{f} $

• Can be done in a principled way: filtering

- Convert $F$ to a continuous function:

$ f_{F}(x) = F\left(\frac{x}{d}\right) $ when  $ \frac{x}{d} $ is an integer, 0 otherwise

• Reconstruct by convolution with a reconstruction filter, h

$$ \tilde{f}=h*f_{F} $$

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fc80f20f2a9b54d0a8c966a872d6f4d98.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=UaTVVsyTdyRXee3NLn8rgcc6OBo%3D)

"Ideal" reconstruction

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F479f7eb7605b41bdabe3fc6b55ec6f17.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=%2FMAlavvZ8bXtYub4BJLK3j20nW0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F10ce837d4f594107be3ba6996b8e54d7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=szz2f%2FhpBNl%2B7iZFALXPFOyS25o%3D)

Nearest-neighbor interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F91cb023f03454a1fb3901da9ad795da1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=Z6%2FPjuDAUn5tM0IFhclclbmm1d0%3D)

Linear interpolation

<table><tr><td>gauss(x)</td><td>x</td></tr></table>

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fff44202fb17140dba4dff90f13fe3345.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=0p2%2FcFYcib5ZeXBkRs13wqmkr48%3D)

Gaussian reconstruction

# Reconstruction filters

• What does the 2D version of this hat function look like?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F7efcd10fa0294e76a0e5625134e742e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=aRaC1c6O%2B6VowWeJBR9358mtDko%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F7ae90722d1564e318f185c807b0d5387.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=sMHd%2B%2BQE2%2Fl4U3hLDtR5ezIT3tw%3D)

Often implemented without cross-correlation

• E.g.,  $ \underline{\text{http://en.wikipedia.org/wiki/Bilinear_interpolation}} $

Better filters give better resampled images

• Bicubic is common choice

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fd6dbc9076bda4a21ae588fc7d534d98a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=DGVwhAl5ssBKJxcJMjVNEErHKBA%3D)

Cubic reconstruction filter

$$ r(x)=\frac{1}{6}\begin{cases}(12-9B-6C)\left|x\right|^{3}+(-18+12B+6C)\left|x\right|^{2}+(6-2B)&\left|x\right|<1\ $ (-B-6C)\left|x\right|^{3}+(6B+30C)\left|x\right|^{2}+(-12B-48C)\left|x\right|+(8B+24C)&1\leq\left|x\right|<2\\0&otherwise\end{cases} $$

# I mage interpolation

Original image: x 10

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fd75905cc86d84aedb11f1668d66923b6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=Y6U0NUrALv8nDHchNVJ4Tr1VfYI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Ff1af767633c74cdb9c8ccecc33f0dccd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=6TQi3miFQ9oYXGVNdOEJ3jHWQyI%3D)

Nearest-neighbor interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Faef2116fd9444b81b830ff9d95bb953f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=HDguqnDYoDWN1HFgeLXT2yo4Ask%3D)

Bilinear interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fcc75f762d28e49b2a54176a02e81cf0f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=Id9B4yuod9nxX1Z0JIyIKBze%2Bc0%3D)

Bicubic interpolation

# I mage interpolation

Also used for resampling

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F1ad2dc37f95f4e60be7293203c7e760e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=gvgpKDkuO8u9vHSWeC%2F1%2F%2BdY2QI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F384557637cfc48f89e439c700767bd5d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=OwxXPRP2AW2%2Bd1r2hQt4phPmQkg%3D)
