# 作业1 Q1:双极性感知机和ADALINE,对OR和XOR数据做分类
# 输入是双极性的,x1、x2 ∈ {-1, +1}

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

rng = np.random.default_rng(42)

# OR线性可分,XOR线性不可分
X = np.array([[-1.0, -1.0],
              [-1.0,  1.0],
              [ 1.0, -1.0],
              [ 1.0,  1.0]])
T_OR  = np.array([-1.0, 1.0, 1.0, 1.0])
T_XOR = np.array([-1.0, 1.0, 1.0, -1.0])


def bipolar(net):
    # 双极性阶跃函数
    return np.where(net >= 0.0, 1.0, -1.0)


def train_perceptron(X, T, lr=1.0, max_epochs=60):
    # 感知机误差修正学习,只在样本分错时更新
    w = rng.uniform(-0.5, 0.5, size=2)
    b = 0.0
    history = []
    for epoch in range(1, max_epochs + 1):
        errors = 0
        for x, t in zip(X, T):
            y = bipolar(w @ x + b)
            if y != t:
                w = w + lr * (t - y) * x
                b = b + lr * (t - y)
                errors += 1
        history.append(errors)
        if errors == 0:   # 这轮全部分对,收敛了
            break
    return w, b, history


def train_adaline(X, T, lr=0.05, max_epochs=300):
    # ADALINE对线性输出net用delta规则学习,分类时才过阶跃函数
    w = rng.uniform(-0.5, 0.5, size=2)
    b = rng.uniform(-0.5, 0.5)
    history = []
    for epoch in range(1, max_epochs + 1):
        for x, t in zip(X, T):
            net = w @ x + b
            err = t - net
            w = w + lr * err * x
            b = b + lr * err
        history.append(np.sum((T - (X @ w + b)) ** 2))   # 记录每轮的SSE
    return w, b, history


w_p_or, b_p_or, hist_p_or = train_perceptron(X, T_OR)
w_p_xor, b_p_xor, hist_p_xor = train_perceptron(X, T_XOR, max_epochs=30)  # XOR不会收敛,跑30轮看情况
w_a_or, b_a_or, hist_a_or = train_adaline(X, T_OR)
w_a_xor, b_a_xor, hist_a_xor = train_adaline(X, T_XOR)


def report(name, w, b, T):
    net = X @ w + b
    y = bipolar(net)
    print("---", name, "---")
    print(f"w = [{w[0]:.4f}, {w[1]:.4f}], b = {b:.4f}")
    for i in range(4):
        print(f"x = {X[i].astype(int)}  net = {net[i]:+.4f}  "
              f"y = {y[i]:+.0f}  t = {T[i]:+.0f}  "
              f"{'OK' if y[i] == T[i] else 'WRONG'}")
    print(f"正确 {int(np.sum(y == T))}/4\n")


print("Q1 感知机(双极性) & ADALINE")
if hist_p_or[-1] == 0:
    print(f"感知机 OR :{len(hist_p_or)} 轮收敛")
else:
    print("感知机 OR :未收敛")
print(f"感知机 XOR:{len(hist_p_xor)} 轮后仍不收敛,错误数来回震荡\n")
report("感知机 OR", w_p_or, b_p_or, T_OR)
report("感知机 XOR", w_p_xor, b_p_xor, T_XOR)
report("ADALINE OR", w_a_or, b_a_or, T_OR)
report("ADALINE XOR", w_a_xor, b_a_xor, T_XOR)

# 图1:收敛过程
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
fig.suptitle("Q1 convergence (bipolar inputs)", fontsize=14)

ax = axes[0, 0]
ax.plot(range(1, len(hist_p_or) + 1), hist_p_or, "o-", color="tab:green")
ax.set_title(f"(a) Perceptron, OR: converged in {len(hist_p_or)} epochs")
ax.set_xlabel("epoch"); ax.set_ylabel("#errors"); ax.set_ylim(-0.3, 4.3)
ax.grid(alpha=0.3)

ax = axes[0, 1]
ax.plot(range(1, len(hist_p_xor) + 1), hist_p_xor, "s-", color="tab:red")
ax.set_title("(b) Perceptron, XOR: never converges")
ax.set_xlabel("epoch"); ax.set_ylabel("#errors"); ax.set_ylim(-0.3, 4.3)
ax.grid(alpha=0.3)

# SSE稳定到的1.0和4.0就是最小二乘的最优值
ax = axes[1, 0]
ax.plot(range(1, len(hist_a_or) + 1), hist_a_or, "-", color="tab:blue")
ax.axhline(1.0, ls="--", color="k", lw=1)
ax.set_title("(c) ADALINE, OR: SSE -> 1.0")
ax.set_xlabel("epoch"); ax.set_ylabel("SSE"); ax.grid(alpha=0.3)

ax = axes[1, 1]
ax.plot(range(1, len(hist_a_xor) + 1), hist_a_xor, "-", color="tab:purple")
ax.axhline(4.0, ls="--", color="k", lw=1)
ax.set_title("(d) ADALINE, XOR: SSE -> 4.0")
ax.set_xlabel("epoch"); ax.set_ylabel("SSE"); ax.grid(alpha=0.3)

fig.tight_layout(rect=[0, 0, 1, 0.95])
fig.savefig(os.path.join(OUT, "q1_convergence.png"), dpi=150)
print("saved: figures/q1_convergence.png")

# 图2:四个模型最后的决策域和分界线
def plot_boundary(ax, w, b, T, title):
    g1, g2 = np.meshgrid(np.linspace(-2, 2, 400), np.linspace(-2, 2, 400))
    Z = bipolar(w[0] * g1 + w[1] * g2 + b)
    ax.contourf(g1, g2, Z, levels=[-2, 0, 2],
                colors=["#dbe9ff", "#ffd9d9"], alpha=0.7)
    xs = np.linspace(-2, 2, 10)
    if abs(w[1]) > 1e-12:
        ax.plot(xs, -(w[0] * xs + b) / w[1], "k-", lw=2)
    for x, t in zip(X, T):
        ax.scatter(x[0], x[1],
                   c="red" if t == 1 else "royalblue", s=130,
                   edgecolors="k", marker="o" if t == 1 else "s", zorder=3)
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.grid(alpha=0.3)
    ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$"); ax.set_title(title)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
fig.suptitle("Q1 decision boundaries (red = class +1, blue = class -1)",
             fontsize=13)
plot_boundary(axes[0], w_p_or, b_p_or, T_OR, "Perceptron, OR")
plot_boundary(axes[1], w_a_or, b_a_or, T_OR, "ADALINE, OR")
plot_boundary(axes[2], w_p_xor, b_p_xor, T_XOR, "Perceptron, XOR (cannot separate)")
plot_boundary(axes[3], w_a_xor, b_a_xor, T_XOR, "ADALINE, XOR (cannot separate)")
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig(os.path.join(OUT, "q1_decision_boundaries.png"), dpi=150)
print("saved: figures/q1_decision_boundaries.png")
