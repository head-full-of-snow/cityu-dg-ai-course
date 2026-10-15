Image Resampling, Interpolation

Prof. Zhu Zhiyu

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2Fd85bfed815e741479d3f4ad8ae805e86.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255796&Signature=sJtUKTgfLWhTzqJabzSE9rCllP8%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F5dafc59812cb420980d73f83f4888d53.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255796&Signature=%2Fav2NVNCKwDU1jesRk6RzVThgNI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2Fe7221dbbf0284b36af6a98caa30e559f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255796&Signature=%2FM6QGdlFxFzk8QcSt6tSI7jE0lc%3D)

# I mage scaling

This image is too big to fit on the screen. How can we generate a half-sized version?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2Fbb44aee93a4a429f9ec7043df1baa94d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255796&Signature=KZjv4yUzGpFiTLQ47NP%2F%2BvthZEA%3D)

# I mage sub-sampling

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F82686eaf2da148b5beb0b8e9c3c4c011.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255796&Signature=3f0YKrQcr7GXUnvn00T%2FLA19pQM%3D)

Throw away every other row and column to create a 1/2 size image - called image sub-sampling

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F4ea6b9689c78496083903b82ad8a5020.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255797&Signature=MNJqy1R5s6L1S8BykqohHi3oADQ%3D)

1/4

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F3e2eb6cc037d49f589598422ea631af3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255797&Signature=ezWjQzoui7VNBUueIUwWczAt7wU%3D)

1/8

# I mage sub-sampling

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2Fafbf65239b2d42d9bc6bbccb67a2872e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255797&Signature=t%2F3tkL8prOPZFb2nesaBO%2B1u3Wg%3D)

1 /2

Why does this look so cruffy?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F4b33934430cb4f90b7d250d3b080f9f2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255797&Signature=QSQ%2FYkWo2kN%2BAdgT8TVNxC2PtBg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F5b2bb6ce9dff4da7842be87cf99b6be2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255797&Signature=Q77EJkRjpye0j1ugKiIAvWzdb1g%3D)

1/8 (4x zoom)

Source: S. Seitz

# I mage sub-sampling – another example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F097bb91f380049f985462aab9871cf66.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255798&Signature=fpQGIP40gFVpH0aeoXXalMMsjpE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F614fe0f69e44417782bdec7214a2a164.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255798&Signature=WTvqf06jk0scfVm7%2Fdw4cgBpPeI%3D)

Source: F. Durand

# Even worse for synthetic images

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F31e929b3137147d9a336fe3a50ccacbe.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255798&Signature=HGhOhxrx7sXdV2uYw51%2B917TBOU%3D)

# Aliasing

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2F7835c09c43194a8191681d59b3c15ddc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255798&Signature=pA7z7T7BRqzeWSVYZDjjobuJ84Q%3D)

- Occurs when your sampling rate is not high enough to capture the amount of detail in your image

• Can give you the wrong signal/image—an alias

• To do sampling right, need to understand the structure of your signal/image

• Enter Monsieur Fourier...

— "But what is the Fourier Transform? A visual introduction."

To avoid aliasing:

– sampling rate ≥ 2 * max frequency in the image

• said another way: ≥ two samples per cycle

– This minimum sampling rate is called the Nyquist rate

# Wagon-wheel effect

Imagine a spoked wheel moving to the right (rotating clockwise).

Mark wheel with dot so we can see what's happening.

If camera shutter is only open for a fraction of a frame time (frame time = 1/30 sec. for video, 1/24 sec. for film):

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F5fb0a1c98e6e4ade9ffb0ded54cd2a64%2Fmedia%2Fe8a8cf4d5afb4a2fb7069f81234deb9b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255799&Signature=vRD7J6DWj5Ea0p9uyrzuh8L8K6c%3D)

Without dot, wheel appears to be rotating slowly backwards! (counterclockwise)
