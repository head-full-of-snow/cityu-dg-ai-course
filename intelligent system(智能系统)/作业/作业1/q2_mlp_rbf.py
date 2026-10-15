# 作业1
# 输入 x1、x2 ∈ {0,1},目标 t ∈ {0,1}

import matplotlib.pyplot as plt
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

# XOR的四种输入
X = np.array([[0.0, 0.0],
              [0.0, 1.0],
              [1.0, 0.0],
              [1.0, 1.0]])
T = np.array([0.0, 1.0, 1.0, 0.0])


def sigmoid(u):
    return 1.0 / (1.0 + np.exp(-u))


# (a) MLP 2-2-1,逐样本反向传播
def train_mlp(X, T, lr=0.5, max_epochs=20000, sse_stop=1e-3, seed=7):
    rng = np.random.default_rng(seed)
    W1 = rng.uniform(-1.0, 1.0, size=(2, 2))   # 输入->隐层
    b1 = rng.uniform(-1.0, 1.0, size=2)
    W2 = rng.uniform(-1.0, 1.0, size=2)        # 隐层->输出
    b2 = rng.uniform(-1.0, 1.0)

    history = []
    for epoch in range(1, max_epochs + 1):
        for x, t in zip(X, T):
            # 前向计算
            h = sigmoid(W1 @ x + b1)
            y = sigmoid(W2 @ h + b2)
            # 反向传播,依次算输出层和隐层的delta
            delta_out = (t - y) * y * (1.0 - y)
            delta_hid = delta_out * W2 * h * (1.0 - h)
            W2 = W2 + lr * delta_out * h
            b2 = b2 + lr * delta_out
            W1 = W1 + lr * np.outer(delta_hid, x)
            b1 = b1 + lr * delta_hid
        sse = sum((sigmoid(W2 @ sigmoid(W1 @ x + b1) + b2) - t) ** 2
                  for x, t in zip(X, T))
        history.append(sse)
        if sse < sse_stop:
            break

    def net(x):
        return sigmoid(W2 @ sigmoid(W1 @ x + b1) + b2)

    return net, history


mlp_net, mlp_hist = train_mlp(X, T)
mlp_out = np.array([mlp_net(x) for x in X])

print("Q2(a) MLP 2-2-1,单极性sigmoid,BP算法(lr=0.5)")
print(f"SSE < 1e-3 时停止,训练了 {len(mlp_hist)} 轮,最终SSE = {mlp_hist[-1]:.2e}\n")
print("  输入      目标    MLP输出")
for x, t, y in zip(X, T, mlp_out):
    print(f"  {x.astype(int)}      {t:.0f}      {y:.4f}")
print("  按0.5分类:", ["OK" if (y > 0.5) == (t > 0.5) else "WRONG"
                    for y, t in zip(mlp_out, T)], "\n")


# (b) RBF网络:4个高斯隐单元,中心取4个训练样本,输出层线性、用delta规则训练
def gaussian_rbf(x, c, sigma):
    return np.exp(-np.sum((x - c) ** 2) / (2.0 * sigma ** 2))


def train_rbf(X, T, sigma=0.5, lr=0.1, max_epochs=500, sse_stop=1e-8):
    C = X.copy()
    Phi = np.array([[gaussian_rbf(x, c, sigma) for c in C] for x in X])
    w = np.zeros(len(C))

    # 伪逆求出的最小二乘解,用来和训练结果对照
    w_ls = np.linalg.pinv(Phi) @ T

    history = []
    for epoch in range(1, max_epochs + 1):
        for phi, t in zip(Phi, T):
            y = w @ phi
            w = w + lr * (t - y) * phi
        sse = np.sum((Phi @ w - T) ** 2)
        history.append(sse)
        if sse < sse_stop:
            break

    def net(x):
        phi = np.array([gaussian_rbf(x, c, sigma) for c in C])
        return w @ phi

    return net, history, w, w_ls, C


rbf_net, rbf_hist, rbf_w, rbf_w_ls, centers = train_rbf(X, T)
rbf_out = np.array([rbf_net(x) for x in X])

print("Q2(b) RBF网络,4个高斯隐单元(sigma=0.5),线性输出(LMS)")
print(f"训练了 {len(rbf_hist)} 轮,最终SSE = {rbf_hist[-1]:.2e}")
print(f"delta规则训练的输出权值:{np.round(rbf_w, 4)}")
print(f"伪逆解的输出权值        :{np.round(rbf_w_ls, 4)}\n")
print("  输入      目标    RBF输出")
for x, t, y in zip(X, T, rbf_out):
    print(f"  {x.astype(int)}      {t:.0f}      {y:.4f}")
print("  按0.5分类:", ["OK" if (y > 0.5) == (t > 0.5) else "WRONG"
                    for y, t in zip(rbf_out, T)], "\n")


# 画网络在整个输入平面上的输出,黑色线是0.5等值线
def plot_output_map(ax, net, title, show_centers=False):
    g1, g2 = np.meshgrid(np.linspace(-0.4, 1.4, 300),
                         np.linspace(-0.4, 1.4, 300))
    Z = np.array([[net(np.array([a, b])) for a, b in zip(row1, row2)]
                  for row1, row2 in zip(g1, g2)])
    cs = ax.contourf(g1, g2, Z, levels=np.linspace(0, 1, 21), cmap="RdBu_r")
    ax.contour(g1, g2, Z, levels=[0.5], colors="k", linewidths=2)
    fig.colorbar(cs, ax=ax, label="network output")
    for x, t in zip(X, T):
        ax.scatter(x[0], x[1], c="yellow" if t == 1 else "cyan",
                   s=130, edgecolors="k", marker="o" if t == 1 else "s",
                   zorder=3)
    if show_centers:
        ax.scatter(centers[:, 0], centers[:, 1], marker="x",
                   s=90, c="lime", linewidths=2.5, zorder=4,
                   label="RBF centers")
        ax.legend(loc="upper right", fontsize=8)
    ax.set_xlim(-0.4, 1.4)
    ax.set_ylim(-0.4, 1.4)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_title(title)


# MLP的图
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.5))
fig.suptitle("Q2(a) MLP 2-2-1, sigmoid, back-propagation (lr=0.5)",
             fontsize=13)
ax = axes[0]
ax.semilogy(range(1, len(mlp_hist) + 1), mlp_hist, color="tab:blue")
ax.set_title(f"SSE vs epoch ({len(mlp_hist)} epochs)")
ax.set_xlabel("epoch")
ax.set_ylabel("SSE (log)")
ax.grid(alpha=0.3)
plot_output_map(axes[1], mlp_net,
                "Decision boundary (output = 0.5)\n"
                f"outputs: {np.round(mlp_out, 3)}")
fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(os.path.join(OUT, "q2_mlp.png"), dpi=150)
print("saved: figures/q2_mlp.png")

# RBF的图
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.5))
fig.suptitle("Q2(b) RBF network, Gaussian units (centers = 4 samples, "
             "sigma = 0.5)", fontsize=13)
ax = axes[0]
ax.semilogy(range(1, len(rbf_hist) + 1), rbf_hist, color="tab:green")
ax.set_title(f"SSE vs epoch ({len(rbf_hist)} epochs)")
ax.set_xlabel("epoch")
ax.set_ylabel("SSE (log)")
ax.grid(alpha=0.3)
plot_output_map(axes[1], rbf_net,
                "Network output (boundary at 0.5)\n"
                f"outputs: {np.round(rbf_out, 3)}", show_centers=True)
fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(os.path.join(OUT, "q2_rbf.png"), dpi=150)
print("saved: figures/q2_rbf.png")
