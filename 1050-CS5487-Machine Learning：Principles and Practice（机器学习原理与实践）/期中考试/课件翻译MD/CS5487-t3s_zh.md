> 来源: CS5487-t3s.pdf | 翻译模型: deepseek-v4-flash-0731

# 教程 3：贝叶斯估计与正则化 三项必做任务与一项选做挑战

Kangning Cui

香港城市大学（东莞）

2026/27 学年 A 学期

# 如何使用本教程

▶ 在阅读解答之前，先尝试解答每道题。

清晰写出主要计算过程或论证。

▶ 解释结果的含义，而不仅仅是最终的数值或公式。

先完成第 1–3 项任务。最后一项是选做挑战。

# 任务 1：Beta 更新

我们观察四次伯努利试验：

$$ m=3,\qquad n=4. $$

考虑两种先验：

先验 A：Beta(2, 2)，

先验 B：Beta(20, 20)。

两种先验的均值都是 0.5，但先验 B 集中得多。

1. 求每种先验下的后验分布。

2. 计算每种先验下的后验均值和下一次试验的成功概率。并将它们与 MLE 进行比较。

3. 对于先验 A，计算 MAP 估计。解释它为什么不同于后验均值。

# 解答 1：后验更新

1. 求两个后验分布。

Beta-伯努利更新给出

$$ \mathrm{Beta}(\alpha,\beta)\rightarrow\mathrm{Beta}(\alpha+m,\beta+n-m). $$

由于 m = 3 且 n - m = 1，先验 A 给出

$$ \operatorname{Beta}(2,2)\to\boxed{\operatorname{Beta}(5,3)}. $$

先验 B 给出

$$ \operatorname{Beta}(20,20)\to\boxed{\operatorname{Beta}(23,21)}. $$

两种先验的均值都从 0.5 开始，但在相同的四次观测之后，更强的先验变化更小。

# 解答 1：估计

2. 计算后验均值、预测值和 MLE。

对于先验 A，

$$ \mathbb{E}[\pi\mid\mathcal{D}]=P(x_{*}=1\mid\mathcal{D})=\frac{5}{8}=0.625. $$

对于先验 B，

$$ \mathbb{E}[\pi\mid\mathcal{D}]=P(x_{*}=1\mid\mathcal{D})=\frac{23}{44}\approx0.523. $$

MLE 只使用观测数据：

$$ \hat{\pi}_{ML}=\frac{3}{4}=0.75. $$

先验 B 使估计值更接近 0.5，因为它代表了更强的先验信息。

# 解答 1：MAP

3. 计算先验 A 下的 MAP，并将其与后验均值进行比较。在先验 A 下，

$$ \pi\mid\mathcal{D}\sim\mathrm{Beta}(5,3). $$

两个形状参数都大于 1，因此 MAP 估计为

$$ \hat{\pi}_{MAP}=\frac{5-1}{5+3-2}=\frac{2}{3}\approx0.667. $$

后验均值为

$$ \mathbb{E}[\pi\mid\mathcal{D}]=0.625. $$

它们不同，因为 MAP 选择密度最高的点，而后验均值是对整个后验分布取平均。

同一个后验分布可以根据所问的问题产生不同的点估计汇总。

# 任务 2：高斯更新

假设我们对未知均值的先验信念为

$$ \mu\sim\mathcal{N}(10,4). $$

我们观测到 n = 2 个测量值，其中

$$ \bar{x}=14,\qquad\sigma^{2}=8, $$

其中 $ \sigma^{2} $ 是已知的观测方差。

1. 计算先验精度和数据精度。哪个来源获得更大的权重？

2. 计算后验均值和后验方差。

3. 设 $ x_{*} $ 是来自同一总体的一个新观测值。求其预测均值和预测方差，并解释为什么预测方差更大。

# 解答 2：精度

1. 计算并比较这两个精度。

先验精度为

$$ \lambda_{0}=\frac{1}{4}=0.25. $$

数据精度为

$$ \lambda_{D}=\frac{n}{\sigma^{2}}=\frac{2}{8}=0.25. $$

这两个精度相等，因此先验均值10和样本均值14获得相同的权重。

# 解答2：后验

2. 计算后验均值和方差。

$$ \mu_{n}=\frac{0.25(10)+0.25(14)}{0.25+0.25}=12. $$

后验精度为

$$ \lambda_{n}=0.25+0.25=0.5, $$

所以

$$ \tau_{n}^{2}=\frac{1}{0.5}=2. $$

因此，

$$ \left|\mu\right|\mathcal{D}\sim\mathcal{N}(12,2)\left|.~\right. $$

# 解答2：预测

3. 求一个新观测的预测分布。一个新观测满足

$$ x_{*}\mid\mu\sim\mathcal{N}(\mu,8). $$

预测均值为

$$ \mathbb{E}[x_{*}\mid\mathcal{D}]=\mu_{n}=12. $$

预测方差包含两个来源：

$$ \operatorname{Var}(x_{*}\mid\mathcal{D})=\underbrace{8}_{\mathrm{o b s e r v a t i o n~n o i s e}}+\underbrace{2}_{\mathrm{u n c e r t a i n t y~a b o u t~\mu~}}=10. $$

因此，

$$ \left|x_{*}\right|\mathcal{D}\sim\mathcal{N}(12,10)\left|.~.\right. $$

预测方差大于后验方差，因为预测一个新观测既包含关于 $ \mu $ 的不确定性，也包含新的观测噪声。

# 任务3：MAP与岭回归

在讲座中，岭回归使用了以零为中心的高斯先验。现在假设改为

$$ w\sim\mathcal{N}(w_{0},\tau^{2}\boldsymbol{I}), $$

而回归模型为

$$ \boldsymbol{y}\mid\boldsymbol{w}\sim\mathcal{N}(\boldsymbol{X}\boldsymbol{w},\sigma^{2}\boldsymbol{I}). $$

1. 推导MAP目标（忽略常数项）。什么替代了通常的 $ \|w\|_{2}^{2} $ 惩罚项？

2. 对目标函数求导并推导正规方程。

3. 解释当 $ w_0 = 0 $ 和 $ \tau^2 \to \infty $ 时会发生什么。

# 解答3：MAP目标

# 1. 推导MAP目标

高斯似然部分为

$$ -\log p(\boldsymbol{y}\mid\boldsymbol{X},\boldsymbol{w})=\frac{1}{2\sigma^{2}}\|\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w}\|_{2}^{2}+C. $$

高斯先验部分为

$$ -\log p(\boldsymbol{w})=\frac{1}{2\tau^{2}}\|\boldsymbol{w}-\boldsymbol{w}_{0}\|_{2}^{2}+C. $$

因此MAP最小化

$$ \frac{1}{2\sigma^{2}}\|\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w}\|_{2}^{2}+\frac{1}{2\tau^{2}}\|\boldsymbol{w}-\boldsymbol{w}_{0}\|_{2}^{2}. $$

乘以 $ 2\sigma^{2} $ 后

$$ \boxed{\|\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w}\|_{2}^{2}+\lambda\|\boldsymbol{w}-\boldsymbol{w}_{0}\|_{2}^{2}},\qquad\lambda=\frac{\sigma^{2}}{\tau^{2}}. $$

该惩罚项现在将权重向 $ w_{0} $ 收缩，而不是向零收缩。

**解答3：正规方程**

2. 对目标函数求导并推导正规方程。

对目标函数求导得到

$$ -2\boldsymbol{X}^{\top}(\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w})+2\lambda(\boldsymbol{w}-\boldsymbol{w}_{0})=\mathbf{0}. $$

整理得，

$$ \left|\left(X^{\top}X+\lambda I\right)\hat{w}_{\mathrm{M A P}}=X^{\top}y+\lambda w_{0}\right|. $$

与普通岭回归相比，先验中心 $ w_{0} $ 贡献了额外的项

**解 3：特殊情况**

3(a). 当 $ w_{0}=0 $ 时会发生什么？

惩罚项变为

$$ \|w-w_{0}\|_{2}^{2}=\|w\|_{2}^{2}, $$

因此我们恢复了标准岭回归。

3(b). 当 $ \tau^{2} \rightarrow \infty $ 时会发生什么？

因为

$$ \lambda=\frac{\sigma^{2}}{\tau^{2}}, $$

我们得到

$$ \tau^{2}\rightarrow\infty\quad\Rightarrow\quad\lambda\rightarrow0. $$

先验变弱，惩罚项消失，MAP 趋近于普通最小二乘。

**可选：岭回归实验**

编写一个 Python 程序，研究当两个特征高度相关时岭回归的表现。生成一个合成数据集，其中

$$ n=80,\qquad w_{true}=(2,2)^{\top}. $$

从标准高斯分布生成 $ x_{1} $，并构造

$$ x_{2}=x_{1}+small\ Gaussian\ noise, $$

使得两个特征几乎相同。使用下式生成目标值

$$ y=X w_{true}+Gaussian noise. $$

1. 实现普通最小二乘和岭回归，其中 $ \lambda = 1 $。

2. 比较它们的拟合系数和训练 MSE。

3. 使用新的响应噪声重复实验 100 次，并比较拟合系数的变异性。

4. 解释为什么岭回归产生更稳定的系数。

**解：数据生成**

1. 生成一个具有高度相关特征的数据集。一种可能的实现是：

```python
rng = np.random.default_rng(7)

n = 80

x1 = rng.normal(size=n)

x2 = x1 + 0.02 * rng.normal(size=n)

X = np.column_stack([x1, x2])

w_true = np.array([2.0, 2.0])

y = X @ w_true + 0.5 * rng.normal(size=n)
```

因为 $ x_{2} $ 与 $ x_{1} $ 仅相差小的噪声，

$$ x_{2}\approx x_{1}. $$

因此 X 的两列包含几乎相同的信息。

**解：OLS 和岭回归**

1. 拟合普通最小二乘和岭回归。

```python
lam = 1.0

w_ols = np.linalg.lstsq(X, y, rcond=None)[0]

w_ridge = np.linalg.solve(

X.T @ X + lam * np.eye(2),

X.T @ y

)
```

在固定的随机种子下，拟合系数约为

$$ \hat{w}_{\mathrm{O L S}}=(4.16,-0.22)^{\top}, $$

而

$$ \hat{w}_{\mathrm{r i d g e}}=(1.98,1.93)^{\top}. $$

尽管两个模型的单个系数差异很大，但它们可以做出相似的预测。

**解：训练误差**

2. 比较训练 MSE。

计算

```python
mse_ols = np.mean((y - X @ w_ols)**2)

mse_ridge = np.mean((y - X @ w_ridge)**2)

print(mse_ols, mse_ridge)
```

对于该数据集，

$$ \mathrm{MSE_{OLS}}\approx0.215,\qquad\mathrm{MSE_{ridge}}\approx0.217. $$

预测误差几乎相同，尽管系数估计差异很大。

良好的训练拟合并不能保证系数稳定或可解释。

**解：重复试验**

3. 使用新的响应噪声重复拟合。保持 X 固定，仅重新生成 y：

```python
rng2 = np.random.default_rng(17)

ols_coef = []
```

```python
ridge_coef = []

for _ in range(100):

y_new = X @ w_true + 0.5 * rng2.normal(size=n)

ols_coef.append(

np.linalg.lstsq(X, y_new, rcond=None)[0]

)

ridge_coef.append(

np.linalg.solve(

X.T @ X + np.eye(2),

X.T @ y_new

)

)
```

**解答：变异性**

3. 比较系数变异性。

将结果转换为数组并计算其标准差：

```python
ols_coef = np.array(ols_coef)
ridge_coef = np.array(ridge_coef)

print(ols_coef.std(axis=0))
print(ridge_coef.std(axis=0))
```

标准差约为

$$ \mathrm{S D}(\hat{w}_{\mathrm{r i d g e}})=(0.050,0.047). $$

相比之下，OLS系数在重复的含噪数据集上变化剧烈，而岭系数则保持稳定得多。

**解答：解释**

4. 为什么岭回归更稳定？

因为

$$ x_{1}\approx x_{2}, $$

数据无法明确确定总效应应如何在两个系数之间分配。因此，OLS可以在保持预测几乎不变的同时增大一个系数并减小另一个系数。岭回归添加了惩罚项

$$ \lambda\|w\|_{2}^{2}, $$

这会抑制不必要的大系数。这选择了一个更均衡、对噪声更不敏感的解决方案。

即使训练误差几乎不变，岭回归也能大幅降低系数变异性。

**教程3完成**

问题与讨论

如有问题或评论，请在下方留言。

如发现任何错误或拼写问题，请在此报告。

如果您想支持这项工作，请考虑给仓库点星。

谢谢！

本教程由Jupyter笔记本生成。

下载笔记本或在GitHub上查看。

**下一篇：教程4**

在下一篇教程中，我们将探讨正则化路径和模型选择。

敬请期待！

**上一篇：教程2**

在上一篇教程中，我们介绍了偏差-方差权衡。

现在我们准备看看岭回归如何解决这一问题。

**参考文献**

[1] Hastie, Tibshirani, Friedman. 统计学习基础。

[2] Bishop. 模式识别与机器学习。

**许可证**

MIT许可证

版权所有（c）2025 您的姓名

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人无限制地处理本软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售软件副本的权利，并允许向其提供本软件的人员这样做，但须满足以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或实质性部分中。

本软件按“现状”提供，不提供任何明示或暗示的担保，包括但不限于适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对因使用本软件或与本软件的使用或其他交易有关的任何索赔、损害或其他责任负责，无论是合同诉讼、侵权行为还是其他原因。

**有问题吗？**

请在GitHub Discussions中提问。

**学习愉快！**
