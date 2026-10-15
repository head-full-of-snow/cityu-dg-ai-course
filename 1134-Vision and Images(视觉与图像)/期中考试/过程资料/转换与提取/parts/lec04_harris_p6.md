# Harris detector example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2Fb2e08f7e868f490b8e53827fed603788.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256047&Signature=EOqAvdEpoSq8%2Fatc%2FO61D4dhIL4%3D)

# f value (red high, blue low)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F26d2079f3caa47769a3d977970385632.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256047&Signature=YxC8dbAAYrDz1%2F6D53II68b0X%2BA%3D)

# Threshold (f > value)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2Ff71ec1cd410c4c4cbdb8fd693743611e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256047&Signature=W6JJFkWN8Y9U%2B%2F0UcblUCW523XI%3D)

# Find local maxima of f (non-max suppression)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F02c60577c6804ce89ff25c81feb24436.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256048&Signature=6T9xUanSaIf4pilsZUWY3zX7bME%3D)

# Harris features (in red)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F7af6e67946b44f5799bf8d7c30ada54e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256048&Signature=CiFi%2Fs5GlgP%2Bqj7bO7hMarOWG%2BU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F05498d07be8e49af9a9745d6d998dfa4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256048&Signature=LgGeIRw1Mvam%2B9ic5A0fNHwVR9A%3D)

# Weighting the derivatives

• In practice, using a simple window W doesn't work too well

$$ H=\sum_{(x,y)\in W}\left[\begin{array}{cc}I_{x}^{2}&I_{x} I_{y}\\ I_{x} I_{y}&I_{y}^{2}\end{array}\right] $$

• Instead, we'll weight each derivative value based on its distance from the center pixel

$$ H=\sum_{(x,y)\in W}w_{x,y}\left[\begin{array}{cc}I_{x}^{2}&I_{x} I_{y}\\ I_{x} I_{y}&I_{y}^{2}\end{array}\right] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F61282bbff7b64a9e9ce7c0b0ea344059.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256048&Signature=yte9Qyq47X8xyax92ICmjxH7hx8%3D)

# Harris Detector – Recap [Harris88]

Second moment matrix

$$ \mu(\sigma_{I},\sigma_{D})=g(\sigma_{I})*\begin{bmatrix}I_{x}^{2}(\sigma_{D})&I_{x}I_{y}(\sigma_{D})\\ I_{x}I_{y}(\sigma_{D})&I_{y}^{2}(\sigma_{D})\end{bmatrix} $$

$$ \det M=\lambda_{1}\lambda_{2} $$

trace  $ M = \lambda_{1} + \lambda_{2} $

0. Input image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F5d4769d154604f0a973b8f762e15ae9b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256048&Signature=vgVod24lLiQeFEhiEga0vyTG31k%3D)

1. Image derivatives

2. Square of derivatives

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F01edb5693b774b09a0c7628cc853ed3d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256048&Signature=Wi9G6NDLcnCE3JQW30RCd1vZq7I%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F2f2b2346f7d540faa025f8bfc5245f03.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256048&Signature=c%2BEnyj%2B%2F4tYMUN5H%2FfnjRJYPaFI%3D)

3. Gaussian filter  $ g(s_{i}) $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F1e4d29d4fe0d431a9d4f7393ad8c9ab2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256053&Signature=9KX6E1DNt52LnKL0b%2BMMROOdKhU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F19a733ea81254883a6ea4075ed091100.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256053&Signature=288mFq%2FZ4T5JuPaaTdztRSPhChw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2Fa373adc860c7473386f4dc7cad86d938.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256054&Signature=zNQ4y6AKEf60NhwmG8rfdDfkZjg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F03396f01b86b40e690e9e461b0022d7b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256054&Signature=ciP7owIkV%2Fi03ccVpcRlztboC3c%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2Fc2b5512131b14fcf90f1485abf490918.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256054&Signature=U5BQ%2FxKG2u2r5wJgugUxYbiPKNY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2Ffe0b841c4721400ca5113f832f3a689c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256054&Signature=8%2BP%2FgMGN2tmRIxPukf6uBSQyHpE%3D)

4. Cornerness function – both eigenvalues are strong

5. Non-maxima suppression

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F60c925c6190f4a3d84c824e190ba6c57.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256054&Signature=Xhn5%2BZUSxKPWfOn08NUWArSgWiQ%3D)

# Harris Corners – Why so complicated?

• Can't we just check for regions with lots of gradients in the x and y directions?

— No! A diagonal line would satisfy that criteria

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fceadcb21f4354f71918e63356afdaa6b%2Fmedia%2F9fec860a715042e0b627d13a3afa519a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256054&Signature=E6VOA7fnP%2F1iEGZ0H0dDc413Y1s%3D)
