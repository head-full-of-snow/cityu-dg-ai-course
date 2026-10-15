# Wagon-wheel effect

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F9ea603e16c9c4b948b48550a442183c5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255820&Signature=zKCBRU4IVBQP5EHyMxqTf%2BKGTSg%3D)

https://en.wikipedia.org/wiki/Wagon-wheel_effect

# Temporal aliasing – helicopter blades

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F5028d7e7bd5f4125891c15ee48c2a417.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255820&Signature=euKGy1PtIbVzPbkrKo6Pn6xF1hE%3D)

https://www.youtube.com/watch?v=yr3ngmRuGUc

# Aliasing in practice

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2Fcafc892160444b1c8e284060def78c89.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=4D%2BCD83h1h%2FjINgXK%2B4EoVPrVNI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F2b924cb43a6e4192bf888577f9dfd300.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=TClxtiMOnzx0MezP6jcgUtKX0G8%3D)

# Aliasing

• When downsampling by a factor of two

– Original image has frequencies that are too high

• How can we fix this?

# Gaussian pre-filtering

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F4ec4352908d4409cace59ace74c6065c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=Dqw0Lb8WSifTw15Kf%2FJJHja831w%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F43dbeb38e84643b5834b97d59cb68bcc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=swOmiUABmy2RnGWXAvrUkk5Nhgk%3D)

Gaussian 1/2

G 1/4

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F6f4558f4a1dc455fb0bb272529c21061.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=PljXKX3le4B8d56ArjY6VKOKQsM%3D)

G 1/8

• Solution: filter the image, then subsample

# Subsampling with Gaussian pre-filtering

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F7ebb76fc2cd84ab8a80be11afc353650.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=qq6L5%2BTe1SPH0LQk1JAnsRVUwm0%3D)

Gaussian 1/2

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2Fd831fbe2215243ba8d7aaff3f93fe140.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=U5eOBgp3QUO0S%2FcLjmw4MwSGA4c%3D)

G 1/4

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F702f2f90e81548d08aa51b0d883bd85e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=fzmRYGAWLqGahIEwzsaWNhu3KUA%3D)

G 1/8

• Solution: filter the image, then subsample

# Compare with

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2Fcf7012b62b1f4af0abdb505e53397a4d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255821&Signature=J0TGXYZ2aoV52u05xpER60HeGEA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F0d267d4f41dd4a18a96b552cff9a6d6c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=gqzPHgssr7HOMMf9OfVBgpAWUyE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2Fc3e0f8d407b144f0a422fe910b3f96b6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=YyDdvHUZYSSTLbAgBvqCdYHrAFQ%3D)

1 /8 (4x zoom)

# Gaussian prefiltering

• Solution: filter the image, then subsample

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F44854e96fe494446a6a4ca9b53521929.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=xVY0y9Cu0YAVifkRjBu%2F1PWhJyk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F8c9c0bc0aa8646519b0f299dca5f6937.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=5AhGpx2PHhJAord4ANFKMYeErkE%3D)

subsample

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2Fcf430c2edbd64a629ccd46be3c7969e4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=%2FdawJACVNNTA5UiS8uqp5d6jYZg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2F0d0a22582dd14e03a5b17d186b9b0d63.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=IT7RM7RWMk6H1DxaTOAuuxR62r4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2Fb9dbbaeaa3d34ed091b50e9784c2646d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=KHGxljEKGSt%2BYaaVYFYVcecZ9DU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2Fcf090ac5a77a4dab96618882f6e0e391.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=mOUoat2KFbCVCufQcgOHX6AM3Ts%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fd524c9ccda664fbf9871a2072a5c58b1%2Fmedia%2Ff91d64f310a44106965e05205e8703d6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255822&Signature=jiUdk1L8fC5zfkcX26Ew8NXBKzA%3D)
