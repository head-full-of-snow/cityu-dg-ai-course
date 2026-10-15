# Where do we go from here?

$$ \begin{bmatrix} {a}&{b}&{c} \\ {d}&{e}&{f} \\ {0}&{0}&{1} \end{bmatrix} \begin{bmatrix} {f}\\{l} \end{bmatrix} $$

what happens when we

mess with this row?

affine transformation

# Projective Transformations aka Homographies aka Planar Perspective Maps

$$ \mathbf{H}=\left[\begin{array}{ccc}{{{a}}}&{{{b}}}&{{{c}}} \\{{{d}}}&{{{e}}}&{{{f}}} \\{{{g}}}&{{{h}}}&{{{1}}}\end{array}\right] $$

Called a homography

(or planar perspective map)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F515a4d12e22a4f81abcfe0ca2d8ead52.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256769&Signature=G6XNevL9aYNHIDRt8vXRDjY4Nko%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2Ffeca27d746c846edbb8d822223bedf06.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256769&Signature=jeEi5CwvmRxDZwqRXpnS8ZLnfsI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F72f2aeeb2b0f4967a496a6cdc8e0c5d6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256769&Signature=af3Lin8rvhFZtnDfJPcY7wy0M9Y%3D)

# Homographies

$$ \left[\begin{array}{l}{{{x^{\prime}}}} \\{{{y^{\prime}}}} \\{{{w^{\prime}}}}\end{array}\right]=\left[\begin{array}{l l l}{{{a}}}&{{{b}}}&{{{c}}} \\{{{d}}}&{{{e}}}&{{{f}}} \\{{{g}}}&{{{h}}}&{{{1}}}\end{array}\right]\left[\begin{array}{l}{{{x}}} \\{{{y}}} \\{{{1}}}\end{array}\right] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F58e940df7d0940faa743258304883e4e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256769&Signature=lgCgCq57oXdJEW%2Fjt8wvwPH6mFU%3D)

What happens when the denominator is 0?

$$ \begin{aligned}&\sim\begin{bmatrix} \\{{{ax+by+c}}} \\{{{gx+hy+1}}} \\{{{dx+ey+f}}} \\{{{gx+hy+1}}} \\{{{1}}} \\\end{bmatrix}\\ \end{aligned} $$

# Homographies

# HOMOGRAPHY MATRIX & PERSPECTIVE TRANSFORMATION:

Visualizing the Denominator  $ w' \rightarrow 0 $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2Fbd2a5a08a43d4a08abb895085c2114d4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=mNp3Vq0gYtTQeYavNoJcSui6PFw%3D)

2. HOMOGRAPHY TRANSFORMATION (H)

The  $ 3 \times 3 $ Homography Matrix H:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F2d1a094d651045f3a9b4d0c01ed3d2fe.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=n9i7Le%2BuWOUFF0vIBGkzhZypTSw%3D)

3. TRANSFORMED IMAGE (Plane B)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2Fda401e26022b489696afe904eab53208.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=NmdlPJ1GtARQYiEpXAPp%2BmWzBuc%3D)

Resulting Perspective Transformation. Parallel lines meet at Vanishing Points on the Vanishing Line.

• For points $(x,y)$ in Source, as the Denominator $w^{\prime}\to0$ (near the Vanishing Line), their position $(X_{new},Y_{new})$ in Target recedes toward the Vanishing Line (Horizon) with increasing distortion.

• Parallel lines in source meet exactly on the vanishing line in the target.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2Ffa0829fcebc44d8d91e6a36b8ea15618.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=5uCONGQ3zUtJQIMzM7cP%2FWy0j2E%3D)

# Points at infinity

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F7aeacd4e17844fb8915e1889edbe46a5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=DT51Q9bcn%2FLjZOY7lPbW70t%2BTds%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F5b6f57c39fb14df490d1023e34ee4355.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=2inB9%2BJVuvHUhpavJFwntStABLo%3D)

# I mage warping with homographies

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2Fe2ffe3c28dd741e0b10ad3405f447ea4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=a8KtLonGF2C0Q5%2Bo%2FE1q1iwdBJY%3D)

# Homographies

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F082e79c67be14580a6fb803c1d0ba72c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=jAlIWWhiJROeq0JCXJ2%2BV%2BAArOU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F67162336505648c8bb7def7314a15575.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=a%2FmaOE5Q6KBcY9tn%2F%2FffA1qlXTw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2Fa972083b614848019d27d626798a2957.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256770&Signature=BFYEUvxxc4no3uwG3gS7ZXXodpY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff41f51f675b140368e1a1505fe7e95f2%2Fmedia%2F9d72748b907448fb9f335121c53c006e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256771&Signature=9jBqcN5QcvZCMyVBnplH25wzFgE%3D)

# Homographies

• Homographies ...

— Affine transformations, and

— Projective warps

$$ \left[\begin{array}{c}{{{x^{\prime}}}} \\{{{y^{\prime}}}} \\{{{w^{\prime}}}}\end{array}\right]=\left[\begin{array}{c c c}{{{a}}}&{{{b}}}&{{{c}}} \\{{{d}}}&{{{e}}}&{{{f}}} \\{{{g}}}&{{{h}}}&{{{1}}}\end{array}\right]\left[\begin{array}{c}{{{x}}} \\{{{y}}} \\{{{w}}}\end{array}\right] $$

• Properties of projective transformations:

– Origin does not necessarily map to origin

– Lines map to lines

– Parallel lines do not necessarily remain parallel

– Ratios are not preserved

– Closed under composition

• Key fact: homographies are only defined up to a scale factor (e.g., H and 2H are equivalent homographies)
