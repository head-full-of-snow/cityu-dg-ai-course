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
![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2Fa3699ba5e62d4be697d1c89ec97684ab.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255840&Signature=y8i27HyczMDMmwbbJzvzMnzmg2Y%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2Fdbdfa1641f114a449dd0a98c755cc6e7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255840&Signature=VUJInbiwA8OVW5duJ%2B3%2Fomp0Cis%3D)

# Gaussian pyramids [Burt and Adelson, 1983]

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2F3466ccec0719485daf36563dd5b814a0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255840&Signature=HVzZ69tNzaQK8tKKsHWUucP8qDc%3D)

• In computer graphics, a mip map [Williams, 1983]

• A precursor to wavelet transform

Gaussian Pyramids have all sorts of applications in computer vision

# Gaussian pyramids [Burt and Adelson, 1983]

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2F38c73653158f47e485c01a79816cc361.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255840&Signature=XmTVuMW5LNVFzJ7hvjDk12RUgBQ%3D)

Q: How much space does a Gaussian pyramid take compared to the original image?

# Gaussian pyramid

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2F2343f0427cfe4f32bade0b97625abf59.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255841&Signature=hDQDmMIIKkz1fuzyA4kscwuIff4%3D)

# Gaussian pyramid

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2Ffd0d1505fc0b4c92a2833ba833760c17.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255841&Signature=9m4VVDk9zc5pSgcd4RAEJRJgyYc%3D)

Answer: 4/3 the amount of space as the original image alone

See  $ \underline{\text{https://en.wikipedia.org/wiki/Geometric_series}} $

# Back to the checkerboard

• What should happen when you make the checkerboard smaller and smaller?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2F5d5509ef86044e11876c826360c028fb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255841&Signature=Ub3%2FzrsKpC0qfOFv7we7vzJSov4%3D)

Naïve subsampling

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F670e0a0b7fa04efe9d11280a9bd75ee3%2Fmedia%2Fd7a7414f976047b88438d41d1fad0263.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255841&Signature=VfZBPbm1M1FJ2AztbehCcYQ%2BtS8%3D)

Proper prefiltering ("antialiasing")

Image turns grey!

(Average of black and white squares, because each pixel contains both.)

Questions?
# Upsampling

• This image is too small for this screen:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F2f6fcbe23c234145846a2c4f2731e1f3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255864&Signature=PdEAjNqtA6FtyL1rgJZ1e2l5QEY%3D)

• How can we make it 10 times as big?

• Simplest approach:

repeat each row

and column 10 times

• ("Nearest neighbor interpolation")

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fdc30d009ff6f4fbea43e6f6f432d512c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255864&Signature=K5b8j0oMx66ccDbO055lM0qDk4Q%3D)

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F889287fabe304308bfc850a52dc570b7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255864&Signature=D6tJghxvQdO7p8ghQelyW2ZqDcA%3D)

d = 1 in this example

Recall that a digital images is formed as follows:

$$ F[x,y]=quantize\{f(xd,yd)\} $$

• It is a discrete point-sampling of a continuous function

- If we could somehow reconstruct the original function, any new image could be generated, at any resolution and scale

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fd53dfe6f3a2d4c38b760d7490c5be49b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=CTt8t%2FrxIArwYf3S25E81PD4O38%3D)

d = 1 in this example

Recall that a digital images is formed as follows:

$$ F[x,y]=quantize\{f(xd,yd)\} $$

• It is a discrete point-sampling of a continuous function

- If we could somehow reconstruct the original function, any new image could be generated, at any resolution and scale

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fc75dacc4c8e3449fa3db69ea45ab89c3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=XLTTDm7xH7vdnf8npQ5bqssMU%2FM%3D)

d = 1 in this example

• What if we don't know f ?

• Guess an approximation:  $ \tilde{f} $

• Can be done in a principled way: filtering

- Convert $F$ to a continuous function:

$ f_{F}(x) = F\left(\frac{x}{d}\right) $ when  $ \frac{x}{d} $ is an integer, 0 otherwise

• Reconstruct by convolution with a reconstruction filter, h

$$ \tilde{f}=h*f_{F} $$

# I mage interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fc80f20f2a9b54d0a8c966a872d6f4d98.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=UaTVVsyTdyRXee3NLn8rgcc6OBo%3D)

"Ideal" reconstruction

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F479f7eb7605b41bdabe3fc6b55ec6f17.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=%2FMAlavvZ8bXtYub4BJLK3j20nW0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F10ce837d4f594107be3ba6996b8e54d7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=szz2f%2FhpBNl%2B7iZFALXPFOyS25o%3D)

Nearest-neighbor interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F91cb023f03454a1fb3901da9ad795da1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=Z6%2FPjuDAUn5tM0IFhclclbmm1d0%3D)

Linear interpolation

<table><tr><td>gauss(x)</td><td>x</td></tr></table>

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fff44202fb17140dba4dff90f13fe3345.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=0p2%2FcFYcib5ZeXBkRs13wqmkr48%3D)

Gaussian reconstruction

# Reconstruction filters

• What does the 2D version of this hat function look like?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F7efcd10fa0294e76a0e5625134e742e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=aRaC1c6O%2B6VowWeJBR9358mtDko%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F7ae90722d1564e318f185c807b0d5387.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255865&Signature=sMHd%2B%2BQE2%2Fl4U3hLDtR5ezIT3tw%3D)

Often implemented without cross-correlation

• E.g.,  $ \underline{\text{http://en.wikipedia.org/wiki/Bilinear_interpolation}} $

Better filters give better resampled images

• Bicubic is common choice

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fd6dbc9076bda4a21ae588fc7d534d98a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=DGVwhAl5ssBKJxcJMjVNEErHKBA%3D)

Cubic reconstruction filter

$$ r(x)=\frac{1}{6}\begin{cases}(12-9B-6C)\left|x\right|^{3}+(-18+12B+6C)\left|x\right|^{2}+(6-2B)&\left|x\right|<1\ $ (-B-6C)\left|x\right|^{3}+(6B+30C)\left|x\right|^{2}+(-12B-48C)\left|x\right|+(8B+24C)&1\leq\left|x\right|<2\\0&otherwise\end{cases} $$

# I mage interpolation

Original image: x 10

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fd75905cc86d84aedb11f1668d66923b6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=Y6U0NUrALv8nDHchNVJ4Tr1VfYI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Ff1af767633c74cdb9c8ccecc33f0dccd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=6TQi3miFQ9oYXGVNdOEJ3jHWQyI%3D)

Nearest-neighbor interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Faef2116fd9444b81b830ff9d95bb953f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=HDguqnDYoDWN1HFgeLXT2yo4Ask%3D)

Bilinear interpolation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2Fcc75f762d28e49b2a54176a02e81cf0f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=Id9B4yuod9nxX1Z0JIyIKBze%2Bc0%3D)

Bicubic interpolation

# I mage interpolation

Also used for resampling

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F1ad2dc37f95f4e60be7293203c7e760e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=gvgpKDkuO8u9vHSWeC%2F1%2F%2BdY2QI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F955f483ff9b84491bf040426e04abb4f%2Fmedia%2F384557637cfc48f89e439c700767bd5d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799255866&Signature=OwxXPRP2AW2%2Bd1r2hQt4phPmQkg%3D)
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
