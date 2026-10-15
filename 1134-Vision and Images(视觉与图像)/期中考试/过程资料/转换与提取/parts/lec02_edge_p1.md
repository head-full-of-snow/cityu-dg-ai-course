# CS4186: Computer Vision

## Prof. Zhu Zhiyu

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2Fcc41aed7fa1e4c36a13392ee6e3712ef.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255700&Signature=c%2B0qzyvCS0zks6ouJul2iUkMB2s%3D)

# Edge detection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2F6836978381e445e1bcf99693926e4654.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255700&Signature=te%2Bp4A20CH6e44RzsWYZrAZSgic%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2F68a14821acb743949f8c1743a450fd67.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255700&Signature=IsolJK2GKSgNBeIeFMcIjY%2FmW4k%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2F619e519ac1af4158b9fe8d7e508ac5a1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255700&Signature=uGXqK4Wj9xmzBt6RoVvbO9Zfb6w%3D)

- Convert a 2D image into a set of curves

— Extracts salient features of the scene

— More compact than pixels

# Origin of edges

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2Fc6d8ce372eb945c8b58229935b374a96.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255700&Signature=VfyS21%2FgYLk5PQmMoQrVeBcGtiM%3D)

surface normal discontinuity

depth discontinuity

surface color discontinuity

illumination discontinuity

• Edges are caused by a variety of factors

# I mages as functions

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2F17a478a6fd6e44ddae5a237b9d987947.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255700&Signature=sxON3lTM5CSCY%2BBIJWSFcBLXbQc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2F4f3b89e37a3448218042baa0c6429c1e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255700&Signature=nyqkOnx9GUjhxP25QIePFmGGLKY%3D)

• Edges look like steep cliffs

# Characterizing edges

• An edge is a place of rapid change in the image intensity function

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2F0bd82e054a4e4c469ed2ecea08dda139.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255701&Signature=KnOQfZFOrPc%2B2pXQR8tLPAD74Ck%3D)

# I mage gradient

• The gradient of an image:  $ \nabla f = \left[\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right] $

The gradient points in the direction of most rapid increase in intensity

$$ \begin{array}{r}{\nabla f=\left[\frac{\partial f}{\partial x},0\right]}\end{array} $$

$$ \begin{array}{c} \left.\begin{array}{l}\Delta f=\left[\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right]\\ \end{array}\right.\\ \left.\begin{array}{l}\nabla f=\left[0,\frac{\partial f}{\partial y}\right]\\ \end{array}\right.\end{array} $$

The edge strength is given by the gradient magnitude:

$$ ||\nabla f||=\sqrt{(\frac{\partial f}{\partial x})^{2}+(\frac{\partial f}{\partial y})^{2}} $$

The gradient direction is given by:

$$ \theta=\tan^{-1}\left(\frac{\partial f}{\partial y}/\frac{\partial f}{\partial x}\right) $$

• how does this relate to the direction of the edge?

# I mage derivatives

• How can we differentiate a digital image F[x,y]?

– Option 1: reconstruct a continuous image, $f$, then compute the derivative

– Option 2: take discrete derivative (finite difference)

$$ \frac{\partial f}{\partial x}[x,y]\approx F[x+1,y]-F[x,y] $$

How would you implement this as a linear filter?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2Fb7c596de4b094897a154355ee4ad2d41.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255701&Signature=Ipvvvm8QTqPxxW0LNjiQL0IMesU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2F7f0a58a215ef4842ab9e9dbd90e1c6e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255701&Signature=4DpDN2q8vNPw3vCaY7d2ZuPupcQ%3D)

# I mage gradient

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2F2e527905d7a0496a92d513cd4c3fbbab.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255701&Signature=7tS3gOrkSfxUHyNWOMQswYAr3H4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2Fc2360e218bd241e9bd468444ad8cc568.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255701&Signature=2V9y15vMrHytKC7WJUflkWIc1Tg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2Fdf6a94550ccd4694a7139d13b630842b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255701&Signature=w3tQc7l2qF0A%2FarpN%2Fcmn3o%2FcuU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F27379e99a38e4f62877c252e953ca6f1%2Fmedia%2Fe9dca579f00349859c80f526ae546560.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255706&Signature=UEO6hKUjm50mQLvpMg0YMbgOL5Q%3D)
