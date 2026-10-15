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
# I nvariance

Suppose we are comparing two images $l_{1}$ and $l_{2}$

− I₂ may be a transformed version of I₁

– What kinds of transformations are we likely to encounter in practice?

# I nvariant descriptors

• We looked at invariant / equivariant detectors

• Most feature descriptors are also designed to be invariant to:

– Translation, 2D rotation, scale

# • They can usually also handle

– Limited 3D rotations (SIFT works up to about 60 degrees)

– Limited affine transforms (some are fully affine invariant)

— Limited illumination/contrast changes

# How to achieve invariance

Need both of the following:

1. Make sure your detector is invariant

2. Design an invariant feature descriptor

— Simplest descriptor: a single 0

• What's this invariant to?

– Next simplest descriptor: a square, axis-aligned 5x5 window of pixels

• What's this invariant to?

— Let's look at some better approaches...

# Rotation invariance for feature descriptors

• Find dominant orientation of the image patch (this orientation should be equivariant to image rotation)

– E.g., given by  $ \mathbf{x}_{\text{max}} $, the eigenvector of the second moment matrix  $ \mathbf{H} $ corresponding to  $ \lambda_{\text{max}} $ (the larger eigenvalue)

– Or (better) simply the orientation of the (smoothed) gradient

– Rotate the patch according to this angle

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2F0d0ea121484340d4b8c315bd9ab02f46.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=tiC1KEr5fOawpUqEk1Pp5YwRRWw%3D)

Figure by Matthew Brown

# Multiscale Oriented Patches descriptor

Take 40×40 square window around detected feature

– Scale to 1/5 size (using prefiltering)

— Rotate to horizontal

Sample 8x8 square window

centered at feature

Intensity normalize the window by subtracting the mean, dividing by the standard deviation in the window (why?)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2F54a6b1a3b4a147aab1d6bf7512b7d75a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=TjIgmoClCJxGuy00Mbv7GqZXlO0%3D)

# Detections at multiple scales

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2Ff3c78521152e4919b6ff27565ac46058.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=y8Gb2tzjAHiTwvZyyVCDk0rT3Ms%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2F5c347aba63d84dbfb038f8595736eca3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=pQ2S2njndQir%2FF43nIPreAsMdvY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2Fef4c020a408c4f1f813838be55c71f80.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=nCpCIRINW%2B9JQ3U7WR9vS7Wv4%2B0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2F7ea20bf1f29a4b2ea33e1b9e578443e6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=Ai7jtaNIXwywPGTjto5aCkDLXD4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2Fbb2bf629b80e4a5d80f9bc882b394e6b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=PIxirnmYHxPS5%2BzBYRi9mCElKkc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2F7aedc2cd569546beb60ab2a7500c3b3d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=Qk%2B96SrCLZ14pN4Gaa44l549uUs%3D)

Figure 1. Multi-scale Oriented Patches (MOPS) extracted at five pyramid levels from one of the Matier images. The boxes show the feature orientation and the region from which the descriptor vector is sampled

# Scale Invariant Feature Transform

Basic idea:

• Take 16x16 square window around detected feature

• Compute edge orientation (angle of the gradient - 90°) for each pixel

• Throw out weak edges (threshold gradient magnitude)

• Create histogram of surviving edge orientations

• Shift the bins so that the biggest one is first

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2F054f788e2b1e4e5fa42b21182377da32.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256246&Signature=Y9xI4uwlQEI%2BQAK%2B9kxHAuDSAyc%3D)

# SIFT descriptor

Full version

- Divide the 16x16 window into a 4x4 grid of cells (2x2 case shown below)

• Compute an orientation histogram for each cell

• 16 cells * 8 orientations = 128 dimensional descriptor

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Faaeca9f3995848cb98c4914a8a1d3265%2Fmedia%2F90dad015a224464b98b273af3c7f6ea3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256247&Signature=4X91HCOZRYAf49FKxgK6jhmWAcE%3D)

Image gradients

Keypoint descriptor
# Properties of SIFT

Extraordinarily robust matching technique

– Can handle changes in viewpoint (up to about 60 degree out of plane rotation)

– Can handle significant changes in illumination (sometimes even day vs. night (below))

– Pretty fast—hard to make real-time, but can run in &lt;1s for moderate image sizes

— Lots of code available

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F27af0cf4c66b4791bdb627a1d8510b8a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256270&Signature=1LPx0aLoSeMliy%2FC1jk8ICmo4JQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F0aa8c2fb505c4aadb0830ea80e4b0cc2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256270&Signature=1NAvaE6ueE177K9Lz5uNqRxXo7k%3D)

# SIFT Example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F83754616fa3d44fc93b0f0e32e8c4f94.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256270&Signature=aJzFlDkv%2F7ojucWe2Va8tuIRsis%3D)

sift

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F4c2e3fbe57d54249b37c222702405008.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256270&Signature=XhVezWARHsgpBdJMGOdbRYfMxvQ%3D)

868 SIFT features

# Other descriptors

- HOG: Histogram of Gradients (HOG)

- Dalal/Triggs

– Sliding window, pedestrian detection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F9ab249c18d8f43e8812f982f81776ca6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=D90PFT184r94LV42US581du7w8g%3D)

• FREAK (Fast Retina Keypoint) or ORB features

— Can run in real-time; used in Visual SLAM on-device

# • LIFT: Learned Invariant Feature Transform

– Learned via deep learning – along with many other recent features

https://arxiv.org/abs/1603.09114

# Other descriptors

# • HOG: Histogram of Gradients (HOG)

– Dalal/Triggs

# – Sliding window, pedestrian detection

1. Gradient Computation

- Compute horizontal and vertical gradients using  $ [-1, 0, 1] $ filters

- Calculate gradient magnitude and orientation at each pixel

2. Cell Histograms

- Divide image into small cells (e.g., 8×8 pixels)

- Create histogram of gradient orientations (typically 9 bins, 0-180°)

- Weight votes by gradient magnitude

# 3. Block Normalization

- Group cells into overlapping blocks (e.g.,  $ 2 \times 2 $ cells)

- Normalize histograms within each block (L2-norm)

- Provides invariance to illumination changes

HOG: Histogram of Oriented Gradients Process

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F925ef294d9784e1c87128d3732fb16e4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=8aopp4ODuyHD8Or3CX97IKzsMks%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F0e5b97335859474295f3ce3407f3d23a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=bAXw%2By90ZPrOF%2BD4OPMzY1RZf9M%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F26e97af49cc440328eee09417cd964ff.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=5N9TqHGSFf%2FFGaJ%2BO0Ks69fcJ%2BE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2Fdcd26044ea484a8ab54a88d3e07d66b3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=sz%2FLPNt1TCqBVk1XJUGNqeexfZg%3D)

**Other descriptors**

**• FREAK (Fast Retina Keypoint) or ORB features – Can run in real-time; used in Visual SLAM on-device**

1. oFAST: Oriented FAST Keypoint Detection

- Uses FAST corner detector to find keypoints

- Computes intensity centroid to determine orientation

- Applies Harris corner measure to rank keypoints

2. rBRIEF: Rotated BRIEF Descriptor

- Binary descriptor: compares intensity of pixel pairs

- 256 bits (256 binary tests)

1. FAST Corner Detection

- Rotates sampling pattern according to keypoint orientation

ORB: Oriented FAST and Rotated BRIEF

2. Orientation

Estimation

- Uses learned sampling patterns for better performance

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2Ffb58f5c53c664272a4cdef66d6b6fc64.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=liMhmbqFfjHP30kO5sYcqAElwow%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2Fc64662bb69074889a58a71cf415aa07d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=XQ4Fk5xCiNNciHAl9uJ%2BrxSDTEM%3D)

3. BRIEF Binary Tests (256 pairs)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2Fc61775117f4043be9d46f626307e3e4b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=sJqovhdYZwrIB%2FI%2BcellC2yza%2B0%3D)

Questions?

**Summary**

• Keypoint detection: repeatable and distinctive

– Corners, blobs

— Harris, DoG

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F3dbc594c85b14082b4bf4cba977236e8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=cTP840%2Fb9GT8%2FiZ6XnPDGt9PfAc%3D)

**• Descriptors: robust and selective**

– spatial histograms of orientation

– SIFT and variants are typically good for stitching and recognition

— But, need not stick to one

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F330d13e556ed44e6b7243033bca69b78.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256271&Signature=4Q4AbONFPFWoi9kY%2FrcLQ6NDpBU%3D)

**Which features match?**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F67ab6807397e4e9b98ab3f74d369d5c8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256272&Signature=gtpGkeUtG0mOAk7Y2Q7EEVj6pKU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fdbd9934276e544779cba5e5a62894448%2Fmedia%2F208850fe9b7a4b5e949e40e43d4a7147.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256272&Signature=aVoTqi%2BmBjjLGaC0poeDKvZgCZ4%3D)
# Feature matching

Given a feature in  $ I_{1} $, how to find the best match in  $ I_{2} $?

1. Define distance function that compares two descriptors

2. Test all the features in  $ I_{2} $, find the one with min distance (can be accelerated with a nearest neighbors search data structure, like a kd-tree)

# Feature distance

How to define the difference between two features  $ f_{1}, f_{2} $?

– Simple approach:  $ L_{2} $ distance,  $ \parallel f_{1}-f_{2}\parallel $

— can give small distances for ambiguous (incorrect) matches

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F92348dcba45c43f8ada8d96e299a1d0d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256298&Signature=ddhsSbXZArWJDfvg6A6a9XNk3w8%3D)

$ I_{1} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2Ff8111082a868406f8c53c116ebe476d4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=oUnT5ROXaXQxd9o646m9BQE849Q%3D)

$ I_{2} $

# Feature distance

How to define the difference between two features  $ f_{1}, f_{2} $?

• Better approach: ratio distance =  $ \left\| f_1 - f_2 \right\| / \left\| f_1 - f_2' \right\| $

•  $ f_{2} $ is the best SSD match to  $ f_{1} $ in  $ I_{2} $

•  $ f_{2}^{\prime} $ is the  $ 2^{nd} $ best SSD match to  $ f_{1} $ in  $ I_{2} $

• gives large values for ambiguous matches

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F86aaadc80ae0413f96d43c9aa08c2de1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=NyqJoGjc%2BiOWLN7icPbdeZI5wxk%3D)

$ I_{1} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F7523c2cca2cf499aa54aa9ae41b24ead.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=Uv94lhiGhPHoaE3BrVTEmmBNH9U%3D)

$ I_{2} $

# Feature distance

• Does the SSD vs "ratio distance" change the best match to a given feature in image 1?

• No, but it changes the distance, and it can change the ordering of matches from good to bad

• After we compute a set of matches, we threshold by distance (that is, throw out matches with distance > threshold)

# Feature matching example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2Faa17d4332d9b4b3793be8797c006135d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=gwo0bcmaVPAa3gFv2LYG53ZZ4eU%3D)

58 matches (thresholded by ratio score)

# Feature matching example

We'll deal with outliers later

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F5e0a915bed574c2aaf0027a92661eb4a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=sA8x7fKUsoG4OGhCTASFBXgVlTQ%3D)

51 matches (thresholded by ratio score)

# Evaluating the results

How can we measure the performance of a feature點選擇?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F934f845156ef4cfa966e9af58f5dd6fb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=K4YJXNrxp0iZJMHCQDsV6SF7e9c%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F5f6d8832f2d6452a874371334e9bc18c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=hM%2FW7AODLnoL4geT3hn9fmISQng%3D)

feature distance

# True/false positives

How can we measure the performance of a feature點選擇?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F7715dbe704984c06b919a34c9fbfd378.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=6DfLlCTv5EqbLKYS5q6oyGl2ZCo%3D)

feature distance

The distance threshold affects performance

– True positives = # of detected matches that survive the threshold that are correct

– False positives = # of detected matches that survive the threshold that are incorrect
# True/false positives

How can we measure the performance of a feature點選擇?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2F05fe872cfaad450f8a49b345fc3643d3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=ReIXxtFT4wEJLL65En%2FixLVB7SI%3D)

feature distance

Suppose we want to maximize true positives. How do we set the threshold?

(Note: we keep all matches with distance below the threshold.)

# True/false positives

How can we measure the performance of a feature點選擇?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2F4943cf6b793e49e2bfc8f5da7bbb3343.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=0ndXUC%2FNl2AZ%2BmHpTfYC3d5jVoI%3D)

feature distance

Suppose we want to minimize false positives. How do we set the threshold?

(Note: we keep all matches with distance below the threshold.)

# Example

• Suppose our Matcher computes 1,000 matches between two images

– 800 are correct matches, 200 are incorrect (according to an oracle that gives us ground truth matches)

– A given threshold (e.g., ratio distance = 0.6) gives us 600 correct matches and 100 incorrect matches that survive the threshold

– True positive rate = 600 / 800 =  $ \frac{3}{4} $

– False positive rate = 100 / 200 =  $ \frac{1}{2} $

# Evaluating the results

How can we measure the performance of a feature點選擇?

# true positives surviving threshold

# total correct matches (positives)

recall

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2F010dfb3014c6439fb6571ad116553136.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=vF3qkLyjXyao0rW3hBww611vnYY%3D)

# Evaluating the results

How can we measure the performance of a feature點選擇?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2Fcb7caf5c89924880a31a23f438c9a07f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=OP09i1ig4wVx%2FVOC3%2FaT1qDWtoo%3D)

# ROC curves – summary

• By thresholding the match distances at different thresholds, we can generate sets of matches with different true/false positive rates

- ROC curve is generated by computing rates at a set of threshold values swept through the full range of possible thresholds

• Area under the ROC curve (AUC) summarizes the performance of a feature pipeline (higher AUC is better)

# Lots of applications

Features are used for:

– Image alignment (e.g., mosaics)

– 3D reconstruction

– Motion tracking

— Object recognition

– Indexing and database retrieval

– Robot navigation

- ... other

# Object recognition (David Lowe)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2F197e53de58514c15a1cc5b349edb3892.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=fCBFbY4gJf21lcSJJ9F12DbnVqo%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2Fdeba4aa7ec2141a98e270f29c0b1c6e4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=50VGXTQpg5q%2BbU06AHwiFNmFvbE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2Fbb4ba40c4f95426cb1174248ce7bfd1c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=ZB77NySHhtHk75fWf2U8pXoTC2o%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2F321fdf3278c142bbbc0424ca11a0b408.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=H23L5s2zV0R9RxJ%2B4sxv3%2Fupxas%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2Fdd3f794825a84e0ab3f467d2e2ca26c2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256321&Signature=hGdHtV2kchuYbYbhRC%2FuvbU%2BJ8M%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2F5b8a67c8deb745e5ad25cdf82133060a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256322&Signature=0jYPu7BC%2BeYAh%2B4AKZU4WTx6XMk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fbb43916544804a12907df0881c11c708%2Fmedia%2Fead49acda66042e9948fd905e48db96b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256322&Signature=WQiLNBAHbhtlhpMcVdQxA%2BZ1bVg%3D)
# 3 D Reconstruction

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F54eb321ce6214ff7be6f2f0f737c0ebe%2Fmedia%2F6b222f85adbc4eb4adcc001dc0d39036.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256339&Signature=wW%2BFS9Z6qZFyWW4F6hk06H5vzyw%3D)

Internet Photos ("Colosseum")

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F54eb321ce6214ff7be6f2f0f737c0ebe%2Fmedia%2F1387348b836d422097bce9e78ef6a1fc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256339&Signature=nJs3nhNlmacYN91%2FGUq%2FogkD8mE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F54eb321ce6214ff7be6f2f0f737c0ebe%2Fmedia%2F3374379631934e43854bdc37d89d3d52.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256339&Signature=4APn2U%2F2yUmo06iQbpXN2cpDfg4%3D)

Reconstructed 3D cameras and points

**WildGaussians: first reconstruct cameras using feature matching, then create dense model**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F54eb321ce6214ff7be6f2f0f737c0ebe%2Fmedia%2Fa16e664434d3408e9436e0b34b6fa05e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256339&Signature=jcZqxM8ebP1wiD%2BHP3YrKR%2F1QEA%3D)

Kulhanek, et al. WildGaussians. NeurIPS 2024

**Augmented Reality**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F54eb321ce6214ff7be6f2f0f737c0ebe%2Fmedia%2Fd86112cf1d6c4dc2ac10a58fc5db7fc7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256340&Signature=tZrVLXeZyotHwuAva7K%2FCbqmbr8%3D)

**Learned feature matchers**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F54eb321ce6214ff7be6f2f0f737c0ebe%2Fmedia%2F0eda67cd7ac145889e483361709c8e83.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256340&Signature=tK4OZt8jMkRluBUQC6MBJJ6MeGQ%3D)

LoFTR: Detector-Free Local Feature Matching with Transformers

CVPR 2021 [Sun, Shen, Wang, et al.]

**Learned feature matchers**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F54eb321ce6214ff7be6f2f0f737c0ebe%2Fmedia%2Fad21a97313da4b32956e4bff31ca350c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256340&Signature=ywMDESxLunpJ9xO1ufkyvPXRs70%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F54eb321ce6214ff7be6f2f0f737c0ebe%2Fmedia%2F25f275ea7e934b28afeed4facbe2323f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256340&Signature=ncyyIwp3%2FpTjKQgrnafo0xYHU6c%3D)

RoMa: Robust Dense Feature Matching, CVPR 2024

Questions?
