

本次课程讲解图像生成模型与变分推断。前半部分回顾最大似然估计及过拟合防范方法；后半部分引入隐变量建模高维图像，推导证据下界ELBO作为对数似然的优化目标，阐明当近似后验等于真实后验时ELBO等于对数似然。课程强调蒙特卡洛估计在复杂分布中的应用，并布置掌握ELBO推导及其与模型似然关系的课后重点。




## 模型优化基础与过拟合防范

- **随机梯度下降与交叉熵优化**
  - 使用Stochastic Gradient Descent训练图像计算网络时，优化目标为模型输出与Ground Truth标签之间的Cross Entropy
- **过拟合风险与模型简化原则**
  - 训练数据有限而参数过多会导致Overfitting
  - 引用Occam's Razor原则，主张模型应尽可能简单
  - 可通过添加Smoothness等正则化项或先验约束避免过拟合

## 高维图像生成挑战与潜变量引入

- **图像数据的高维特性**
  - 以1920×1080分辨率为例，单张图像包含约2 million pixels
  - 直接在原始高维像素空间建模生成过程面临显著困难
- **潜变量建模思路**
  - 图像可由若干语义Factor（如发型、表情、光照等）描述
  - 不直接重建高维向量，而是估计Latent Variable，再由潜变量重构图像
  - 潜变量分布通常较简单，可用Gaussian Distribution或Mixture of Gaussians建模
  - Mixture Model中引入离散类别变量z作为Latent Variable，各分量独立控制生成内容

## 蒙特卡洛估计局限与重要性采样改进

- **朴素蒙特卡洛采样的效率问题**
  - 真实后验p(z|x)通常非均匀分布，集中在极小区域
  - Uniform Sampling在大部分采样点概率为零，导致估计效率极低
- **引入先验分布的重要性采样**
  - 引入Prior Distribution q(z)（如以0为中心的高斯分布）替代均匀采样
  - 通过Importance Sampling重写似然：$E_{z \sim q}[\frac{p_\theta(x,z)}{q(z)}]$
  - 该方法为Naive Monte Carlo的进阶版本，提升采样有效性

## ELBO推导与对数似然优化关系

- **Jensen不等式与下界建立**
  - Log函数为凹函数，满足Log Expectation ≥ Expectation Log
  - 由此导出Evidence Lower Bound（ELBO）≤ Log Likelihood
- **ELBO的优化意义**
  - 最大化ELBO可间接提升Log Likelihood
  - ELBO可分解为两项：期望对数联合概率减去q(z)的Entropy
- **下界取等条件**
  - 当且仅当q(z) = p(z|x,θ)时，ELBO精确等于Log Likelihood
  - 准确编码后验分布是获得精确对数似然的关键
- **ELBO与Log Likelihood的差距**
  - 二者之差等于q(z)与真实后验p(z|x,θ)之间的KL Divergence
  - 优化ELBO同时缩小该KL散度

## 课程核心概念总结与课间安排

- **本节核心知识点回顾**
  - Likelihood的定义与最大化目标
  - Monte Carlo Estimation在分布未知时的应用
  - Latent Variable Model的基本框架
  - Evidence Lower Bound的推导及其与Log Likelihood的关系
- **课间休息安排**
  - 确认无提问后安排10分钟课间休息