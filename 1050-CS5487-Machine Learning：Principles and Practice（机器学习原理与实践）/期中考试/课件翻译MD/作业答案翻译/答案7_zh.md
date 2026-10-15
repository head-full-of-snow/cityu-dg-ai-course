> 来源: 7.jpg | 翻译模型: deepseek-v4-flash-0731

@  $ P(w|x) \propto P(x|w)P(w) $

似然  $ P(x|w) \propto \exp\left[-\frac{1}{2\sigma^{2}} \sum_{i} (x_{i} - w)^{2}\right] $

先验：  $ P(w) \propto e^{-\lambda(w)} $

$ P(w|x) \propto \exp\left[-\frac{1}{2\sigma^{2}} \sum_{i} (x_{i} - w)^{2} - \lambda(w)\right] $

负对数  $ L(w) = \frac{1}{2\sigma^{2}} \sum_{i} (x_{i} - w)^{2} + \lambda(w) $

②  $ \sum_{i}(x_{i}-w)^{2}=\sum_{i}(x_{i}-x)^{2}+n(w-x)^{2} $

$ L(w)=\frac{n}{2\sigma^{2}}(w-\bar{x})^{2}+N(w)+C $

$$ \frac{n}{62}(W-B E)+\lambda=0 $$

$$ \therefore w=\overline{x}-\frac{x^{2}}{n} $$

$ \Delta:f:w<0 $

$ \frac{dL}{dW}=\frac{n}{\sigma^{2}}c(W-x)-1\rightarrow\frac{n}{\sigma^{2}}c(W-x)-1=0 $

$ \therefore W=x+\frac{x\sigma^{2}}{n}<0 $

$$ \overline{x}>\frac{\lambda\sigma^{2}}{n} $$

$$ \widehat{W}=\overline{x}-\frac{\lambda\sigma^{2}}{n} $$

$$ \overline{x}<\frac{-\lambda\sigma^{2}}{n} $$

$$ \hat{w}=\overline{x}+\frac{\lambda\overline{x}}{\overline{n}} $$

$$ \vert x\vert\leq\frac{x\vert\frac{1}{n}\vert}{n} $$

$$ \widehat{w}=0 $$
