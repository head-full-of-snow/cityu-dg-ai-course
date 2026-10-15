# CS5187: Vision & Image Local features & Harris corner detection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Ffab400c2025349c3bd80e9165aa0ef88.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255914&Signature=yCM2HXDce6oqRkuWuE7WVen6%2FyA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F22023cf793db48af8269b6ab79a2c0b5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=dJPvN1V0WxheTTQIWHXdLpzPYEw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fc489ee698147498484da41e9eb4b2493.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=WoMJAG1b8LJIjQDdUUqW1oz%2Fbtw%3D)

# Today: Feature extraction—Corners and blobs

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fb6821dc5b04141f4a46a94ce39994e33.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=L7IlUBexaxD1fktzR5zsXOMRwl0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fe9230d0726c64cff9fcc90f9d3dcd671.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=b9G18ZOf1cJxX0%2BXMwRHUw2amHw%3D)

# Motivation: Automatic panoramas

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F059e3f965fef4d5aae2b0ee4510012b7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=UUaA5DyRf%2FLBjY4OXlMQC3cu49w%3D)

Credit: Matt Brown

# Panorama stitching

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fd2e7a716efd24a17bf317c97c8bd451c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=aqHc6fydl98Tcz41Z%2FMsg2QkjbM%3D)

Panorama captured by Perseverence Rover, Feb. 20, 2021

# Motivation: Automatic panoramas

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fb7d4582d6ca24efd83a7eeec0cb49330.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=YxKsQ8b3cZqiXkKtwVNjnVLJMnc%3D)

GigaPan:

http://gigapan.com/

Also see Google Zoom Views:

https://www.google.com/culturalinstitute/beta/project/gigapixels

# Why extract features?

• Motivation: panorama stitching

– We have two images – how do we combine them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F8016aa5185184b8fb2aba8fa3b83b46b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255919&Signature=iObjTtphKShyHXRUkn7MWBCJjIk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2Fc98254a37f4f43559cab490e5fc7306b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255921&Signature=OZJA3vhHw2YHEk0YtR5Zd5wDkwk%3D)

# Why extract features?

• Motivation: panorama stitching

– We have two images – how do we combine them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F06d17798911f4748a0fc28b5998491d0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255921&Signature=qIucg%2FjIzW8DXfs5Y%2FcBtnNXG%2BQ%3D)

Step 1: extract features

Step 2: match features

# Why extract features?

• Motivation: panorama stitching

– We have two images – how do we combine them?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F527242d7c6ad4f3683636271d7374820%2Fmedia%2F8d072887d1eb42cbb7a14786bce8d113.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255921&Signature=aSt%2FPhNgFp8Q0qxchnoTli40ygk%3D)

Step 1: extract features

Step 2: match features

Step 3: align images
