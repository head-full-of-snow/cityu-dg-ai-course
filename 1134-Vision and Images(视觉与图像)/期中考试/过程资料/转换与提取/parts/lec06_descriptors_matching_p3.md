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
