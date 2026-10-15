Prof. Zhu Zhiyu

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2Fd2eed77879154faa81090774729a0751.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256219&Signature=kyemMjQ6wnoRyZqrYLW5%2BquerGE%3D)

# Local features: main components

1) Detection: Identify the interest points

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2Fb427b4b65f5841b7a5bc81f9f7d42226.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256219&Signature=26RuUAlZ8ZjTuJGrgNEoVXjcanE%3D)

2) Description: Extract vector feature descriptor surrounding each interest point.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2F84866d478571497e8e18060cb65dafc5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256219&Signature=DJuPNc7Qkko2jIbTog4Zke3Kmpk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2F1acef102383b4a1298c48e25ed3dee16.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256224&Signature=F6NhIQYD6A24RG%2FLuix7EvoHMKY%3D)

3) Matching: Determine correspondence between descriptors in two views

$$ \mathbf{x}_{2}^{\downarrow}=[x_{1}^{(2)},\ldots,x_{d}^{(2)}] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2Fd6e3a232c25d4547b2d8f63735e98d5e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256224&Signature=mINbmvk3JWSyIeWZZ6RM5a79SVw%3D)

# Review of the last lecture

The surface  $ E(u,v) $ is locally approximated by a quadratic form.

$$ \begin{array}{r l r}{E(u,v)}&{\approx}&{A u^{2}+2B u v+C v^{2}}\\ &{\approx}&{\left[\begin{array}{l l}{u}&{v}\end{array}\right]\left[\begin{array}{l l}{A}&{B}\\ {B}&{C}\end{array}\right]\left[\begin{array}{l}{u}\\ {v}\end{array}\right]}\\ &{}&{\underbrace{\quad\quad\quad\quad}_{A=\displaystyle\sum_{(x,y)\in W}I_{x}^{2}}}\\ &{}&{H}\end{array} $$

$$ B=\sum_{(x,y)\in W}I_{x} I_{y} $$

$$ C=\sum_{(x,y)\in W}I_{y}^{2} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2F4ab785ec7d5f465e860b99b3c421bd67.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256224&Signature=6lNSQHcgZw2KQphs7KGahM8y7xM%3D)

Let's try to understand its shape.

# Review of the last lecture

We can visualize H as an ellipse with axis lengths determined by the eigenvalues of H and orientation determined by the eigenvectors of H

Ellipse equation:

$ \lambda_{\max}, \lambda_{\min} $ : eigenvalues of H

direction of the

fastest change

$$ \left[u\quad v\right]\quad H\quad\begin{bmatrix}u\\ v\end{bmatrix}=\mathbf{const} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2F4e9c5fd1203c4aa9bd29e66275f1d3b1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256224&Signature=aIHkwnB8D9C%2BPn1ZmG8GD2R%2FPAU%3D)

direction of the

slowest change

# Feature descriptors

We know how to detect good points

Next question: How to match them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2Fb74de0c1a9ce4737a41f7b113f7f416c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256224&Signature=XUnwRfGlEO7i7MWB5i1WyIhaT14%3D)

Answer: Come up with a descriptor for each point, find similar descriptors between the two images

# Feature descriptors

We know how to detect good points

Next question: How to match them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2Fb8ca614e385e406fbadfe60927bd6eea.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256225&Signature=3RsjdRmTKsRK6KVVrgiDZeiyIJM%3D)

# Lots of possibilities

– Simple option: match square windows around the point

– State of the art approach: SIFT

• David Lowe, UBC  $ \underline{\text{http://www.cs.ubc.ca/~lowe/keypoints/}} $

## I nvariance vs. discriminability

• Invariance:

– Descriptor shouldn’t change even if image is transformed

• Discriminability:

— Descriptor should be highly unique for each point

# I mage transformations revisited

• Geometric

Rotation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2F652cf71ae6ac4147913eda083e03b3f0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256225&Signature=fY1RhBpvIP%2B7HuKqQX9s%2FuHmrbc%3D)

Scale

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2F5ca5d07cfa434e538f45bfcb94359be4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256225&Signature=A9HIPj3Fuadnm8luR4kLwJ175Ts%3D)

Intensity change

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0e3d906e0ef74ca7ab1fa25174d1dfb6%2Fmedia%2F15de57d2ec8f4a94a5d58a341b98b9ca.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256225&Signature=ox249BNv%2FcZm9dVNefnDPLbuAZA%3D)
