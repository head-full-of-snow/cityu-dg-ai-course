# CS5187: Vision & Image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2Fb79a2de745fa46288d81a4003441022a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256112&Signature=zkmMGb5sS0S0z6UnDPOe0zbziDg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F443ebf7c4af9423eb6142553c431abc3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256112&Signature=AsjAKr3SGvs52Cd1IC9zaHAdQuc%3D)

# Local features: main components

1) Detection: Identify the interest points

2) Description: Extract vector feature descriptor surrounding each interest point.

3) Matching: Determine correspondence between descriptors in two views

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2Fac333797bda84a9e8f2ae5e28c20ad38.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256112&Signature=0%2Bp0oHjltBB7Sfn2cpLXCJ2TTbw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F4a13e68c1616451f9771315cac6195c7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256112&Signature=Y%2Fy0h7jbBhYZK%2Bf6IQwCL7wPEL0%3D)

$$ \mathbf{x}_{2}^{ 徳 }=[x_{1}^{(2)},\ldots,x_{d}^{(2)}] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F931e1f651d6c488587bb88cd637d7764.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=%2FJzs3cXfXC82D%2Fl2f9rr88a9zQQ%3D)

# Harris features (in red)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2Fc1782a09439f41efaaa16f80effd4733.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=Gzaa7vFkUWWtcpzL01MjtcPGrpI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2Fc8457d0d5f0a4a64a204e2f42dc99f09.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=XO1gv3dhBHA6zOIyMwb%2B5ihz3%2FA%3D)

# I mage transformations

• Geometric

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2Feba3de7319b54679aa5bff8f12d92988.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=QCwG%2BK2IAZRy%2BC1P8KKN7OeaSFU%3D)

Scale

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F752242ada17a44c78169b4c738abd54a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=2sndkMSXBZH19wvZYLH5diA8hvo%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F44ee172d0891408aa75d5958e176d2f8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=%2B7viWZR2egmBwBdhwWUOf4OVKNc%3D)

# I nvariance and equivariance

- We want corner locations to be invariant to photometric transformations and equivariant to geometric transformations

– Invariance: image is transformed and corner locations do not change

– Equivariance: if we have two transformed versions of the same image, features should be detected in corresponding locations

– (Sometimes “invariant” and “equivariant” are both referred to as “invariant”)

– (Sometimes "equivariant" is called "covariant")

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F9cc5a8190c174295a6fb2c5e3579c2a1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=RkdA2SmjQ29i4%2FIUjIIo9SHUUl0%3D)

# Harris detector invariance properties: image translation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F7cf6335d30cf47c1bc5fb6bc2a4a89e2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=3y0GoV98ZRzH1I1GyuKMwVjqYsE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2Fe3393374b9f446b899301d76c111e196.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256113&Signature=yd5DNeRe52wWT%2BlAUJCKQ8WKK9k%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2Ffa5190e5ef564916a504dc409688211c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256114&Signature=27s5fr1AjV9vKak2VZm%2F%2B3mqItU%3D)

• Derivatives and window function are equivariant

# Harris detector invariance properties: image rotation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F531ead7bcb3440599c5dc67da48ae321.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256114&Signature=ESN7GCkbpKxfrC8pvo8xYIJ58aU%3D)

Second moment ellipse rotates but its shape (i.e. eigenvalues) remains the same

# Harris detector invariance properties: Affine intensity change

$$ \boxed{\quad} $$

$$ I\rightarrow a I+b $$

• Only derivatives are used to compute Harris scores →

invariance to intensity shift  $ I \rightarrow I + b $

• Intensity scaling:  $ I \rightarrow a I $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2Ff379b304c5684fcda0acea525bcdb6cb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256114&Signature=pPaYxpXW3lmlTPkTB39g%2Bu7t3TY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F65d889d326984d99af2f05323cecd49b%2Fmedia%2F8bc1cab61e1c44e59c3040cd2f6bdc56.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256114&Signature=junBLUYAJC51FTBgGaFy1wjPYIc%3D)

Partially invariant to affine intensity change
