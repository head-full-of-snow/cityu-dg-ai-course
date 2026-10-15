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
