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
# Effects of noise

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2Fdf0036a826444c9b9f5843f65cac805c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255732&Signature=2stw%2B%2F0YSBxL3v%2BFnIePpf9DgCs%3D)

Noisy input image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F90273779f309454caab6ae349ee9e88d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255732&Signature=qA%2F5d0SOqKQWulMaP9a3AhVOS5U%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F8693e7a0a0b248febde644da49fe380c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255732&Signature=JRdjtRb0g4x4sMQ7g3Fzw2uO4Sk%3D)

Where is the edge?

Source: S. Seitz

# Solution: smooth first

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F98aca97be3104dc7b76de48f91a1f68c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=SktCoOyVVUFXGVwRcH7WRjvxT8s%3D)

To find edges, look for peaks in  $ \frac{d}{dx}(f \times h) $ Source: S. Seitz

# Associative property of convolution

• Differentiation is convolution, and convolution is associative:

$$ \frac{d}{dx}(f*h)=f*\frac{d}{dx}h $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F0546c54b81e34fa19759a2b765d78301.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=vqq%2Bv43UvykUHxd5Aee5gGDbOU4%3D)

$$ \frac{d}{dx}\left(f*h\right)=\frac{d}{dx}\int f(t)\cdot h(x-t)dt=\int f(t)\cdot\frac{d}{dx}h(x-t)dt=f*\frac{d}{dx}h $$

• This saves us one opera

# The 1D Gaussian and its derivatives

$$ G_{\sigma}(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{x^{2}}{2\sigma^{2}}} $$

$$ G_{\sigma}^{\prime}(x)=\frac{d}{dx}G_{\sigma}(x)=-\frac{1}{\sigma}\left(\frac{x}{\sigma}\right)G_{\sigma}(x) $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2Ff89c045e8ade4978b7c06a179a27241a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=ynR2CneeigFDo%2BciqoafX3nnonw%3D)

# 2 D edge detection filters

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F9f5757d2d1c94942b3e274fb4c3bdd8c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=KjnBE6areaTHxNj3cI3VzJDXC0Y%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F4c0a1f5a46e64440b165c46758516d45.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=qVwJqgtsm7y00QZp%2F%2BuEwpETIno%3D)

$$ h_{\sigma}(u,v)=\frac{1}{2\pi\sigma^{2}}e^{-\frac{u^{2}+v^{2}}{2\sigma^{2}}} $$

derivative of Gaussian (x)

$$ \frac{\partial}{\partial x}h_{\sigma}(u,v) $$

**Derivative of Gaussian filter**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F9069fac9dc934992ae6499028cb88a1d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=ZuPerJH3V6EgzdcyDL5DjDrSNAw%3D)

x-direction

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F300c4f8ccddc43eeb9576fc6dc923b38.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=rI2FYtDObVsNFhI%2BFT8FBuViiXY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F016ea794f3f24bd5aaee43f26031f793.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=H%2BR6R4KyIMDI5wJLIA%2B0ZJM%2Bw7I%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F20edb21b3ef940c381337ab6066e6a88.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255733&Signature=UkN2dKF5v%2FE7Nh2V87YMeVJeKPY%3D)

**The Sobel operator**

• Common approximation of derivative of Gaussian

<table><tr><td>-1</td><td>0</td><td>1</td></tr><tr><td>-2</td><td>0</td><td>2</td></tr><tr><td>-1</td><td>0</td><td>1</td></tr></table>

$S_{x}$

<table><tr><td>1</td><td>2</td><td>1</td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>-1</td><td>-2</td><td>-1</td></tr></table>

$sy$

• The standard definition of the Sobel operator omits the 1/8 term

– doesn’t make a difference for edge detection

– the 1/8 term is needed to get the right gradient magnitude

**Sobel operator: example**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2Fcbbe50deb99a41e38016775ae526b29b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255734&Signature=d81AlcQL0dIoesgj5hQGErHmwWc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F645ade16cdb14ce0a113302bf9036bb4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255734&Signature=yvdaXYMT%2F%2FbS6UjgcpMKX3EBtyQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2Fffab6a065a7e4e63a38384bf98de287b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255734&Signature=3iUpWdiL%2FanCbQLjvmhBiUDgqdU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F31994a9a3aa74cf4996f13c4c1c1b865.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255734&Signature=WdDyNDJ8GCsUasBci6uwlNL%2Bva4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9327354269f6423ab9a7eeabef5df328%2Fmedia%2F9c88a33f87144ff2b95422d7011d3df2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255734&Signature=apMgq5OcPBxD8o5V5Pl8PV1RcRk%3D)
![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Feddabb92a4cd4b0db7e980d41b799c45.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=pJk6KYATXwDt8XgIjRs85dX%2Ft%2Fw%3D)

Image with Edge

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F284c975adad64444b5187a407952563e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=SC5VvaJrgh%2FYGEIxgPRL0spOClE%3D)

Edge Location

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Fee61dff4007f4b7b98bcee7b8a428090.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=qTqOgvtFyee8uWUEg3lWMmPQIvA%3D)

Image + Noise

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Ff485f84c49ce421495c7441f6bd9a047.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=rywTXfc7JdHC9e4vEBWeDmmA0iE%3D)

Derivatives detect edge and noise

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F379aaabac4c849fe8dddfcd6ea125ab4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=KTpiGCOEPiQ%2F6qu2T1D6I3jpL20%3D)

Smoothed derivative removes noise, but blurs edge

# Example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Fe4fbbaeefbc84ef7b5ce38e6cf7cc2e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=UMHennxumoEx9CDKY3Y%2FSxYnpU0%3D)

original image

# Finding edges

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F379067c92add4afc83f7eaddf80b03d0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=JFvW4%2FsEE4HGOyBpfou7hDuEozo%3D)

smoothed gradient magnitude

# Finding edges

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Fd3409b8221814574bc3c7641c1ec5407.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=lA4D510GmIFavctdjqueE27w4P4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Ff3e465968b5546878115935a690a3487.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=28TawF%2BJx%2FjauWErCRs6w1X30nY%3D)

thresholding

where is the edge?

# Get Orientation at Each Pixel

• Get orientation (below, threshold at minimum gradient magnitude)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Fa24df8ed07fd49fea9aeb6aff18f3a6b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=GdSy%2FVtDX8syfMqoYM73uACFO5E%3D)

$$ \theta=atan2(gy,gx) $$

Gradient orientation angle

# Non-maximum suppression

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F195533c32b8b4c5eb84b818475daa5e1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=rFc9AinaNJp9vx5nTrWJuGskap8%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F44035775a68e4e3c9ee35a7627da24d4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=iT207GfntOw72lyg9Do41b9X%2BDs%3D)

- requires interpolating pixels p and r

# Before Non-max Suppression

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F61506debd30d4d5c83c48fcdb6b18983.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=KIyZc46ZtawcRCJuTkDARUbB2Ps%3D)

# After Non-max Suppression

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F748e65723390423b876fe50b202d3625.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=i8oec0cZdofaRE5aD6DMcGTW8ek%3D)
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
