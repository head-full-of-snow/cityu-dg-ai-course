# 2 x2 Matrices

• What types of transformations can be represented with a 2x2 matrix?

2D Translation?

$$ x^{\prime}=x+t_{x} $$

NO!

$$ y^{\prime}=y+t_{y} $$

Translation is not a linear operation on 2D coordinates

**All 2D Linear Transformations**

• Linear transformations are combinations of ...

- Scale,

– Rotation,

– Shear, and

$$ \begin{bmatrix}{{{x^{\prime}}}} \\{{{y^{\prime}}}}\end{bmatrix}=\begin{bmatrix}{{{a}}}&{{{b}}} \\{{{c}}}&{{{d}}}\end{bmatrix}\begin{bmatrix}{{{x}}} \\{{{y}}}\end{bmatrix} $$

- Mirror

**• Properties of linear transformations:**

– Origin maps to origin

– Lines map to lines

– Parallel lines remain parallel

– Ratios are preserved

– Closed under composition

$$ \begin{bmatrix}{{{x^{\prime}}}} \\{{{y^{\prime}}}}\end{bmatrix}=\begin{bmatrix}{{{a}}}&{{{b}}} \\{{{c}}}&{{{d}}}\end{bmatrix}\begin{bmatrix}{{{e}}}&{{{f}}} \\{{{g}}}&{{{h}}}\end{bmatrix}\begin{bmatrix}{{{i}}}&{{{j}}} \\{{{k}}}&{{{l}}}\end{bmatrix}\begin{bmatrix}{{{x}}} \\{{{y}}}\end{bmatrix} $$

**Homogeneous coordinates**

Trick: add one more coordinate:

$$ (x,y)\Rightarrow\left[\begin{array}{c}x\\ y\\ 1\end{array}\right] $$

homogeneous image

coordinates

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4b63dc229684b36be03371feb9d34d2%2Fmedia%2Ff2e73ae45ddd4f21a8d8bcf17aace095.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256720&Signature=21VbrajQrG3UKdMg9YOjIiWejyQ%3D)

Converting from homogeneous coordinates

$$ \begin{bmatrix}x\\ y\\ w\end{bmatrix}\Rightarrow(x/w,y/w) $$

**Translation**

• Solution: homogeneous coordinates to the rescue

$$ \mathbf{T}=\left[\begin{array}{ccc}1&0&t_{x}\\0&1&t_{y}\\0&0&1\end{array}\right] $$

$$ \left[\begin{array}{ccc}1&0&t_{x}\\0&1&t_{y}\\0&0&1\end{array}\right]\left[\begin{array}{c}x\\y\\1\end{array}\right]=\left[\begin{array}{c}x+t_{x}\\y+t_{y}\\1\end{array}\right] $$

**Affine transformations**

$$ \begin{aligned}&\mathbf{T}=\begin{bmatrix} \\{{{1}}}&{{{0}}}&{{{t_{x}}}} \\{{{0}}}&{{{1}}}&{{{t_{y}}}} \\{{{0}}}&{{{0}}}&{{{1}}} \\\end{bmatrix}\begin{aligned}\\ &\leftarrow\\ &\end{aligned}\\ \end{aligned} $$

any transformation

represented by a 3x3 matrix

with last row [0 0 1 ] we call

an affine transformation

$$ \begin{bmatrix}{{{a}}}&{{{b}}}&{{{c}}} \\{{{d}}}&{{{e}}}&{{{f}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{bmatrix} $$

**Basic affine transformations**

$$ \begin{bmatrix}x^{\prime}\\ y^{\prime}\\ 1\end{bmatrix}=\begin{bmatrix}1&0&t_{x}\\ 0&1&t_{y}\\ 0&0&1\end{bmatrix}\begin{bmatrix}x\\ y\\ 1\end{bmatrix} $$

Translate

$$ \begin{bmatrix}{{{x^{\prime}}}} \\{{{y^{\prime}}}} \\{{{1}}}\end{bmatrix}=\begin{bmatrix}{{{s_{x}}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{s_{y}}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{bmatrix}\begin{bmatrix}{{{x}}} \\{{{y}}} \\{{{1}}}\end{bmatrix} $$

Scale

$$ \begin{bmatrix}{{{x^{\prime}}}} \\{{{y^{\prime}}}} \\{{{1}}}\end{bmatrix}=\begin{bmatrix}{{{\cos\theta}}}&{{{-\sin\theta}}}&{{{0}}} \\{{{\sin\theta}}}&{{{\cos\theta}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{bmatrix}\begin{bmatrix}{{{x}}} \\{{{y}}} \\{{{1}}}\end{bmatrix} $$

2D in-plane rotation

$$ \begin{bmatrix}{{{x^{\prime}}}} \\{{{y^{\prime}}}} \\{{{1}}}\end{bmatrix}=\begin{bmatrix}{{{1}}}&{{{s h_{x}}}}&{{{0}}} \\{{{s h_{y}}}}&{{{1}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{bmatrix}\begin{bmatrix}{{{x}}} \\{{{y}}} \\{{{1}}}\end{bmatrix} $$

Shear

**Affine transformations**

• Affine transformations are combinations of ...

— Linear transformations, and

– Translations

$$ \begin{bmatrix}{{{x^{\prime}}}} \\{{{y^{\prime}}}} \\{{{w}}}\end{bmatrix}=\begin{bmatrix}{{{a}}}&{{{b}}}&{{{c}}} \\{{{d}}}&{{{e}}}&{{{f}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{bmatrix}\begin{bmatrix}{{{x}}} \\{{{y}}} \\{{{w}}}\end{bmatrix} $$

• Properties of affine transformations:

– Origin does not necessarily map to origin

– Lines map to lines

– Parallel lines remain parallel

– Ratios are preserved

– Closed under composition

**I s this an affine transformation?**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4b63dc229684b36be03371feb9d34d2%2Fmedia%2F64ede5aec0904912a133317aa53dad10.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256720&Signature=%2Ff1%2FEKGQ2fEtyAbvPXMIaJWgSPw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4b63dc229684b36be03371feb9d34d2%2Fmedia%2Fab6ee4d2d93f4dfb87be99cfa4d16d6a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256720&Signature=gPOaM8YV7sm6znl2jAYHaogxFUs%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4b63dc229684b36be03371feb9d34d2%2Fmedia%2Ff537a12787b94fdab6e55aae5328f3e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256720&Signature=fLveZuEGq1lfXFT8NjdU7c5gfbQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4b63dc229684b36be03371feb9d34d2%2Fmedia%2F0f3debe704064a449b03dc0055741eb9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256720&Signature=DZ53oBhpwN8FlzsRnM7drPdAMrA%3D)
