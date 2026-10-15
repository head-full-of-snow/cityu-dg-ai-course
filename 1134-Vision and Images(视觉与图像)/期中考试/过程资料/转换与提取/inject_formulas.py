# -*- coding: utf-8 -*-
"""Inject human-verified LaTeX formulas into PyMuPDF-extracted lecture MDs.
Formulas transcribed from rendered slide images (see .pdf_convert/tiles/)."""
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')

MARK = '> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：\n'

F = {}

F['lec01_filtering'] = {
12: MARK + """
$$G[i,j] = \\sum_{u=-k}^{k}\\sum_{v=-k}^{k} H[u,v]\\,F[i-u,\\ j-v]$$

即卷积运算 $G = H * F$（可视为局部邻域与 kernel 的"点积"）。
""",
32: MARK + """
$$G_{\\sigma_1} * G_{\\sigma_2} = G_{\\sqrt{\\sigma_1^2+\\sigma_2^2}}$$

与自身卷积两次宽度为 $\\sigma$ 的 Gaussian kernel $=$ 用宽度 $\\sqrt{2}\\,\\sigma$ 的 kernel 卷积一次。

二维高斯核（标准形式，同 Tutorial 02）：

$$h_\\sigma(u,v) = \\frac{1}{2\\pi\\sigma^2}\\, e^{-\\frac{u^2+v^2}{2\\sigma^2}}$$
""",
}

F['lec02_edge'] = {
6: MARK + """
$$\\nabla f = \\left[\\frac{\\partial f}{\\partial x},\\ \\frac{\\partial f}{\\partial y}\\right], \\qquad \\|\\nabla f\\| = \\sqrt{\\left(\\tfrac{\\partial f}{\\partial x}\\right)^2+\\left(\\tfrac{\\partial f}{\\partial y}\\right)^2}, \\qquad \\theta = \\tan^{-1}\\!\\left(\\frac{\\partial f/\\partial y}{\\partial f/\\partial x}\\right)$$

梯度方向 = 强度增加最快的方向；**边缘方向与梯度方向正交**。
""",
7: MARK + """
有限差分求导（Option 2，离散导数）= 线性滤波：

$$\\frac{\\partial}{\\partial x} \\approx \\begin{bmatrix}-1 & 0 & 1\\end{bmatrix}, \\qquad \\frac{\\partial}{\\partial y} \\approx \\begin{bmatrix}-1 \\\\ 0 \\\\ 1\\end{bmatrix}$$

写成 3×3 滤波核：

$$H_x = \\begin{bmatrix} 0 & 0 & 0 \\\\ -1 & 0 & 1 \\\\ 0 & 0 & 0 \\end{bmatrix}, \\qquad H_y = \\begin{bmatrix} 0 & -1 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 1 & 0 \\end{bmatrix}$$
""",
11: MARK + """
求导是卷积、卷积满足结合律：

$$\\frac{\\partial}{\\partial x}(f * h) = \\left(\\frac{\\partial}{\\partial x} f\\right) * h = f * \\left(\\frac{\\partial}{\\partial x} h\\right)$$

→ "先平滑再求导"可合并为"直接用高斯导数核卷积"，省一次运算。
""",
12: MARK + """
一维高斯及其导数（解析式）：

$$G_\\sigma(x) = \\frac{1}{\\sqrt{2\\pi}\\,\\sigma} e^{-\\frac{x^2}{2\\sigma^2}}, \\qquad G_\\sigma'(x) = -\\frac{x}{\\sigma^2}\\,G_\\sigma(x)$$
""",
13: MARK + """
二维高斯：

$$h_\\sigma(u,v) = \\frac{1}{2\\pi\\sigma^2}\\, e^{-\\frac{u^2+v^2}{2\\sigma^2}}$$
""",
14: MARK + """
高斯导数（DoG）滤波核，x 方向：

$$\\begin{pmatrix} 1 & 0 & -1 \\\\ 2 & 0 & -2 \\\\ 1 & 0 & -1 \\end{pmatrix}$$

y 方向为其转置。符号约定（正负方向）与 Sobel 相同，仅差系数。
""",
15: MARK + """
Sobel 算子（高斯导数的常用近似）：

$$s_x = \\frac{1}{8}\\begin{pmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{pmatrix}, \\qquad s_y = \\frac{1}{8}\\begin{pmatrix} 1 & 2 & 1 \\\\ 0 & 0 & 0 \\\\ -1 & -2 & -1 \\end{pmatrix}$$

标准定义省略 $\\tfrac{1}{8}$（不影响边缘检测）；要得到正确的梯度幅值需保留 $\\tfrac{1}{8}$。
""",
}

F['lec03_resample'] = {
26: MARK + """
数字图像 = 连续函数的点采样 + 量化：

$$F[x,y] = \\text{quantize}\\big(f(xd,\\ yd)\\big) \\quad (d\\ \\text{为采样间隔，本例 } d=1)$$
""",
28: MARK + """
重建：把离散样本转成连续函数，再与重建滤波器 $h$ 卷积：

$$\\tilde{f} = h * \\tilde{f}_F$$

（$\\tilde{f}_F$ 为离散样本脉冲串；不知道真实 $f$ 时用其近似。）
""",
30: MARK + """
- 帽函数 hat（1D）→ 线性插值；2D 帐篷函数 tent → **双线性插值**（常直接实现，不用显式卷积）。
- 三次重建滤波 → **bicubic**，重建质量更好，是常用选择。
""",
}

F['lec04_harris'] = {
23: MARK + """
窗口 $W$ 平移 $(u,v)$ 的 SSD 误差：

$$E(u,v) = \\sum_{(x,y)\\in W}\\big[I(x+u,\\ y+v) - I(x,y)\\big]^2$$

（$E$ 对所有偏移都大 → 角点。）
""",
24: MARK + """
小运动假设下的泰勒一阶展开：

$$I(x+u,\\ y+v) \\approx I(x,y) + u\\,I_x + v\\,I_y, \\qquad I_x = \\tfrac{\\partial I}{\\partial x},\\ I_y = \\tfrac{\\partial I}{\\partial y}$$
""",
26: MARK + """
代入得二次型近似：

$$E(u,v) \\approx \\sum_{(x,y)\\in W}\\big[u\\,I_x + v\\,I_y\\big]^2 = \\begin{bmatrix}u & v\\end{bmatrix} H \\begin{bmatrix}u \\\\ v\\end{bmatrix} = Au^2 + 2Buv + Cv^2$$

二阶矩矩阵（结构张量）：

$$H = \\sum_{(x,y)\\in W}\\begin{bmatrix} I_x^2 & I_x I_y \\\\ I_x I_y & I_y^2 \\end{bmatrix}, \\qquad A=\\sum I_x^2,\\ B=\\sum I_x I_y,\\ C=\\sum I_y^2$$
""",
30: MARK + """
椭圆等值线方程：

$$\\begin{bmatrix}u & v\\end{bmatrix} H \\begin{bmatrix}u \\\\ v\\end{bmatrix} = \\text{const}$$

轴长由特征值决定（半轴 $\\propto 1/\\sqrt{\\lambda}$），方向由特征向量决定：$\\lambda_{\\max}$=最快变化方向的变化量，$\\lambda_{\\min}$=最慢方向的变化量。
""",
31: MARK + """
特征值回顾（$H$ 为 2×2）：

$$\\det(A-\\lambda I) = 0 \\;\\Rightarrow\\; \\lambda^2 - (h_{11}+h_{22})\\lambda + (h_{11}h_{22}-h_{12}^2) = 0$$

$$\\lambda = \\tfrac{1}{2}\\Big[(h_{11}+h_{22}) \\pm \\sqrt{(h_{11}-h_{22})^2 + 4h_{12}^2}\\Big]$$

求得 $\\lambda$ 后解 $(A-\\lambda I)x = 0$ 得特征向量。
""",
38: MARK + """
Harris 算子（本页定义，$\\lambda_{\\min}$ 的变体，无开方）：

$$f = \\frac{\\lambda_1 \\lambda_2}{\\lambda_1 + \\lambda_2} = \\frac{\\det(H)}{\\operatorname{trace}(H)}$$

（trace$(H)=h_{11}+h_{22}$。）
""",
39: MARK + """
**课程将采用的另一种 Harris 算子定义**（Tutorial 03 同款）：

$$R = \\lambda_1\\lambda_2 - k\\,(\\lambda_1+\\lambda_2)^2 = \\det(M) - k\\cdot\\operatorname{tr}(M)^2, \\quad k \\approx 0.04\\text{~}0.06$$
""",
46: MARK + """
实际用高斯窗加权（而非简单方块窗 $W$）：

$$H = \\sum_{(x,y)\\in W} w_{x,y}\\begin{bmatrix} I_x^2 & I_x I_y \\\\ I_x I_y & I_y^2 \\end{bmatrix}, \\qquad w_{x,y} = \\text{高斯权重（按距中心距离衰减）}$$
""",
}

F['lec05_invariance'] = {
10: MARK + """
尺度不变检测关键思想：在**位置和尺度**上都取 $f$ 的局部最大：

$$f = \\text{Harris 算子（一种 } f \\text{ 的定义）}$$

对每个候选点，画 $f$–尺度曲线，取峰值对应的尺度为该特征的代表尺度。
""",
21: MARK + """
Laplacian of Gaussian（LoG，$f$ 的另一种常用定义；blob 检测）：

$$\\nabla^2 g = \\frac{\\partial^2 g}{\\partial x^2} + \\frac{\\partial^2 g}{\\partial y^2}$$

LoG ≈ DoG（Difference of Gaussians，大高斯减小高斯），DoG 计算更快（SIFT 采用）。
""",
23: MARK + """
尺度选择：半径 $r$ 的圆形 blob，LoG 响应在与 $r$ 成比例的尺度上达到峰值（峰值尺度 $\\sigma \\propto r$，标准结果 $\\sigma = r/\\sqrt{2}$）。该峰值尺度即特征尺度（characteristic scale）。
""",
}

F['lec06_descriptors_matching'] = {
13: MARK + """
MOP（Multiscale Oriented Patches）参数：

- 特征点周围取 $40\\times40$ 窗口 → 缩小到 $1/5$ → 旋转对齐 → 采样 $8\\times8$ 窗口
- 强度归一化：窗口内减均值、除以标准差（光度不变性）
""",
15: MARK + """
SIFT 基本思想（方向直方图）：

- $16\\times16$ 窗口内每像素计算梯度方向 $\\theta(x,y)$（幅值小者剔除）
- 关键点主方向：$36\\text{ bins}\\times10^\\circ$ 的梯度方向直方图取峰值（旋转归一基准）
""",
16: MARK + """
SIFT 完整版：

- $16\\times16$ 窗口分成 $4\\times4$ cell，每 cell 做 $8$ 方向直方图
- 描述子维度 $= 16\\ \\text{cells} \\times 8\\ \\text{orientations} = 128$
""",
27: MARK + """
比值距离（ratio distance）：

$$\\text{ratio} = \\frac{\\|f_1 - f_2\\|}{\\|f_1 - f_2'\\|}$$

（$f_2$ = 最近邻，$f_2'$ = 次近邻。）比值小 → 匹配置信度高；讲义阈值示例 $0.8$；Tutorial 04 代码用 $0.75$。
""",
}

F['lec07_transformations'] = {
11: MARK + """
均匀缩放：

$$S = \\begin{bmatrix} s & 0 \\\\ 0 & s \\end{bmatrix}, \\qquad S^{-1} = \\begin{bmatrix} 1/s & 0 \\\\ 0 & 1/s \\end{bmatrix}$$
""",
12: MARK + """
绕原点旋转 $\\theta$：

$$R = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix}, \\qquad R^{-1} = R^{\\mathsf T} = R(-\\theta)$$
""",
19: MARK + """
齐次坐标：

$$\\begin{bmatrix}x \\\\ y\\end{bmatrix} \\Rightarrow \\begin{bmatrix}x \\\\ y \\\\ 1\\end{bmatrix}, \\qquad \\begin{bmatrix}x \\\\ y \\\\ w\\end{bmatrix} \\Leftrightarrow \\left(x/w,\\ y/w\\right)$$
""",
20: MARK + """
平移（齐次坐标实现）：

$$T = \\begin{bmatrix} 1 & 0 & t_x \\\\ 0 & 1 & t_y \\\\ 0 & 0 & 1 \\end{bmatrix}, \\qquad T\\begin{bmatrix}x \\\\ y \\\\ 1\\end{bmatrix} = \\begin{bmatrix}x+t_x \\\\ y+t_y \\\\ 1\\end{bmatrix}$$
""",
21: MARK + """
仿射变换 = 末行 $[0\\ 0\\ 1]$ 的任意 3×3 矩阵：

$$\\begin{bmatrix} a & b & t_x \\\\ c & d & t_y \\\\ 0 & 0 & 1 \\end{bmatrix}$$
""",
26: MARK + """
投影变换 / 单应（Homography）：放开末行限制（$g,h \\ne 0$，平行线可相交）：

$$H = \\begin{bmatrix} a & b & c \\\\ d & e & f \\\\ g & h & 1 \\end{bmatrix}$$
""",
33: MARK + """
单应的另一种参数化（单位范数约束）：

$$\\begin{bmatrix}x_i' \\\\ y_i' \\\\ 1\\end{bmatrix} \\cong \\begin{bmatrix} h_{00} & h_{01} & h_{02} \\\\ h_{10} & h_{11} & h_{12} \\\\ h_{20} & h_{21} & h_{22} \\end{bmatrix}\\begin{bmatrix}x_i \\\\ y_i \\\\ 1\\end{bmatrix}, \\qquad \\|[h_{00},\\dots,h_{22}]\\| = 1$$

（$\\cong$ 表示差一个尺度因子；每对点提供 2 个方程，**8 个自由度需 4 对点**。）
""",
}

F['lec13_stereo'] = {
6: MARK + """
校正立体对（纯水平平移相机）的视差定义：

$$x_2 - x_1 = \\text{the disparity of pixel }(x_1, y_1)$$

（对应点在同一水平极线上搜索。）
""",
10: MARK + """
SSD 立体匹配：对每个候选视差 $d$ 计算窗口 SSD 代价曲线，取最小：

$$\\hat{d} = \\arg\\min_{d}\\ \\mathrm{SSD}(d)$$
""",
16: MARK + """
立体匹配 = 能量最小化。数据项形式：

$$E(d) = \\sum_{(x,y)\\in I} C\\big(x,\\ y,\\ d(x,y)\\big)$$

（$C$ = 左 $(x,y)$ 与右 $(x+d,\\ y)$ 窗口间的 SSD/匹配代价；一般形式再加平滑项 $+\\lambda\\sum\\rho(d(x,y)-d(x{+}1,y))$。）
""",
24: MARK + """
相似三角形得深度-视差关系：

$$\\text{disparity} = x - x'' = \\frac{B\\,f}{z} \\quad\\Longrightarrow\\quad z = \\frac{f\\,B}{\\text{disparity}}$$

（$f$=焦距，$B$=基线。视差与深度成反比：越近视差越大。）
""",
}

F['lec14_mvs'] = {
23: MARK + """
常用匹配代价（$W$ 为窗口）：

$$\\mathrm{SSD} = \\sum_{(i,j)} W(i,j)\\big[I_1(i,j)-I_2(i,j)\\big]^2, \\qquad \\mathrm{SAD} = \\sum_{(i,j)} W(i,j)\\big|I_1(i,j)-I_2(i,j)\\big|$$

$$\\mathrm{ZNCC} = \\frac{\\sum_{(i,j)} W(i,j)\\big[(I_1-\\overline{I_1})(I_2-\\overline{I_2})\\big]}{\\sigma_{I_1}\\,\\sigma_{I_2}}$$

（NCC/ZNCC 对线性光照变化更鲁棒。）
""",
}

F['lec15_neural_networks'] = {
26: MARK + """
线性分类器几何观点：每类参数定义一张超平面，分数 = 到超平面的（带符号）距离：

$$f(x, W, b) = Wx + b$$
""",
39: MARK + """
Softmax 分类器：把分数解释为未归一化对数概率：

$$p_i = \\frac{e^{s_i}}{\\sum_j e^{s_j}}, \\qquad P(y_i\\mid x_i; W) = \\frac{e^{s_{y_i}}}{\\sum_j e^{s_j}}$$
""",
41: MARK + """
交叉熵损失：

$$L_i = -\\log\\!\\left(\\frac{e^{s_{y_i}}}{\\sum_j e^{s_j}}\\right) = -s_{y_i} + \\log\\sum_j e^{s_j}$$

（最小化负对数似然。）
""",
48: MARK + """
两层神经网络（隐层 100，输入 3072 维，输出 10 类）：

$$f = W_2\\max(0, W_1 x)$$

权重总数 $= 3072\\times100 + 100\\times10 = 308{,}200$。
""",
50: MARK + """
深度网络 = 线性层与非线性激活交替串联：

$$f = W_3\\max\\big(0,\\ W_2\\max(0, W_1 x)\\big)$$

（去掉非线性则整体退化为线性。）
""",
}

F['lec16_cnns_transformers'] = {
8: MARK + """
RNN 循环关系【标准形式】：

$$h_t = \\tanh\\big(W_{hh}h_{t-1} + W_{xh}x_t\\big), \\qquad y_t = W_{hy}h_t$$

隐状态每步更新并反馈回 cell；所有时间步共享同一组权重 $W$。
""",
23: MARK + """
卷积层输出尺寸：

$$\\text{Output} = \\frac{N - F}{\\text{stride}} + 1$$

例：$N=7, F=3$, stride 1 $\\Rightarrow 5$；stride 2 $\\Rightarrow 3$。
""",
44: MARK + """
自注意力【标准公式，幻灯片为示意图】：

$$\\mathrm{Attention}(Q, K, V) = \\mathrm{softmax}\\!\\left(\\frac{QK^{\\mathsf T}}{\\sqrt{d}}\\right)V$$

（Q=query, K=key, V=value；多头 = 多组 QKV 并行再拼接。）
""",
}

for fname, blocks in F.items():
    path = f'期中考试/课件提取MD/{fname}.md'
    src = open(path, encoding='utf-8').read()
    # split into (header, body) sections on '## Slide N'
    parts = re.split(r'(?m)^(## Slide (\d+))$', src)
    # parts: [pre, hdr1, num1, body1, hdr2, num2, body2, ...]
    out = [parts[0]]
    injected = []
    i = 1
    while i < len(parts):
        hdr, num, body = parts[i], int(parts[i+1]), parts[i+2]
        out.append(hdr)
        if num in blocks:
            out.append(body.rstrip() + '\n\n' + blocks[num].rstrip() + '\n')
            injected.append(num)
        else:
            out.append(body)
        i += 3
    open(path, 'w', encoding='utf-8').write(''.join(out))
    print(fname, '-> injected slides:', injected)
print('INJECT DONE')
