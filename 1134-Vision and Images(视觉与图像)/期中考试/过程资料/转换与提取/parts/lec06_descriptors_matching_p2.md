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
