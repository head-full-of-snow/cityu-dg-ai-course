# Stereo as energy minimization

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2F0bf673d1eb89448ca5c7c9f7bb58a7d8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=B1LcJ8nn0a0YR6hhDL2kWLOPrA8%3D)

$ C(x, y, d) $; the disparity space image (DSI)

# Stereo as energy minimization

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2Ffe44726022ea4612bee73155643f00df.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=E3IWejIk1tCGpLZeLkEzp33HnwY%3D)

Simple pixel / window matching: choose the minimum of each column in the DSI independently:

$$ d(x,y)=\arg\min C(x,y,d^{\prime}) $$

# Greedy selection of best match

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2F58b4c35b23014e209632c0987c9cddc2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=T65XjzYzymd7boxQDyfKeeORskA%3D)

# Stereo as energy minimization

• Better objective function

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2F6dad668f8b3c4c08afa3ac490598405c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=npDAcpXOwpG3YZ77qvXho0nbt78%3D)

# Stereo as energy minimization

$$ E(d)=E_{d}(d)+\lambda E_{s}(d) $$

match cost:

$$ E_{d}(d)=\sum_{(x,y)\in I}C(x,y,d(x,y)) $$

smoothness cost:

$$ E_{s}(d)=\sum_{(p,q)\in\mathcal{E}}V(d_{p},d_{q}) $$

E : set of neighboring pixels

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2Fd3e63036f3f34712bf2045fc4e8433ac.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=f%2F%2FY6YNfDSW6VOsfLdnAFDXw5jY%3D)

Smoothness cost

$$ \begin{array}{r l r}&{}&{E_{s}(d)=\displaystyle\sum_{V(d_{p},d_{q})}}\\ &{}&{(p,q)\in\mathcal{E}}\\ &{}&{\mathrm{H o w~d o~w e~c h o o s e~}V?}\end{array} $$

$$ V(d_{p},d_{q})=|d_{p}-d_{q}| \quad \text{L}_{1}\text{distance} $$

$$ V(d_{p},d_{q})=\begin{cases}0&if d_{p}=d_{q}\\1&if d_{p}\neq d_{q}\end{cases} $$

# Smoothness cost

$$ E(d)=E_{d}(d)+\lambda E_{s}(d) $$

• If  $ \lambda = \infty $ is infinity, then we only consider smoothness

• Optimal solution is a surface of constant depth/disparity

– Fronto-parallel surface

• In practice, want to balance data term with smoothness term

# Depth from disparity

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F85ce5ac6ad44460ba8016aa56f907af9%2Fmedia%2Fea244e9ea8924be491f1cea3056520f2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256939&Signature=r5HC4gZD4wFPGEuHfcqsXWXeUZo%3D)

$$ disparity=x-x^{\prime}=\frac{baseline*f}{z} $$
