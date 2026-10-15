# CS5187: Vision & Image Local features & Harris corner detection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Ffab400c2025349c3bd80e9165aa0ef88.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255914&Signature=yCM2HXDce6oqRkuWuE7WVen6%2FyA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F22023cf793db48af8269b6ab79a2c0b5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=dJPvN1V0WxheTTQIWHXdLpzPYEw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fc489ee698147498484da41e9eb4b2493.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=WoMJAG1b8LJIjQDdUUqW1oz%2Fbtw%3D)

# Today: Feature extraction—Corners and blobs

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fb6821dc5b04141f4a46a94ce39994e33.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=L7IlUBexaxD1fktzR5zsXOMRwl0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fe9230d0726c64cff9fcc90f9d3dcd671.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=b9G18ZOf1cJxX0%2BXMwRHUw2amHw%3D)

# Motivation: Automatic panoramas

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F059e3f965fef4d5aae2b0ee4510012b7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=UUaA5DyRf%2FLBjY4OXlMQC3cu49w%3D)

Credit: Matt Brown

# Panorama stitching

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fd2e7a716efd24a17bf317c97c8bd451c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=aqHc6fydl98Tcz41Z%2FMsg2QkjbM%3D)

Panorama captured by Perseverence Rover, Feb. 20, 2021

# Motivation: Automatic panoramas

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fb7d4582d6ca24efd83a7eeec0cb49330.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=YxKsQ8b3cZqiXkKtwVNjnVLJMnc%3D)

GigaPan:

http://gigapan.com/

Also see Google Zoom Views:

https://www.google.com/culturalinstitute/beta/project/gigapixels

# Why extract features?

• Motivation: panorama stitching

– We have two images – how do we combine them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F8016aa5185184b8fb2aba8fa3b83b46b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=iObjTtphKShyHXRUkn7MWBCJjIk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fc98254a37f4f43559cab490e5fc7306b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255921&Signature=OZJA3vhHw2YHEk0YtR5Zd5wDkwk%3D)

# Why extract features?

• Motivation: panorama stitching

– We have two images – how do we combine them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F06d17798911f4748a0fc28b5998491d0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255921&Signature=qIucg%2FjIzW8DXfs5Y%2FcBtnNXG%2BQ%3D)

Step 1: extract features

Step 2: match features

# Why extract features?

• Motivation: panorama stitching

– We have two images – how do we combine them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F8d072887d1eb42cbb7a14786bce8d113.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255921&Signature=aSt%2FPhNgFp8Q0qxchnoTli40ygk%3D)

Step 1: extract features

Step 2: match features

Step 3: align images
# Application: Visual SLAM

• (aka Simultaneous Localization and Mapping)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2F4e057d9a3ada4f1cb92c0730d5dc12a6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255957&Signature=k7%2FpQtk3J0acHkcc3kjoUf%2FiT1g%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2Fdd9a7c87666549ac9d0bc61e453b3dd7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255957&Signature=e%2FFz2rzJ%2Bu7xfdZG3L1qDQUvsrw%3D)

# Do these images overlap?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2F6c771f393c79457ebd99b09e4334ea13.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255958&Signature=izcc824gpfXDO2wQtfr%2Fopv%2B5NA%3D)

#### Answer below (look for tiny colored squares...)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2F8a0cf81f87fa473999337076c923f606.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255958&Signature=q5%2F32o80irhz0oDK0z7sr3E3rmk%3D)

NASA Mars Rover images with SIFT feature matches

# Feature matching for object search

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2F9f19721fbe954a29b46c20e9aa715923.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255958&Signature=UUntS6VQLWUFEuf4QpQoGv1gYJc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2Faeefc04032a34ad8844ff0c1cc7ead38.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255958&Signature=fjuzSdimpsQbDVJOJQ7UypuQteo%3D)

# Feature matching

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2Fa8ceb8eab01f402aa754952d4a18d173.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255958&Signature=zVgks8k5TejlXFpDrQ%2FhaViGBXA%3D)

# I nvariant local features

Find features that are invariant to transformations

- geometric invariance: translation, rotation, scale

– photometric invariance: brightness, exposure, ...

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2F65c80ab3de8c4c4caeee2827c683b3af.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255958&Signature=aGz2D7CHoBi%2FfPRUIa1rxgGRdJA%3D)

Feature Descriptors

# Advantages of local features

Locality

– features are local, so robust to occlusion and clutter

Quantity

— hundreds or thousands in a single image

Distinctiveness:

– can differentiate a large database of objects

Efficiency

– real-time performance achievable

# More motivation

Feature points are used for:

– Image alignment (e.g., mosaics)

– 3D reconstruction

– Motion tracking (e.g. for AR)

— Object recognition

– Image retrieval

– Robot/car navigation

- ... other

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fc4ac3928d4f349ebbd9134c9d1645e44%2Fmedia%2Fea637cc836b7429fb6d39db8cb0dc1ce.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255958&Signature=Zprn5sQR5EcaH3xOzskxmrJtBlU%3D)
# Approach

1. Feature detection: find it

2. Feature descriptor: represent it

3. Feature matching: match it

Feature tracking: track it, when motion

# Local features: main components

1) Detection: Identify the interest points

2) Description: Extract vector feature descriptor surrounding each interest point

3) Matching: Determine correspondence between descriptors in two views

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2F79fc8b2e7eb14d6ba59e9a045ead721c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255979&Signature=%2Fz1d6DvKIvu5aJ1LyImF5RAByrk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2Fc6b0a7265f9e4f24b8462e966a8f9bb8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=J6SJspqblJJ96muR%2BxqLuLZAMRI%3D)

$$ \mathbf{x}_{2}^{\downarrow}=[x_{1}^{(2)},\ldots,x_{d}^{(2)}] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2F208fdf21911a4470918e83db359ecc75.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=qdJjHhB92f%2Fb%2BsiPLD3r2B%2BdjMU%3D)

What makes a good feature?

# Want uniqueness

Look for image regions that are unusual

– Lead to unambiguous matches in other images

How to define "unusual"?

# Local measures of uniqueness

Suppose we only consider a small window of pixels

– What defines whether a feature is a good or bad candidate?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2F223fa42d54664cd3b97640215dc608c9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=VreHxtvOPRNPWXbvBvFKU6CbYGQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2Fdc70082e81df427794b00c6fc9ddbfb0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=6E7eaX2ehMtLCM1kQuaX4BtM%2BGM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2F17302327fe00453c90a726c9798c9f5a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=iMMK%2Fke7Rh2cCrdM%2B4aSAdDdiDw%3D)

# Local measures of uniqueness

• How does the window change when you shift it?

• Shifting the window in any direction causes a big change

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2Fb9d5e6f94d4440dd8154acacd4e2a674.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=22RkemvsN6GlD6x5SI8lReC8nS4%3D)

"flat" region: no change in all directions

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2Fc7182e2aa275429ab6e324a4ae29e8aa.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=euCTUmhJmoPLEsJVKf6zoCOQAos%3D)

"edge": no change along the edge direction

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2F23769edc82fe4e59a5ba34b6e4a68e94.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=flm6bwzSktsYuGQb62fhGYmT%2Br0%3D)

"corner": significant change in all directions

# Harris corner detection: the math

Consider shifting the window W by  $ (u,v) $

• how do the pixels in W change?

- compare each pixel before and after by summing up the squared differences (SSD)

• this defines an SSD "error"  $ E(u,v) $:

$$ E(u,v)=\sum_{\substack{(x,y)\in W}}[I(x+u,y+v)-I(x,y)]^{2} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F242e9ef376ef4361b929b89c478a8ccd%2Fmedia%2F6562ab0f92924ea192604a2a15c37c15.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255980&Signature=KQNpW9gOXggRxLT8bQfDCnac2vE%3D)

• We are pretty happy if this error is high for some offset  $ (u, v) $

• We are very happy if this error is high for all offsets  $ (u,v) $

• But, slow to compute exactly for each pixel and each offset  $ (u,v) $

# Small motion assumption

Taylor Series expansion of  $ I $:

$$ I(x+u,y+v)=I(x,y)+{\frac{\partial I}{\partial x}}u+{\frac{\partial I}{\partial y}}v+higher order terms $$

If the motion  $ (u, v) $ is small, then first order approximation is good

$$ \begin{align*}I(x+u,y+v)\approx&I(x,y)+\frac{\partial I}{\partial x}u+\frac{\partial I}{\partial y}v\\ \approx&I(x,y)+[I_{x}\ I_{y}]\begin{bmatrix}u\\ v\end{bmatrix}\end{align*} $$

shorthand:  $ I_{x}=\frac{\partial I}{\partial x} $

Plugging this into the formula on the previous slide...
# Corner detection: the math

Consider shifting the window W by  $ (u,v) $

• define an SSD "error"  $ E(u,v) $:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F201523dc67754404a42577613262ea7b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256001&Signature=CUd%2BLtkxEV220PVw5QEnUE9pt%2Bg%3D)

$$ \begin{array}{r c l}{E(u,v)}&{=}&{\displaystyle\sum_{(x,y)\in W}[I(x+u,y+v)-I(x,y)]^{2}}\\ {}&{\approx}&{\displaystyle\sum_{(x,y)\in W}[I(x,y)+I_{x}u+I_{y}v-I(x,y)]^{2}}\\ {}&{\approx}&{\displaystyle\sum_{(x,y)\in W}[I_{x}u+I_{y}v]^{2}}\\ \end{array} $$

# Corner detection: the math

Consider shifting the window W by  $ (u,v) $

• define an SSD "error"  $ E(u,v) $:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F5a538fa568724392902de769d556959e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256001&Signature=AkjvDt1O%2F4hZMQl5tm%2B43l7UjIY%3D)

$$ \begin{array}{r l r}{E(u,v)}&{\approx}&{\displaystyle\sum_{(x,y)\in W}[I_{x}u+I_{y}v]^{2}}\\ &{\approx}&{A u^{2}+2B u v+C v^{2}}\end{array} $$

$$ A=\sum_{(x,y)\in W}I_{x}^{2}\quad B=\sum_{(x,y)\in W}I_{x}I_{y}\quad C=\sum_{(x,y)\in W}I_{y}^{2} $$

• Thus,  $ E(u,v) $ is locally approximated as a quadratic error function

# The second moment matrix

The surface  $ E(u,v) $ is locally approximated by a quadratic form.

$$ \begin{array}{r l r}{E(u,v)}&{\approx}&{A u^{2}+2B u v+C v^{2}}\\ &{\approx}&{\left[\begin{array}{l l}{u}&{v}\end{array}\right]\left[\begin{array}{l l}{A}&{B}\\ {B}&{C}\end{array}\right]\left[\begin{array}{l}{u}\\ {v}\end{array}\right]}\\ &{}&{\underbrace{\quad\quad\quad\quad}_{(x,y)\in W}\quad}\\ {A}&{=}&{\displaystyle\sum_{(x,y)\in W}I_{x}^{2}}\\ &{}&{H}\end{array} $$

$$ B=\sum_{(x,y)\in W}I_{x}I_{y} $$

$$ C=\sum_{(x,y)\in W}I_{y}^{2} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F2132df807ad54f419821ff4a66b90925.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=ZxV%2BglDMNe4Dk7HBCclHhuXQClM%3D)

Let's try to understand its shape.

$$ \begin{array}{c}{E(u,v)\approx\left[\begin{array}{l l}{u}&{v}\end{array}\right]\left[\begin{array}{l l}{A}&{B}\\ {B}&{C}\end{array}\right]\left[\begin{array}{l}{u}\\ {v}\end{array}\right]}\\ {\underbrace{\quad}_{H}}\\ \end{array} $$

$$ A=\sum_{(x,y)\in W}I_{x}^{2} $$

$$ B=\sum_{(x,y)\in W}I_{x} I_{y} $$

$$ C=\sum_{(x,y)\in W}I_{y}^{2} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F5a8dcad68f4a4ca6b6884ade72d8ff5f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=jcji%2Fv8a3%2FdMD%2FmBA5Gjilc50NE%3D)

Horizontal edge:  $ I_{x}=0 $

$$ \boldsymbol{H}=\left[\begin{array}{ll}{{{0}}}&{{{0}}} \\{{{0}}}&{{{C}}}\end{array}\right] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F32f8097f517045da9a0bf281522efba7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=LF%2BVE13XeZXzKojJdpt58CMA6So%3D)

$$ \begin{array}{c}{E(u,v)\approx\left[\begin{array}{l l}{u}&{v}\end{array}\right]\left[\begin{array}{l l}{A}&{B}\\ {B}&{C}\end{array}\right]\left[\begin{array}{l}{u}\\ {v}\end{array}\right]}\\ {\underbrace{\quad}_{H}}\\ \end{array} $$

$$ \begin{aligned}&A=\sum_{(x,y)\in W}I_{x}^{2}\\ &B=\sum_{(x,y)\in W}I_{x}I_{y}\\ &C=\sum_{(x,y)\in W}I_{y}^{2}\\ \end{aligned} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F60e4e5d5fd4b49ce9677dd25126bb47c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=RCwlvClayVggvtIsPLkh7npr9YY%3D)

$$ I_{y}=0 $$

$$ \boldsymbol{H}=\left[\begin{array}{ll}{{{A}}}&{{{0}}} \\{{{0}}}&{{{0}}}\end{array}\right] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F5d0e469cc00048afa2348d2384714976.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=j1wicbOWRKs8MhbL%2B%2B%2BFpJTxCws%3D)

# General case

We can visualize H as an ellipse with axis lengths determined by the eigenvalues of H and orientation determined by the eigenvectors of H

Ellipse equation:

$ \lambda_{\max}, \lambda_{\min} $ : eigenvalues of H

direction of the

fastest change

$$ \left[u\quad v\right]\quad H\quad\begin{bmatrix}u\\ v\end{bmatrix}=\mathbf{const} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F0e914984d7054b6aafc69c23e7be3969.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=S5GRUOKv05NdwXbaIGVfwogDWcg%3D)

direction of the

slowest change

# Quick eigenvalue/eigenvector review

The eigenvectors of a matrix A are the vectors x that satisfy:

$$ Ax=\lambda x $$

The scalar  $ \lambda $ is the eigenvalue corresponding to x

– The eigenvalues are found by solving:

$$ det(A-\lambda I)=0 $$

– In our case,  $ A = H $ is a 2x2 matrix, so we have

$$ det\left[\begin{array}{cc}h_{11}-\lambda&h_{12}\\h_{21}&h_{22}-\lambda\end{array}\right]=0 $$

— The solution:

$$ \lambda_{\pm}=\frac{1}{2}\left[\left(h_{11}+h_{22}\right)\pm\sqrt{4h_{12}h_{21}+\left(h_{11}-h_{22}\right)^{2}}\right] $$

Once you know  $ \lambda $, you find x by solving

$$ \left[\begin{array}{c c}h_{11}-\lambda&h_{12}\\ h_{21}&h_{22}-\lambda\end{array}\right]\left[\begin{array}{l}x\\ y\end{array}\right]=0 $$

# Corner detection: the math

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F50fbdd787fbc4f57bbfeb496cabe1469.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=5zEJ%2BOlAklhsQlpyaGQx4IppWy4%3D)

Eigenvalues and eigenvectors of H

• Define shift directions with the smallest and largest change in error

•  $ x_{\text{max}} = \text{direction of largest increase in } E $

•  $ \lambda_{\max} = \text{amount of increase in direction } x_{\max} $

•  $ x_{\min} = $ direction of smallest increase in E

•  $ \lambda_{\min} = \text{amount of increase in direction } x_{\min} $
# Corner detection: the math

How are $\lambda_{\max}$, $x_{\max}$, $\lambda_{\min}$, and $x_{\min}$ relevant for feature detection?

• What's our feature scoring function?

# Corner detection: the math

How are  $ \lambda_{\max}, x_{\max}, \lambda_{\min}, \text{and } x_{\min} $ relevant for feature detection?

What's our feature scoring function?

Want  $ E(u,v) $ to be large for small shifts in all directions

• the minimum of  $ E(u,v) $ should be large, over all unit vectors  $ [u\ v] $

• this minimum is given by the smaller eigenvalue ( $ \lambda_{\min} $) of H

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2F919f987563894478831ffeadaf52c77b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256023&Signature=ppr7EDtrjDurpzSPGXL4Hw2i9FQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2Ff5d133e26b724b9f8d6bb132deee2fd5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256023&Signature=gkYLDNWbx7WokS%2Bd%2FWa876pMWTQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2F256408aa095342d5a29f30b127a63e9f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256024&Signature=UM8K%2BLG%2F8K6fp9M9TTS6KJZkbPY%3D)

# I nterpreting the eigenvalues

Classification of image points using eigenvalues of M:

$$ \lambda_{2} $$

$ \lambda_{1} $ and  $ \lambda_{2} $ are small;

$ E $ is almost constant

in all directions

$$ \lambda_{2}>>\lambda_{1} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2F1991bb0de30d46fcb25e2d782823ad9a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256024&Signature=94%2BcmdRCRvcpjMbi7kiZNbD3oSY%3D)

$$ \lambda_{1} $$

$$ \lambda_{2} $$

$$ \lambda_{1}\sim\lambda_{2}; $$

$$ \lambda_{1}>>\lambda_{2} $$

# Corner detection summary

Here's what you do:

• Compute the gradient at each point in the image

• For each pixel:

• Create the H matrix from nearby gradient values

$$ H=\sum_{(x,y)\in W}\left[\begin{array}{cc}I_{x}^{2}&I_{x} I_{y}\\ I_{x} I_{y}&I_{y}^{2}\end{array}\right] $$

• Compute the eigenvalues.

• Find points with large response ( $ \lambda_{\min} > \text{threshold} $)

• Choose those points where  $ \lambda_{\min} $ is a local maximum as features

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2Fb3fe0e61a71340569255f1d253681653.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256024&Signature=2ODD5ESCjtwl05SJfF642acz5Hc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2Fba8f96a486a9425cad05e2e1cee2b5fe.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256024&Signature=4GKbylZcx2rz9fVo1WCFqkCZTzQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2Fe567ff79a601479f9d6f94ef5d424ac1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256024&Signature=5PcRAGk4m6BZ7nIcXhkM2jzGu24%3D)

# Corner detection summary

Here's what you do:

• Compute the gradient at each point in the image

• For each pixel:

• Create the H matrix from nearby gradient values

• Compute the eigenvalues.

• Find points with large response ( $ \lambda_{\min} > \text{threshold} $)

• Choose those points where  $ \lambda_{\min} $ is a local maximum as features

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2F6f1e735b13a14ddea2e5c0b0bb7eaef1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256024&Signature=QkENLsNqSL7pxTmr1fdYyoe%2BiZg%3D)

# The Harris operator

$ \lambda_{\min} $ is a variant of the "Harris operator" for feature detection

$$ \begin{aligned}&f=\frac{\lambda_{1}\lambda_{2}}{\lambda_{1}+\lambda_{2}}\\ &\xlongequal{\quad}frac{determinant(H)}{trace(H)}\\ \end{aligned} $$

• The trace is the sum of the diagonals, i.e., trace(H) = h_{11} + h_{22}

• Very similar to  $ \lambda_{\min} $ but less expensive (no square root)

• Called the Harris Corner Detector or Harris Operator

• Lots of other detectors, this is one of the most popular

# Alternate Harris operator

• will use an alternate definition of the Harris operator:

$$ R=\lambda_{1}\lambda_{2}-k\cdot(\lambda_{1}+\lambda_{2})^{2}=\det(M)-k\cdot\mathrm{tr}(M)^{2} $$

# The Harris operator

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F7c81bbad504b4fe4aaa6b9c2819b9802%2Fmedia%2Fb4e350557dd44b92add93e955b321c55.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256024&Signature=KiDrufA9E4B0T23rzFycgcHq63s%3D)
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
Questions?
