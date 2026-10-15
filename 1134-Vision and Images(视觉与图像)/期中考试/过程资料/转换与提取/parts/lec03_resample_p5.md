# Modern methods

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F40d53cddd02a49218dcc159f0422b33f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=IIcC90llZFtPCP9kEFPlIB8yIpU%3D)

(a) Bicubic

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2Fdca2d09296f9498d820708cc05761de2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=8g09%2BZCkfA3mm%2FlZpVlVn6pKr%2Bs%3D)

(b) SRCNN

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F696cca697dfc4c6e91116e4b7c597881.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=fbfAQqghEslwHvSJ4oduXpUEV1k%3D)

(c) A+

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F412a9d45581741a49907b9d0f1466217.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=0XMKD%2Fvf6SRiqizGROACYHCuyQ4%3D)

(d) RAISR

(e) Bicubic

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F43bde377ce634d4faffbe7674430a0c5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=th%2FhJTxsP8Y8mOTzDpFabccEwt0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F6feabcf57d8942e4923f997801cd9ffd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=KIll21Fs82dnOmZGNWuEUYzZjN4%3D)

(f) SRCNN

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2Fc9f5557442e04bc9973062805e51c060.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=W945rdtKwvj6OaiImhIXtQJpNMY%3D)

(g) A+

From Romano, et al: RAISR: Rapid and Accurate Image Super Resolution, https://arxiv.org/abs/1606.01299

(h) RAISR

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F717bc728408c49d5934ff736563bfc48.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=PwlsMxh3U%2Bo06Pwn10J9XkkDdIE%3D)

# Super-resolution with multiple images

• Can do better upsampling if you have multiple images of the scene taken with small (subpixel) shifts

• Some cellphone cameras (like the Google Pixel line) capture a burst of photos

• Can we use that burst for upsampling?

# Google Pixel 3 Super Res Zoom

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F4b973e4ecb194ff181be4f056ede40d4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=zaaBD%2Bcx46Lrw%2BMHxjygTRgXeK8%3D)

Effect of hand tremor as seen in a cropped burst of photos, after global alignment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F696ff000db4f490faf9164cda3dd0440.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255892&Signature=%2FPNptljtAUxEVYpwuLB9tDSXAXc%3D)

Example photo with and without super res zoom (smart burst align and merge)

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fe468256fea254f52b1b5c3a010ad3f04%2Fmedia%2F4886958ec6c74dbb9b2f6a3cea2d0e09.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255893&Signature=TFAGJvI8nGSrZq1MgGQXbMImkNU%3D)

d = 1 in this example

Recall that a digital images is formed as follows:

$$ F[x,y]=quantize\{f(xd,yd)\} $$

• It is a discrete point-sampling of a continuous function

- If we could somehow reconstruct the original function, any new image could be generated, at any resolution and scale

# Summary

• Key points:

– Subsampling an image can cause aliasing. Better is to blur ("pre-filter") to remove high frequencies then downsample

– If you repeatedly blur and downsample by 2x, you get a Gaussian pyramid

– Upsampling an image requires interpolation. This can be posed as convolution with a “reconstruction kernel”

Questions?
