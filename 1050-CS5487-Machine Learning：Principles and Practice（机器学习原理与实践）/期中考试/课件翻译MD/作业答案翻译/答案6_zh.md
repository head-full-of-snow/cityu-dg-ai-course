> 来源: 6.jpg | 翻译模型: deepseek-v4-flash-0731

@  $ p(x_{1},\ldots,x_{n}|\mu)=\prod_{i}\frac{1}{n2\pi\sigma_{i}^{2}}\exp\left[-\frac{c(x_{i}-\mu)^{2}}{2\sigma_{i}^{2}}\right] $

$ \log p(x_{1}|\mu)=-\frac{1}{2}\sum_{i}\left[\log(2\pi\sigma_{i}^{2})+\frac{c(x_{i}-\mu)^{2}}{\sigma_{i}^{2}}\right] $

$ f(\mu)=-\frac{1}{2}\sum_{i}\frac{n}{2i}\frac{(x_{i}-\mu)^{2}}{\sigma_{i}^{2}}+C $

$ \frac{d\rho}{d\mu}=-\frac{1}{2}\frac{\sum\rho}{2}\frac{d}{d\mu}\left[\frac{x_{i}-\mu)^{2}}{\sigma_{i}^{2}}\right] $

$ \frac{d\rho}{d\mu}=\sum\frac{x_{i}-\mu}{\sigma_{i}^{2}}\sum\frac{x_{i}-\mu}{\sigma_{i}^{2}}=0\quad\therefore\hat{\mu}_{ME}=\frac{\sum\frac{x_{i}}{\sigma_{i}^{2}}-\mu\sum\frac{1}{\sigma_{i}^{2}}}{2}=0 $

权重  $ \rightarrow $  $ \mu_{1}=\frac{1}{\sigma_{2}} $

$$ \widehat{u}=\frac{\sum_{i}\frac{x_{i}}{\sigma^{2}}}{\sum_{i}\frac{1}{\sigma^{2}}}=\frac{\frac{1}{\sigma^{2}}\sum_{i}x_{i}}{\frac{n}{\sigma^{2}}} $$

$$ \widehat{\mu}=\frac{1}{n}\sum x_{i}=\overline{x} $$
