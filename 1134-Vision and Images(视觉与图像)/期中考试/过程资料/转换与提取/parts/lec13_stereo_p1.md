# CS5187: Vision and Image

Binocular Stereo

What is this?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2Faecd13266e2d4132bab64524a6edf5cc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256883&Signature=WWTmsl0UhuE%2BM0gkz8Yv4jpeZs0%3D)

Single image stereogram,

https://en.wikipedia.org/wiki/Autostereogram

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2Fe0099907dddc4f94a4a46936449ec9f1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256883&Signature=oTsBnouESPNBQuvo9bep%2FqhJXJ0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2F918f3cf79be54d05961086ca6a710e4e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256883&Signature=P4Ap2ZV%2FHliDN0l5nFSVD9T6Xpk%3D)

https://giphy.com/gifs/wigglegram-706pNfSKyaDug

# Stereo Vision as Localizing Points in 3D

• An object point will project to some point in our image

• That image point corresponds to a ray in the world

• Two rays intersect at a single point, so if we want to localize points in 3D we need 2 eyes

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2F150e03ef314e4c43824987ac897a2f5e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256884&Signature=tHL8s5PsArPR6R0QX3ROBnc%2FOqg%3D)

# Stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2F0e3fa980da8d4abfb15104b4fb6b9770.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256884&Signature=DvuAb%2FkYi2JzzXjD1hqVLT8OXkc%3D)

• Given two images from different viewpoints

– How can we compute the depth of each point in the image?

– Based on how much each pixel moves between the two images

# Epipolar geometry

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2Fb7def55be4e84f69bdfb84db3d6220aa.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256884&Signature=rPSnItq76YTxh%2FXId0tZqFbjHr0%3D)

Two images captured by a purely horizontal translating camera (rectified stereo pair)

$ x_{2}-x_{1}=\text{the disparity of pixel }(x_{1},y_{1}) $

# Disparity = inverse depth

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5164211b9dbc40768a909cc22c94b2fa%2Fmedia%2F2b63089298574954a0da255dbadc3bda.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256884&Signature=dASiTJGw143nKnYKvMW3097NU2Y%3D)

http://stereo.nypl.org/view/41729

(Or, hold a finger in front of your face and wink each eye in succession.)

# Your basic stereo matching algorithm

# • Match Pixels in Conjugate Epipolar Lines

— Assume brightness constancy

– This is a challenging problem

— Hundreds of approaches

• A good survey and evaluation: http://www.middlebury.edu/stereo/
