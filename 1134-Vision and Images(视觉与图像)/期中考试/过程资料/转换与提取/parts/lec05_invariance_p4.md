# Find local maxima in 3D position-scale space

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa850a02731ed4034ba633f2415269e41%2Fmedia%2F52673ae6007a488294579dc03cdda7e6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256194&Signature=2cNpx3N1DNOy6BjWiQZlLfalvDw%3D)

K. Grauman, B. Leibe

# Scale-space blob detector: Example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa850a02731ed4034ba633f2415269e41%2Fmedia%2Fb7698074fef340a39730b9d47c4e8190.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256194&Signature=c6DqpCjyP0WkZkALyI55u5aF5Vg%3D)

# Scale-space blob detector: Example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa850a02731ed4034ba633f2415269e41%2Fmedia%2Faea86c4901564386a7cac7c3a0c59c93.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256194&Signature=8WtMU3NHnEaRYL045mtNhiKXSKI%3D)

$ \sigma = 11.9912 $

# Scale-space blob detector: Example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa850a02731ed4034ba633f2415269e41%2Fmedia%2Fc414f37dccf64ef5bfef5eeacc77f32e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256194&Signature=PTKlC9v2F2yTX5ervwjZUwa45oI%3D)

# Scale Invariant Detection

• Functions for determining scale

Kernels:

$$ \nabla^{2}g=\frac{\partial^{2}g}{\partial x^{2}}+\frac{\partial^{2}g}{\partial y^{2}} $$

(Laplacian)

$$ DoG=G(x,y,k\sigma)-G(x,y,\sigma) $$

(Difference of Gaussians)

where Gaussian

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa850a02731ed4034ba633f2415269e41%2Fmedia%2F9bdef5ae558c4bab90664b8e381c950d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256194&Signature=jxcTb%2FeRAZG5UAfBpir58IVSALk%3D)

$$ G(x,y,\sigma)=\frac{1}{2\pi\sigma^{2}}e^{-\frac{x^{2}+y^{2}}{2\sigma^{2}}} $$

Note: The LoG and DoG operators are both rotation equivariant

Questions?

# Feature descriptors

We know how to detect good points

Next question: How to match them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa850a02731ed4034ba633f2415269e41%2Fmedia%2F2c4731deb5f942d79eeedd26e8827bbf.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256195&Signature=Vn0h9U3gfyI74HncjuD%2BcCCdVK4%3D)

Answer: Come up with a descriptor for each point, find similar descriptors between the two images
