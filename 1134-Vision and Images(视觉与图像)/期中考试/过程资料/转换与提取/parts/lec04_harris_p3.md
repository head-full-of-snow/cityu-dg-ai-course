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
