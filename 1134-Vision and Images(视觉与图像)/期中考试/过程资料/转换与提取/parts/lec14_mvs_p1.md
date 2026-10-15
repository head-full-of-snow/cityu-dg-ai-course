![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2F56e30c0b4cdd466a8453b80492362d90.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257043&Signature=D8H3jbL7iozYQNA3yNVTsda3fL0%3D)

Multi-Camera Array

# Before: Binocular (Two-View) Stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2F4daaec01abb048a4ad6a0338f430b174.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257043&Signature=EL%2FxS7JMZ8WEpGyqWvLlg32v%2BUM%3D)

Left-right (rectified) stereo pair

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2F8b4f9f0c66cb410aa625d0edb953357d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257043&Signature=g6jdEUC7dx%2FrX%2Bp6h5InZKxyU8o%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2F8322666d573b4951a8a76134903378da.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257043&Signature=%2BIY7N6IOqkyFhJhvMvEX88Ir8FI%3D)

Computed disparity map

Useful for robot perception and navigation, video effects, etc.

# Now: Multi-view Stereo

Problem formulation: given several images of the same object or scene, compute a representation of its 3D shape

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2F0c8be0ce45054500a9f57e30c451de13.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257043&Signature=izMh1Fqv%2BnVlKEpFKBJh6QKqTiQ%3D)

Binocular Stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2F53cd7e0ce83f4ca6b9d68892e6deb85b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257043&Signature=EqcMuRcnmd1MKwOcrpaKbfG7QZ8%3D)

4

Multi-view stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2Fa2e7f409a0d44909a76acbad4e1f890e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257044&Signature=M0LpBSmlL7Educp7O83Gah8fH4s%3D)

# Multi-view Stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2F18cb7099d0f24b229d6c06b8483d819f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257044&Signature=3wdBBuOyfjpNxf8tPauEApRjQDU%3D)

Point Grey's Bumblebee XB3

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2Fed6a7ac3906d4bd2a5b5eb19aef15e37.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257044&Signature=sbSTyBG3UGr%2BeLX0qaloHSQOTLA%3D)

Point Grey's ProFusion 25

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2Fecdc8f7a0b0b45789f98edf09237406e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257044&Signature=FNA44dXg6dniZ0S613gK9dvcHzE%3D)

CMU's Panoptic Studio

# Multi-view Stereo

Input: calibrated images from several viewpoints (known intrinsics and extrinsics / projection matrices)

Output: 3D object model

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2Fc3eae2d251234752a5d33e73d2db1e37.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257044&Signature=f4ulZIINhClkzY3aCPuJqJJ5jNo%3D)

Figures by Carlos Hernandez

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2Fb27f752110244d7cb4856d6a44e9b510.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257044&Signature=OeFMuVneec3EN6Z2tbkkYTry0Hw%3D)

We'll talk more about how to calibrate multiple cameras soon

# Applications

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2Fc577e670f35a42598e7a70f9bda14176.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257044&Signature=zo55aQujbX%2BnxucjnXAqCMTLoe8%3D)

Details Los Angeles County Museum of Art

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff8060ae9eafa40f7940bb89fb4f4c625%2Fmedia%2F8c1fe0a1a315448ab43a1f6c8cb7033b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799257044&Signature=Prq01%2BDG2EY6fsPlG91KKqtHB4w%3D)

Los Angeles County Museum of Art

Sculpture

Share

Compare
