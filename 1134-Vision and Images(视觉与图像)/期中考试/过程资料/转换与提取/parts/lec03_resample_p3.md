![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2Fa3699ba5e62d4be697d1c89ec97684ab.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255840&Signature=y8i27HyczMDMmwbbJzvzMnzmg2Y%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2Fdbdfa1641f114a449dd0a98c755cc6e7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255840&Signature=VUJInbiwA8OVW5duJ%2B3%2Fomp0Cis%3D)

# Gaussian pyramids [Burt and Adelson, 1983]

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2F3466ccec0719485daf36563dd5b814a0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255840&Signature=HVzZ69tNzaQK8tKKsHWUucP8qDc%3D)

• In computer graphics, a mip map [Williams, 1983]

• A precursor to wavelet transform

Gaussian Pyramids have all sorts of applications in computer vision

# Gaussian pyramids [Burt and Adelson, 1983]

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2F38c73653158f47e485c01a79816cc361.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255840&Signature=XmTVuMW5LNVFzJ7hvjDk12RUgBQ%3D)

Q: How much space does a Gaussian pyramid take compared to the original image?

# Gaussian pyramid

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2F2343f0427cfe4f32bade0b97625abf59.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255841&Signature=hDQDmMIIKkz1fuzyA4kscwuIff4%3D)

# Gaussian pyramid

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2Ffd0d1505fc0b4c92a2833ba833760c17.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255841&Signature=9m4VVDk9zc5pSgcd4RAEJRJgyYc%3D)

Answer: 4/3 the amount of space as the original image alone

See  $ \underline{\text{https://en.wikipedia.org/wiki/Geometric_series}} $

# Back to the checkerboard

• What should happen when you make the checkerboard smaller and smaller?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2F5d5509ef86044e11876c826360c028fb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255841&Signature=Ub3%2FzrsKpC0qfOFv7we7vzJSov4%3D)

Naïve subsampling

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2Fd7a7414f976047b88438d41d1fad0263.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255841&Signature=VfZBPbm1M1FJ2AztbehCcYQ%2BtS8%3D)

Proper prefiltering ("antialiasing")

Image turns grey!

(Average of black and white squares, because each pixel contains both.)

Questions?
