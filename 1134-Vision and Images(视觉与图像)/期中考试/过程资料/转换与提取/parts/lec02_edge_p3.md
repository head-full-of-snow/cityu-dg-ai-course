![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Feddabb92a4cd4b0db7e980d41b799c45.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=pJk6KYATXwDt8XgIjRs85dX%2Ft%2Fw%3D)

Image with Edge

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F284c975adad64444b5187a407952563e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=SC5VvaJrgh%2FYGEIxgPRL0spOClE%3D)

Edge Location

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Fee61dff4007f4b7b98bcee7b8a428090.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=qTqOgvtFyee8uWUEg3lWMmPQIvA%3D)

Image + Noise

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Ff485f84c49ce421495c7441f6bd9a047.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=rywTXfc7JdHC9e4vEBWeDmmA0iE%3D)

Derivatives detect edge and noise

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F379aaabac4c849fe8dddfcd6ea125ab4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=KTpiGCOEPiQ%2F6qu2T1D6I3jpL20%3D)

Smoothed derivative removes noise, but blurs edge

# Example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Fe4fbbaeefbc84ef7b5ce38e6cf7cc2e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=UMHennxumoEx9CDKY3Y%2FSxYnpU0%3D)

original image

# Finding edges

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F379067c92add4afc83f7eaddf80b03d0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255754&Signature=JFvW4%2FsEE4HGOyBpfou7hDuEozo%3D)

smoothed gradient magnitude

# Finding edges

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Fd3409b8221814574bc3c7641c1ec5407.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=lA4D510GmIFavctdjqueE27w4P4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Ff3e465968b5546878115935a690a3487.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=28TawF%2BJx%2FjauWErCRs6w1X30nY%3D)

thresholding

where is the edge?

# Get Orientation at Each Pixel

• Get orientation (below, threshold at minimum gradient magnitude)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2Fa24df8ed07fd49fea9aeb6aff18f3a6b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=GdSy%2FVtDX8syfMqoYM73uACFO5E%3D)

$$ \theta=atan2(gy,gx) $$

Gradient orientation angle

# Non-maximum suppression

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F195533c32b8b4c5eb84b818475daa5e1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=rFc9AinaNJp9vx5nTrWJuGskap8%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F44035775a68e4e3c9ee35a7627da24d4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=iT207GfntOw72lyg9Do41b9X%2BDs%3D)

- requires interpolating pixels p and r

# Before Non-max Suppression

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F61506debd30d4d5c83c48fcdb6b18983.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=KIyZc46ZtawcRCJuTkDARUbB2Ps%3D)

# After Non-max Suppression

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F099c7cdada5749bdbbc15312244a6897%2Fmedia%2F748e65723390423b876fe50b202d3625.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255755&Signature=i8oec0cZdofaRE5aD6DMcGTW8ek%3D)
