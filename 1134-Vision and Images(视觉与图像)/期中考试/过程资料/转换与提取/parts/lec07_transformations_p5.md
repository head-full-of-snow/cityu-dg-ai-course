# Alternate formulation for homographies

$$ \begin{aligned}\left[\begin{array}{c}x_{i}^{\prime}\\y_{i}^{\prime}\\1\end{array}\right]&\cong\left[\begin{array}{ccc}h_{00}&h_{01}&h_{02}\\h_{10}&h_{11}&h_{12}\\h_{20}&h_{21}&h_{22}\end{array}\right]\left[\begin{array}{c}x_{i}\\y_{i}\\1\end{array}\right]\end{aligned} $$

where the length of the vector  $ [h_{00} h_{01} \ldots h_{22}] $ is 1

# 2 D image transformations

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2Fac57462994ce4207ba2a45e3029441af.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=UuH1BPSWuAtapX5YjIE6Y7p9FvI%3D)

<table><tr><td>Name</td><td>Matrix</td><td># D.O.F.</td><td>Preserves:</td><td>Icon</td></tr><tr><td>translation</td><td>$ \left[ I \mid t \right]_{2 \times 3} $</td><td>2</td><td>orientation +  $ \cdots $</td><td>☐</td></tr><tr><td>rigid (Euclidean)</td><td>$ \left[ R \mid t \right]_{2 \times 3} $</td><td>3</td><td>lengths +  $ \cdots $</td><td><img src="http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2F954baae63eee455ebfbea71ba8c95ee0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=GhrB0cbZYKt18vBQwLtzpOihFJE%3D" alt="Image"" /></td></tr><tr><td>similarity</td><td>$ \left[ sR \mid t \right]_{2 \times 3} $</td><td>4</td><td>angles +  $ \cdots $</td><td><img src="http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2F38e6d92bbf2d40498ec47e46416686c6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=blZzTZdkUPDcZ%2FNA%2F5INtgtbsXo%3D" alt="Image"" /></td></tr><tr><td>affine</td><td>$ \left[ A \right]_{2 \times 3} $</td><td>6</td><td>parallels +  $ \cdots $</td><td>☐</td></tr><tr><td>projective</td><td>$ \left[ \tilde{H} \right]_{3 \times 3} $</td><td>8</td><td>straight lines</td><td><img src="http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2F5946b45b3ed74b3d817e7dbeb25c424f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=%2BZbP6ODCbuA6UJBjhOv150mVR%2BU%3D" alt="Image"" /></td></tr></table>

These transformations are a nested set of groups

• Closed under composition and inverse is a member

**I mplementing image warping**

• Given a coordinate xform  $ (x',y') = T(x,y) $ and a source image  $ f(x,y) $, how do we compute a transformed image  $ g(x',y') = f(T(x,y)) $?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2F081ec3feba124eddbdf8ee86303a2de8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=6B7cq5ZLnxFRuCwSzJSLVG9CJFI%3D)

**Forward Warping**

• Send each pixel  $ (x,y) $ to its corresponding location  $ (x',y') = T(x,y) $ in  $ g(x',y') $

• What if pixel lands "between" two pixels?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2Fbae81ef1f55e4088927762dd58217cbf.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=pI9hunzicOt0wadIOKMwD7TxaRU%3D)

**Forward Warping**

• Send each pixel  $ (x,y) $ to its corresponding location  $ (x',y') = T(x,y) $ in  $ g(x',y') $

• What if pixel lands "between" two pixels?

• Answer: add "contribution" to several pixels, normalize later (splatting)

• Can still result in holes

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2F16591c0a3be24201889f288f65715894.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=bAT1ihCWfCy55UNOJ92K8PV%2BrO4%3D)

**I nverse Warping**

• Get each pixel $g(x',y')$ from its corresponding location $(x,y) = T^{-1}(x,y)$ in $f(x,y)$

• Requires taking the inverse of the transform

• What if pixel comes from "between" two pixels?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2F42e960de17a0465e8c578be6279df2eb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=S2korOjetArCTbkMXjFAxGRwecw%3D)

**I nverse Warping**

• Get each pixel $g(x',y')$ from its corresponding location $(x,y) = T^{-1}(x',y')$ in $f(x,y)$

• What if pixel comes from "between" two pixels?

• Answer: resample color value from interpolated (prefiltered) source image

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2Fe33532cecc6d47c39fa0d0bf968e0c1f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=%2BQr3DonCTVzMW9B46ufUYRXPpiY%3D)

**I nterpolation**

• Possible interpolation filters:

— nearest neighbor

— bilinear

- bicubic

- sinc

• Needed to prevent "jaggies" and "texture crawl"

(with prefiltering)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F8cc75f8da4c44236b6dc860a6cac31cc%2Fmedia%2F4a03b79165d64a46ae37c6e39192ddd0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256815&Signature=VF2MOYFw%2BAu5UtzKx8a7Kw%2BAZic%3D)
