# Question: Noise reduction

• Given a camera and a still scene, how can you reduce noise?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Fae0e1da751dc4cadaf33c22e6517b597.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255593&Signature=vS03KwMG1FLP%2BuiLpfOILvpIIRI%3D)

Take lots of images and average them!

What's the next best thing?

# I mage filtering

• Modify the pixels in an image based on some function of a local neighborhood of each pixel

<table><tr><td>10</td><td>5</td><td>3</td></tr><tr><td>4</td><td>5</td><td>1</td></tr><tr><td>1</td><td>1</td><td>7</td></tr></table>

Local image data

Some function

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2F709263a81745425f97bc6195b33ffae0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255593&Signature=%2F5F%2BzIKINqubJqyovW14PSocdE0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2F9c0c3b880fd5420bb07b80188fd96c12.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255593&Signature=zQnGnKCm%2FMPVDt8iRXPX0fdkgKk%3D)

Modified image data

# Linear filtering

• One simple version of filtering: linear filtering (cross-correlation, convolution)

– Replace each pixel by a linear combination (a weighted sum) of its neighbors

• The prescription for the linear combination is called the "kernel" (or "mask", "filter")

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Fa8a3e2fcd8184c54b1f802d263a62a29.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255593&Signature=R5ja5kcoCx5eD84Gs1fBD3tvhXs%3D)

# Convolution

Let F be the image, H be the kernel (of size  $ 2k+1 \times 2k+1 $), and G be the output image

$$ G[i,j]=\sum_{u=-k}^{k}\sum_{v=-k}^{k}H[u,v]F[i-u,j-v] $$

This is called a convolution operation:

$$ G=H*F $$

- Can think of as a "dot product" between local neighborhood and kernel for each pixel

# Convolution

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2F7ca83d1700144ebe8a4c43da48d6c9bd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255594&Signature=1yKbicWgNrhxxIQYAKAfz6MqKec%3D)

<table><tr><td>$ \overline{H} $</td><td></td></tr><tr><td></td><td>F</td></tr></table>

# Mean filtering

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Fd342b853b2d742a19ea131dd3cc2dc04.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255594&Signature=pE69UZGRa2%2B8f7V3a9jZepxJzw0%3D)

H

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

F

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>10</td><td>20</td><td>30</td><td>30</td><td>30</td><td>20</td><td>10</td><td></td></tr><tr><td></td><td>0</td><td>20</td><td>40</td><td>60</td><td>60</td><td>60</td><td>40</td><td>20</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>60</td><td>90</td><td>90</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>50</td><td>80</td><td>80</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>30</td><td>50</td><td>80</td><td>80</td><td>90</td><td>60</td><td>30</td><td></td></tr><tr><td></td><td>0</td><td>20</td><td>30</td><td>50</td><td>50</td><td>60</td><td>40</td><td>20</td><td></td></tr><tr><td></td><td>10</td><td>20</td><td>30</td><td>30</td><td>30</td><td>30</td><td>20</td><td>10</td><td></td></tr><tr><td></td><td>10</td><td>10</td><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

G

# Mean filtering / Moving average

<table><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

$ F[x, y] $

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

$ G[x, y] $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Fee3528eaf7bf4128ba964be860075334.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255594&Signature=13Ntju4RA2HceqLs0ux8ZYyN6DI%3D)

# Mean filtering / Moving average

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>90</td><td>90</td><td>90</td><td>90</td><td>90</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>90</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

$ G[x, y] $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F814f850afc1c41efa990ac0b6d3221e9%2Fmedia%2Ff959174cfd9d4b4a8525775c8dafdd27.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255594&Signature=H6v11PdlMIlVUxmDAml16N9G0cw%3D)
