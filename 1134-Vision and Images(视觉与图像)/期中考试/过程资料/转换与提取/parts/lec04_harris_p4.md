# Corner detection: the math

Consider shifting the window W by  $ (u,v) $

• define an SSD "error"  $ E(u,v) $:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F201523dc67754404a42577613262ea7b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256001&Signature=CUd%2BLtkxEV220PVw5QEnUE9pt%2Bg%3D)

$$ \begin{array}{r c l}{E(u,v)}&{=}&{\displaystyle\sum_{(x,y)\in W}[I(x+u,y+v)-I(x,y)]^{2}}\\ {}&{\approx}&{\displaystyle\sum_{(x,y)\in W}[I(x,y)+I_{x}u+I_{y}v-I(x,y)]^{2}}\\ {}&{\approx}&{\displaystyle\sum_{(x,y)\in W}[I_{x}u+I_{y}v]^{2}}\\ \end{array} $$

# Corner detection: the math

Consider shifting the window W by  $ (u,v) $

• define an SSD "error"  $ E(u,v) $:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F5a538fa568724392902de769d556959e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256001&Signature=AkjvDt1O%2F4hZMQl5tm%2B43l7UjIY%3D)

$$ \begin{array}{r l r}{E(u,v)}&{\approx}&{\displaystyle\sum_{(x,y)\in W}[I_{x}u+I_{y}v]^{2}}\\ &{\approx}&{A u^{2}+2B u v+C v^{2}}\end{array} $$

$$ A=\sum_{(x,y)\in W}I_{x}^{2}\quad B=\sum_{(x,y)\in W}I_{x}I_{y}\quad C=\sum_{(x,y)\in W}I_{y}^{2} $$

• Thus,  $ E(u,v) $ is locally approximated as a quadratic error function

# The second moment matrix

The surface  $ E(u,v) $ is locally approximated by a quadratic form.

$$ \begin{array}{r l r}{E(u,v)}&{\approx}&{A u^{2}+2B u v+C v^{2}}\\ &{\approx}&{\left[\begin{array}{l l}{u}&{v}\end{array}\right]\left[\begin{array}{l l}{A}&{B}\\ {B}&{C}\end{array}\right]\left[\begin{array}{l}{u}\\ {v}\end{array}\right]}\\ &{}&{\underbrace{\quad\quad\quad\quad}_{(x,y)\in W}\quad}\\ {A}&{=}&{\displaystyle\sum_{(x,y)\in W}I_{x}^{2}}\\ &{}&{H}\end{array} $$

$$ B=\sum_{(x,y)\in W}I_{x}I_{y} $$

$$ C=\sum_{(x,y)\in W}I_{y}^{2} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F2132df807ad54f419821ff4a66b90925.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=ZxV%2BglDMNe4Dk7HBCclHhuXQClM%3D)

Let's try to understand its shape.

$$ \begin{array}{c}{E(u,v)\approx\left[\begin{array}{l l}{u}&{v}\end{array}\right]\left[\begin{array}{l l}{A}&{B}\\ {B}&{C}\end{array}\right]\left[\begin{array}{l}{u}\\ {v}\end{array}\right]}\\ {\underbrace{\quad}_{H}}\\ \end{array} $$

$$ A=\sum_{(x,y)\in W}I_{x}^{2} $$

$$ B=\sum_{(x,y)\in W}I_{x} I_{y} $$

$$ C=\sum_{(x,y)\in W}I_{y}^{2} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F5a8dcad68f4a4ca6b6884ade72d8ff5f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=jcji%2Fv8a3%2FdMD%2FmBA5Gjilc50NE%3D)

Horizontal edge:  $ I_{x}=0 $

$$ \boldsymbol{H}=\left[\begin{array}{ll}{{{0}}}&{{{0}}} \\{{{0}}}&{{{C}}}\end{array}\right] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F32f8097f517045da9a0bf281522efba7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=LF%2BVE13XeZXzKojJdpt58CMA6So%3D)

$$ \begin{array}{c}{E(u,v)\approx\left[\begin{array}{l l}{u}&{v}\end{array}\right]\left[\begin{array}{l l}{A}&{B}\\ {B}&{C}\end{array}\right]\left[\begin{array}{l}{u}\\ {v}\end{array}\right]}\\ {\underbrace{\quad}_{H}}\\ \end{array} $$

$$ \begin{aligned}&A=\sum_{(x,y)\in W}I_{x}^{2}\\ &B=\sum_{(x,y)\in W}I_{x}I_{y}\\ &C=\sum_{(x,y)\in W}I_{y}^{2}\\ \end{aligned} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F60e4e5d5fd4b49ce9677dd25126bb47c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=RCwlvClayVggvtIsPLkh7npr9YY%3D)

$$ I_{y}=0 $$

$$ \boldsymbol{H}=\left[\begin{array}{ll}{{{A}}}&{{{0}}} \\{{{0}}}&{{{0}}}\end{array}\right] $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F5d0e469cc00048afa2348d2384714976.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=j1wicbOWRKs8MhbL%2B%2B%2BFpJTxCws%3D)

# General case

We can visualize H as an ellipse with axis lengths determined by the eigenvalues of H and orientation determined by the eigenvectors of H

Ellipse equation:

$ \lambda_{\max}, \lambda_{\min} $ : eigenvalues of H

direction of the

fastest change

$$ \left[u\quad v\right]\quad H\quad\begin{bmatrix}u\\ v\end{bmatrix}=\mathbf{const} $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F0e914984d7054b6aafc69c23e7be3969.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=S5GRUOKv05NdwXbaIGVfwogDWcg%3D)

direction of the

slowest change

# Quick eigenvalue/eigenvector review

The eigenvectors of a matrix A are the vectors x that satisfy:

$$ Ax=\lambda x $$

The scalar  $ \lambda $ is the eigenvalue corresponding to x

– The eigenvalues are found by solving:

$$ det(A-\lambda I)=0 $$

– In our case,  $ A = H $ is a 2x2 matrix, so we have

$$ det\left[\begin{array}{cc}h_{11}-\lambda&h_{12}\\h_{21}&h_{22}-\lambda\end{array}\right]=0 $$

— The solution:

$$ \lambda_{\pm}=\frac{1}{2}\left[\left(h_{11}+h_{22}\right)\pm\sqrt{4h_{12}h_{21}+\left(h_{11}-h_{22}\right)^{2}}\right] $$

Once you know  $ \lambda $, you find x by solving

$$ \left[\begin{array}{c c}h_{11}-\lambda&h_{12}\\ h_{21}&h_{22}-\lambda\end{array}\right]\left[\begin{array}{l}x\\ y\end{array}\right]=0 $$

# Corner detection: the math

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F71410924c6cf4c58b653ce5653787fde%2Fmedia%2F50fbdd787fbc4f57bbfeb496cabe1469.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256002&Signature=5zEJ%2BOlAklhsQlpyaGQx4IppWy4%3D)

Eigenvalues and eigenvectors of H

• Define shift directions with the smallest and largest change in error

•  $ x_{\text{max}} = \text{direction of largest increase in } E $

•  $ \lambda_{\max} = \text{amount of increase in direction } x_{\max} $

•  $ x_{\min} = $ direction of smallest increase in E

•  $ \lambda_{\min} = \text{amount of increase in direction } x_{\min} $
