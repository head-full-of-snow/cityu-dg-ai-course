"""Concept figures for the LP study guide: three special cases."""
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
matplotlib.rcParams["axes.unicode_minus"] = False
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 400)
fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2))

# ---- (a) infeasible: x >= 4 and x <= 2 ----
ax = axes[0]
ax.fill_between(x, 0, 10, where=x <= 2, color="skyblue", alpha=0.4)
ax.fill_between(x, 0, 10, where=x >= 4, color="lightgreen", alpha=0.4)
ax.axvline(2, color="tab:red", lw=1.8)
ax.axvline(4, color="tab:purple", lw=1.8)
ax.text(1.0, 5, "x ≤ 2\n区域", ha="center", fontsize=10, color="tab:red")
ax.text(7.0, 5, "x ≥ 4\n区域", ha="center", fontsize=10, color="tab:purple")
ax.text(3.0, 8.6, "无交集 →\n无可行解", ha="center", fontsize=11,
        fontweight="bold", color="black",
        bbox=dict(fc="white", ec="gray", alpha=0.9))
ax.set_title("(a) 无可行解 Infeasible", fontsize=12)
ax.set_xlim(0, 10); ax.set_ylim(0, 10)

# ---- (b) unbounded: x + y >= 2, maximize x + y ----
ax = axes[1]
ax.fill_between(x, 0, 10, where=(x + 0) >= 0, color="none")
gx, gy = np.meshgrid(np.linspace(0, 10, 300), np.linspace(0, 10, 300))
m = (gx + gy >= 2)
ax.imshow(m.astype(float), extent=(0, 10, 0, 10), origin="lower",
          cmap="Blues", alpha=0.35, vmin=0, vmax=1.8, aspect="auto")
ax.plot(x, 2 - x, color="tab:red", lw=1.8, label="x + y = 2")
for c, ls in [(3, "--"), (6, "--")]:
    ys = c - x
    ax.plot(x[ys >= 0], ys[ys >= 0], ls=ls, color="green", lw=1.3)
ax.annotate("", xy=(9.2, 8.4), xytext=(6.2, 5.4),
            arrowprops=dict(arrowstyle="->", color="darkgreen", lw=2))
ax.text(5.6, 6.2, "利润线可无限\n向右上平移\n→ 无界解", fontsize=10,
        fontweight="bold",
        bbox=dict(fc="white", ec="gray", alpha=0.9))
ax.legend(loc="lower right", fontsize=9)
ax.set_title("(b) 无界解 Unbounded（max x+y）", fontsize=12)
ax.set_xlim(0, 10); ax.set_ylim(0, 10)

# ---- (c) multiple optima: feasible triangle, objective parallel to an edge ----
ax = axes[2]
gx, gy = np.meshgrid(np.linspace(0, 10, 300), np.linspace(0, 10, 300))
m = (gx + gy <= 8) & (gy <= 6) & (gx <= 7)
ax.imshow(m.astype(float), extent=(0, 10, 0, 10), origin="lower",
          cmap="Blues", alpha=0.35, vmin=0, vmax=1.8, aspect="auto")
ax.plot(x, 8 - x, color="tab:red", lw=1.8, label="x + y ≤ 8")
ax.axhline(6, 0, 0.7, color="tab:purple", lw=1.8, label="y ≤ 6")
ax.axvline(7, 0, 0.8, color="tab:orange", lw=1.8, label="x ≤ 7")
ax.plot(x, 6 - x, ls="--", color="green", lw=1.6,
        label="P=x+y (与红边平行)")
ax.plot([2, 6], [6, 2], "o", ms=7, color="black", zorder=5)
ax.plot([2, 6], [6, 2], "-", lw=3, color="darkgreen", alpha=0.6)
ax.text(2.1, 6.35, "(2,6)", fontsize=10)
ax.text(6.1, 2.0, "(6,2)", fontsize=10)
ax.text(0.6, 3.4, "整条绿边\n上任意点\nP = 8", fontsize=10, fontweight="bold",
        bbox=dict(fc="white", ec="gray", alpha=0.9))
ax.legend(loc="upper right", fontsize=8)
ax.set_title("(c) 无穷多最优解 Multiple Optima", fontsize=12)
ax.set_xlim(0, 10); ax.set_ylim(0, 10)

for ax in axes:
    ax.set_xlabel("x", style="italic")
    ax.set_ylabel("y", style="italic", rotation=0, labelpad=10)
    ax.grid(True, ls=":", lw=0.5, alpha=0.6)

fig.tight_layout()
fig.savefig("fig_lp_special_cases.png", dpi=150)
print("saved fig_lp_special_cases.png")
