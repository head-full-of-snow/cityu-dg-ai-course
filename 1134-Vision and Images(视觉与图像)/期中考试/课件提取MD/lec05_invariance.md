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
# Harris detector invariance properties: scaling

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2Ff78bd25c787d495299200ad964b23d46.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256136&Signature=88Er%2FIy4VZbtf%2F5swCZwjBSj5Kw%3D)

# Scale invariant detection

Suppose you're looking for corners

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2F442345e2465a4cf8bc9bb81f5835f997.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256136&Signature=s00z2bzLio4JM3%2F16FGfpZ26THU%3D)

Key idea: find scale that gives local maximum of f

– in both position and scale

– One definition of f: the Harris operator

Lindeberg et al., 1996

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2Fe611491799aa4b79a189cdf6bd7f750f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256136&Signature=ROi%2B%2Boo6sIexdtURtwfkaEZmaQk%3D)

# Automatic scale selection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2F54f38adf7f814a77af38d41d4778ea25.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256136&Signature=GUTglzrbgXVEEF9ZWvK6H2wCUy8%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2F90b2a28815a843eab5fd7d140b0d1c72.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256136&Signature=1eNGwoKQkiKDl9PJoZjStG8Z%2BM4%3D)

# Automatic scale selection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2F7677532f0d534532b241ecdd28c0e4e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256136&Signature=yWS9M8CUWwkJ74XMIU7jeVjayDk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2F695dada7bbd9467fad1be182b4ab86e7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256136&Signature=%2BN%2BhHxogh67NNzCa9DVg85I%2BzJs%3D)

# Automatic scale selection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2F93291848024a41638eaa5f7594c9b142.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256136&Signature=or8qonTTbtyciz1Wh0%2B3aEbHr3w%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2Fad7cd60b3f75460cb156f62d9eb399f3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256137&Signature=Kys79bP9g%2BaN7F9zufZyYVKoOBw%3D)

# Automatic scale selection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2Fd60886dd0fd745e7a793e3609b99a494.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256137&Signature=Q1wWdNh42OcQZJBAeUVN%2Fjb9SEg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2F93cb676a6392462399bac19ba4fc0abc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256137&Signature=IhdugptmUyBQOEmixwN3M9hg0Eg%3D)

# Automatic scale selection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2F044e2c1ef2a748659808ea38f922a43e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256137&Signature=xHw7QMeObjURFaUhSz5rlzvbb9Y%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8d5a99f4dd0c42879845885798d18d82%2Fmedia%2Fe2e425d3ec014bbe9933984dbbe53a3d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256137&Signature=%2BD3z7mYCJd3%2FdsXlAt2AOAjqqGI%3D)

f ( I i , , i , n ( x , σ ) )
# Automatic scale selection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fc1157efd7ba34e89bfad8ce1822718c2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256160&Signature=8zfXZCM8DCcYltKwk%2B%2BhfyDxucw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F1cf09c77424b4cf188444357e7dbf783.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=p7vU2JuG6F5PaOVF%2BvW6%2BeMmOjQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F735640d2c3b54de1abb5a5a53ebdfb22.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=NVT1ngvzm2V2jRUcR4uzhlnxjYE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fc749e72fceab40ffafa8586df28a44af.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=PMr0qaMIntXXQ02VIS8jzeLYTnw%3D)

# Automatic scale selection

Normalize: rescale to fixed size

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fc86beb9d12064114a0343723a0522354.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=734nVDhPbshzRU9rbmDxIIKvRaw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F268c3b656a4e461a9d49a573e440657a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=iXc1kO6ujpTjPx38v9m2DBGyMyc%3D)

# I mplementation

• Instead of computing f for larger and larger windows, we can implement using a fixed window size with a Gaussian pyramid

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F7a77a3765c474811bff2255490c56a4e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=fuyQmbxaBbYgipULOqGNhpfZ05k%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fd3463dc99bab43989fde08655daff8d9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=ybZObIVUQ4mPHL2wJtTSjHQ4wgk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fa65aedb4eba046f2a44da79248919660.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=tH7r%2FVHqM2qBo%2FFNN0QoDYw1IM8%3D)

(sometimes need to create in-

between levels, e.g. a  $ \frac{3}{4} $-size image)

# Feature extraction: Corners and blobs

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F679b2f57538849a3b914ea63fb7a3da1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=wsx85dFrqX1UmxzyWAYfoVrTeWc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F00bccc04e54b4536a41a2144cf7ae6ee.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=p7j9VhrQxbkUcTIynjhueoWaNrM%3D)

# Another common definition of f

• The Laplacian of Gaussian (LoG)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F1e3c3362891b4cd687b3377f38036c83.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=nYo0MRbAtdZ62SAv6GGXRNBytH0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F6fc8efefcda9446daf8f476f76eabadf.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=jAcsvMIcMB2YSTY0OnwGfAH1Sdo%3D)

$$ \nabla^{2}g=\frac{\partial^{2}g}{\partial x^{2}}+\frac{\partial^{2}g}{\partial y^{2}} $$

(very similar to a Difference of Gaussians (DoG) – i.e. a Gaussian minus a slightly smaller Gaussian)

# Laplacian of Gaussian

• "Blob" detector

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F3c09571be1b34de2824e3367833cb7c1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=Fg4eCAVu5EVk7xGaO1xevh5CddY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F266f8d706ffb4a53a980d3f2a5482eb5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=%2BrVS8wp0gw0diBjVEpnxlp08JrQ%3D)

• Find maxima and minima of LoG operator in space and scale

# Scale selection

• At what scale does the Laplacian achieve a maximum response for a binary circle of radius r?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fd6745b96873040cb84684b0f7c42f363.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=Zin8nIweZt6%2B7v3u%2Fhkn9g3bTb4%3D)

image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F6302c22048f14bd281ab4a38e9bb0a1a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256172&Signature=QAj25osSMqkyvaWrTyNcGt5SrQ8%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F4b5f301d77e24212aa034fcbee828696.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256172&Signature=RuiNgWxKQsfUd4cPZ9YsWQ28bog%3D)

Laplacian

# Characteristic scale

• We define the characteristic scale as the scale that produces peak of Laplacian response

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fa6449ff891144eac872caaaf43d9d8bc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256172&Signature=O7kY7fEWOMkRKb%2FpyDlvN%2B3%2BTmM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fe38ecf74dba9460ba6bc6d1b92a84649.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256173&Signature=viR2%2B12bXrXGn1l3%2BGCXUC0iXxk%3D)

T. Lindeberg (1998). "Feature detection with automatic scale selection." International Journal of Computer Vision 30 (2): pp 77--116.
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
