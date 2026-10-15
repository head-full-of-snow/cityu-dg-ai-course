# Automatic scale selection

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fc1157efd7ba34e89bfad8ce1822718c2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256160&Signature=8zfXZCM8DCcYltKwk%2B%2BhfyDxucw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F1cf09c77424b4cf188444357e7dbf783.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=p7vU2JuG6F5PaOVF%2BvW6%2BeMmOjQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F735640d2c3b54de1abb5a5a53ebdfb22.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=NVT1ngvzm2V2jRUcR4uzhlnxjYE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fc749e72fceab40ffafa8586df28a44af.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=PMr0qaMIntXXQ02VIS8jzeLYTnw%3D)

# Automatic scale selection

Normalize: rescale to fixed size

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fc86beb9d12064114a0343723a0522354.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=734nVDhPbshzRU9rbmDxIIKvRaw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F268c3b656a4e461a9d49a573e440657a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=iXc1kO6ujpTjPx38v9m2DBGyMyc%3D)

# I mplementation

• Instead of computing f for larger and larger windows, we can implement using a fixed window size with a Gaussian pyramid

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F7a77a3765c474811bff2255490c56a4e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=fuyQmbxaBbYgipULOqGNhpfZ05k%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fd3463dc99bab43989fde08655daff8d9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=ybZObIVUQ4mPHL2wJtTSjHQ4wgk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fa65aedb4eba046f2a44da79248919660.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=tH7r%2FVHqM2qBo%2FFNN0QoDYw1IM8%3D)

(sometimes need to create in-

between levels, e.g. a  $ \frac{3}{4} $-size image)

# Feature extraction: Corners and blobs

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F679b2f57538849a3b914ea63fb7a3da1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256161&Signature=wsx85dFrqX1UmxzyWAYfoVrTeWc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F00bccc04e54b4536a41a2144cf7ae6ee.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=p7j9VhrQxbkUcTIynjhueoWaNrM%3D)

# Another common definition of f

• The Laplacian of Gaussian (LoG)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F1e3c3362891b4cd687b3377f38036c83.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=nYo0MRbAtdZ62SAv6GGXRNBytH0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F6fc8efefcda9446daf8f476f76eabadf.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=jAcsvMIcMB2YSTY0OnwGfAH1Sdo%3D)

$$ \nabla^{2}g=\frac{\partial^{2}g}{\partial x^{2}}+\frac{\partial^{2}g}{\partial y^{2}} $$

(very similar to a Difference of Gaussians (DoG) – i.e. a Gaussian minus a slightly smaller Gaussian)

# Laplacian of Gaussian

• "Blob" detector

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F3c09571be1b34de2824e3367833cb7c1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=Fg4eCAVu5EVk7xGaO1xevh5CddY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F266f8d706ffb4a53a980d3f2a5482eb5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=%2BrVS8wp0gw0diBjVEpnxlp08JrQ%3D)

• Find maxima and minima of LoG operator in space and scale

# Scale selection

• At what scale does the Laplacian achieve a maximum response for a binary circle of radius r?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fd6745b96873040cb84684b0f7c42f363.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256162&Signature=Zin8nIweZt6%2B7v3u%2Fhkn9g3bTb4%3D)

image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F6302c22048f14bd281ab4a38e9bb0a1a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256172&Signature=QAj25osSMqkyvaWrTyNcGt5SrQ8%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2F4b5f301d77e24212aa034fcbee828696.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256172&Signature=RuiNgWxKQsfUd4cPZ9YsWQ28bog%3D)

Laplacian

# Characteristic scale

• We define the characteristic scale as the scale that produces peak of Laplacian response

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fa6449ff891144eac872caaaf43d9d8bc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256172&Signature=O7kY7fEWOMkRKb%2FpyDlvN%2B3%2BTmM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F34ef5be51b174c1cb8b6069d28402b43%2Fmedia%2Fe38ecf74dba9460ba6bc6d1b92a84649.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256173&Signature=viR2%2B12bXrXGn1l3%2BGCXUC0iXxk%3D)

T. Lindeberg (1998). "Feature detection with automatic scale selection." International Journal of Computer Vision 30 (2): pp 77--116.
