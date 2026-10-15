> 来源: CS5487-l3supplements.pdf | 翻译模型: deepseek-v4-flash-0731

# 最小二乘与MAP的矩阵微积分：向量梯度简明指南

Kangning Cui

香港城市大学（东莞）

2026/27学年A学期

# 为什么这很重要

在最小二乘法中，目标函数是一个数值：

$$ J(\boldsymbol{w})=\|\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w}\|_{2}^{2}. $$

未知参数是一个向量：

$$ \boldsymbol{w}=(w_{1},\ldots,w_{d})^{\mathsf{T}}. $$

对 w 求导意味着询问当每个坐标变化时 J 如何变化。因此，

$$ \nabla_{w}J=\begin{bmatrix}\partial J/\partial w_{1}\\ \vdots\\ \partial J/\partial w_{d}\end{bmatrix}. $$

标量目标函数对向量求导得到梯度向量。

# 梯度的形状

如果

$$ f:\mathbb{R}^{d}\to\mathbb{R}, $$

那么 f 接受向量输入并返回标量。在本课程中，我们采用列梯度约定：

$$ \nabla_{w}f=\begin{bmatrix}\partial f/\partial w_{1}\\ \partial f/\partial w_{2}\\ \vdots\\ \partial f/\partial w_{d}\end{bmatrix}\in\mathbb{R}^{d}. $$

梯度与 w 具有相同的形状：

$$ w\in\mathbb{R}^{d},\qquad\nabla_{w}f\in\mathbb{R}^{d}. $$

常见错误

有些教材使用行梯度记号。公式看起来可能是转置的，但含义相同。

CS5487 – 矩阵微积分

# 导数规则

设 a 和 A 是关于 w 的常数

<table><tr><td>表达式</td><td>关于 w 的梯度</td></tr><tr><td>c</td><td>0</td></tr><tr><td>$ a^{\top}w $</td><td>a</td></tr><tr><td>$ w^{\top}a $</td><td>a</td></tr><tr><td>$ w^{\top}w $</td><td>2w</td></tr><tr><td>$ w^{\top}Aw $</td><td>$ (A + A^{\top})w $</td></tr></table>

如果 A 是对称的，

$$ \nabla_{w}(w^{\top}A w)=2A w. $$

# 平方范数

从最简单的二次型开始：

$$ f(\boldsymbol{w})=\boldsymbol{w}^{\top}\boldsymbol{w}. $$

逐坐标写出，

$$ f(\boldsymbol{w})=w_{1}^{2}+\cdots+w_{d}^{2}. $$

对某个坐标的导数为

$$ \frac{\partial f}{\partial w_{k}}=2w_{k}. $$

将所有坐标堆叠起来得到

$$ \nabla_{w}f=\begin{bmatrix}2w_{1}\\ \vdots\\ 2w_{d}\end{bmatrix}=2w. $$

梯度是一个向量，因为它收集了 w 每个分量对应的一个偏导数。

# 二次型

考虑

$$ f(\boldsymbol{w})=\boldsymbol{w}^{\top}\boldsymbol{A}\boldsymbol{w}. $$

在坐标形式下，

$$ f(\boldsymbol{w})=\sum_{i}\sum_{j}w_{i}A_{i j}w_{j}. $$

当对 $ w_{k} $ 求导时，$ w_{k} $ 可能出现在两个位置：

$$ w_{i}A_{i j}w_{j}. $$

它可以是左边的因子 $ w_{i} $，也可以是右边的因子 $ w_{j} $。这产生两项贡献：

$$ \frac{\partial f}{\partial w_{k}}=\sum_{j}A_{kj}w_{j}+\sum_{i}w_{i}A_{ik}. $$

因此，

$$ \nabla_{}{w}f=(A+A^{\mathsf{T}})w. $$

# 对称情形

如果 A 是对称的，那么

$$ \boldsymbol{A}=\boldsymbol{A}^{\top}. $$

二次型规则变为

$$ \nabla_{w}(w^{\top}A w)=(A+A)w=2A w. $$

这就是为什么我们经常看到因子 2。在最小二乘法中，

$$ \boldsymbol{A}=\boldsymbol{X}^{\top}\boldsymbol{X}. $$

该矩阵是对称的，因为

$$ (\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X})^{\mathsf{T}}=\boldsymbol{X}^{\mathsf{T}}\boldsymbol{X}. $$

因子 2 的出现是因为 w 的两个副本都有贡献，而当 A 对称时，这两项贡献相等。

# 最小二乘设置

将所有观测值堆叠为一个矩阵和一个向量：

$$ \boldsymbol{X}\in\mathbb{R}^{n\times d},\qquad\boldsymbol{y}\in\mathbb{R}^{n},\qquad\boldsymbol{w}\in\mathbb{R}^{d}. $$

预测向量为

$$ \hat{\mathbf{y}}=\mathbf{X}\mathbf{w}\in\mathbb{R}^{n}. $$

残差向量为

$$ \boldsymbol{r}=\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w}\in\mathbb{R}^{n}. $$

最小二乘法最小化残差长度的平方：

$$ J(w)=\|r\|_{2}^{2}=\|y-X w\|_{2}^{2}. $$

目标函数是标量，但被优化的变量是向量 w。

# 展开最小二乘

从

$$ J(\boldsymbol{w})=\|\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w}\|_{2}^{2}. $$

开始。

根据平方范数的定义，

$$ J=(y-X w)^{\top}(y-X w). $$

展开得到

$$ J=y^{\top}y-y^{\top}X w-w^{\top}X^{\top}y+w^{\top}X^{\top}X w. $$

中间两项都是标量且相等，因此

$$ J=y^{\top}y-2w^{\top}X^{\top}y+w^{\top}X^{\top}X w. $$

# 对最小二乘求导

展开后的目标函数为

$$ J=y^{\top}y-2w^{\top}X^{\top}y+w^{\top}X^{\top}X w. $$

第一项关于 w 是常数：

$$ \nabla_{w}(y^{\top}y)=0. $$

对于线性项，令

$$ \boldsymbol{a}=\boldsymbol{X}^{\top}\boldsymbol{y}. $$

则

$$ \nabla_{w}(-2w^{\mathsf{T}}a)=-2a=-2X^{\mathsf{T}}y. $$

# 完成梯度

对于二次项，使用

$$ \boldsymbol{A}=\boldsymbol{X}^{\top}\boldsymbol{X}. $$

由于 A 是对称的，

$$ \nabla_{w}(w^{\top}X^{\top}X w)=2X^{\top}X w. $$

合并所有项：

$$ |\nabla_{w}J=-2\boldsymbol{X}^{\top}\boldsymbol{y}+2\boldsymbol{X}^{\top}\boldsymbol{X}w|. $$

等价地，

$$ \nabla_{w}J=-2\mathbf{X}^{\mathsf{T}}(\mathbf{y}-\mathbf{X}w). $$

最小二乘梯度由来自数据的线性项和来自模型的二次项组合而成。

# 为什么会出现 $ X^{\top} $

残差位于观测空间：

$$ \boldsymbol{r}=\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w}\in\mathbb{R}^{n}. $$

但梯度必须位于参数空间：

$$ \nabla_{w}J\in\mathbb{R}^{d}. $$

转置具有正确的形状：

$$ \mathbf{X}^{\mathsf{T}}\in\mathbb{R}^{d\times n}. $$

因此，

$$ \mathbf{X}^{\mathsf{T}}\mathbf{r}\in\mathbb{R}^{d}. $$

这将残差信息映射回 w 的坐标。梯度可以写成

$$ \nabla_{w}J=-2\mathbf{X}^{\top}\mathbf{r}. $$

维度检查解释了为什么需要转置。

# 正规方程

在无约束最优解处，

因此，

$$ \begin{aligned}&\nabla_{w}J=\mathbf{0}.\\ &\\-2\boldsymbol{X}^{\top}\boldsymbol{y}+2\boldsymbol{X}^{\top}\boldsymbol{X}\hat{\boldsymbol{w}}=\mathbf{0}.\\ &\\-\boldsymbol{X}^{\top}\boldsymbol{y}+\boldsymbol{X}^{\top}\boldsymbol{X}\hat{\boldsymbol{w}}=\mathbf{0}.\\ \end{aligned} $$

除以 2：

重新整理得到

$$ \left|X^{\top}X\hat{w}=X^{\top}y\right|. $$

这些就是正规方程。

# 岭梯度

岭回归增加一个惩罚项：

$$ J_{\mathrm{r i d g e}}(w)=\|y-X w\|_{2}^{2}+\lambda w^{\top}w. $$

我们已经知道

$$ \nabla_{w}||y-X w||_{2}^{2}=-2X^{\top}y+2X^{\top}X w. $$

惩罚项贡献为

$$ \nabla_{w}(\lambda w^{\mathsf{T}}w)=2\lambda w. $$

因此，

$$ \nabla_{w}J_{\mathrm{r i d g e}}=-2\boldsymbol{X}^{\top}\boldsymbol{y}+2\boldsymbol{X}^{\top}\boldsymbol{X}w+2\lambda w. $$

# 岭方程

令岭梯度为零，得到

$$ -2\boldsymbol{X}^{\top}\boldsymbol{y}+2\boldsymbol{X}^{\top}\boldsymbol{X}\hat{\boldsymbol{w}}+2\lambda\hat{\boldsymbol{w}}=\mathbf{0}. $$

除以2并合并包含 $ \hat{w} $ 的项：

$$ \boldsymbol{X}^{\top}\boldsymbol{X}\hat{\boldsymbol{w}}+\lambda\boldsymbol{I}\hat{\boldsymbol{w}}=\boldsymbol{X}^{\top}\boldsymbol{y}. $$

因此，

$$ \left|\left(\boldsymbol{X}^{\top}\boldsymbol{X}+\lambda\boldsymbol{I}\right)\hat{\boldsymbol{w}}=\boldsymbol{X}^{\top}\boldsymbol{y}\right|. $$

如果惩罚项以 $ w_{0} $ 为中心，则惩罚梯度变为

$$ 2\lambda(w-w_{0}). $$

岭回归使用与最小二乘相同的求导法则，只是多了一个惩罚梯度。
