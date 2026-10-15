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
