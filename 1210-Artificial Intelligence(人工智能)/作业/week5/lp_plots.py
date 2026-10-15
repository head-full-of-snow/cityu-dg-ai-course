"""Week 5 Linear Programming tutorial — verification & graphical solution figures.

Exercise 1 (garden sheds):  max 60x+84y  s.t. 2x+3y<=30, 5x+5y<=60, x,y>=0 (integers)
Exercise 2 (farmer):        max 100x+120y s.t. x+y<=20, 30x+20y<=480, x+2y<=36, x,y>=0
"""
import itertools
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "."


def feasible1(x, y):
    return ((2 * x + 3 * y <= 30) & (5 * x + 5 * y <= 60)
            & (x >= 0) & (y >= 0))


def feasible2(x, y):
    return ((x + y <= 20) & (30 * x + 20 * y <= 480) & (x + 2 * y <= 36)
            & (x >= 0) & (y >= 0))


# ---------- brute-force verification ----------
best1 = max(
    ((x, y, 60 * x + 84 * y) for x, y in itertools.product(range(31), repeat=2)
     if feasible1(x, y)),
    key=lambda t: t[2])
best2 = max(
    ((x, y, 100 * x + 120 * y) for x, y in itertools.product(range(481), repeat=2)
     if feasible2(x, y)),
    key=lambda t: t[2])
print("Ex1 integer optimum :", best1)   # expect (6, 6, 864)
print("Ex2 LP optimum      :", best2)   # expect (4, 16, 2320)

# also verify the vertex claims of Ex2
for (vx, vy) in [(0, 0), (16, 0), (0, 18), (8, 12), (4, 16), (6, 15)]:
    ok = feasible2(vx, vy)
    print(f"  vertex ({vx:>2},{vy:>2})  feasible={ok}  "
          f"P={100*vx+120*vy if ok else '-'}")

# ---------- plotting helpers ----------
def setup_axes(ax, xmax, ymax, title):
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.set_xlabel("x", style="italic")
    ax.set_ylabel("y", style="italic", rotation=0, labelpad=10)
    ax.set_title(title)
    ax.grid(True, ls=":", lw=0.6, alpha=0.7)


def draw_constraint(ax, fn, xr, label, color):
    xs = np.linspace(0, xr, 400)
    ys = fn(xs)
    ax.plot(xs, ys, color=color, lw=1.6, label=label)


def shade_feasible(ax, feas_fn, xmax, ymax):
    gx, gy = np.meshgrid(np.linspace(0, xmax, 500), np.linspace(0, ymax, 500))
    m = feas_fn(gx, gy)
    ax.imshow(m.astype(float), extent=(0, xmax, 0, ymax),
              origin="lower", cmap="Blues", alpha=0.35,
              vmin=0, vmax=1.6, aspect="auto")


def profit_line(ax, c, a, b, xmax, ymax, label=None, color="green", ls="--"):
    xs = np.linspace(0, xmax, 200)
    ys = (c - a * xs) / b
    mask = ys >= 0
    ax.plot(xs[mask], ys[mask], ls=ls, color=color, lw=1.3, label=label)


# ================= Figure 1 : Exercise 1 =================
fig, ax = plt.subplots(figsize=(7.2, 5.4))
setup_axes(ax, 16, 14, "Exercise 1 (garden sheds): feasible region and profit lines")
draw_constraint(ax, lambda x: (30 - 2 * x) / 3, 15,
                "2x+3y = 30  (machine)", "tab:red")
draw_constraint(ax, lambda x: 12 - x, 12,
                "5x+5y = 60  (craftsman)", "tab:purple")
shade_feasible(ax, feasible1, 16, 14)
for c in (420, 700, 864):
    profit_line(ax, c, 60, 84, 16, 14,
                label=f"P = {c}" if c == 864 else None,
                color="green" if c != 864 else "darkgreen",
                ls="--" if c != 864 else "-")
bbox = dict(fc="white", ec="none", alpha=0.75)
for (vx, vy) in [(0, 0), (12, 0), (0, 10)]:
    ax.plot(vx, vy, "o", ms=6, color="black", zorder=5)
    ax.annotate(f"({vx},{vy})  P={60*vx+84*vy}", (vx, vy),
                textcoords="offset points", xytext=(8, 6), fontsize=9,
                bbox=bbox)
ax.annotate("optimal (6,6)\nP = 864", (6, 6), textcoords="offset points",
            xytext=(25, 35), fontsize=10, fontweight="bold", bbox=bbox,
            arrowprops=dict(arrowstyle="->", color="darkgreen"))
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
fig.savefig(f"{OUT}/fig_ex1_sheds.png", dpi=160)
plt.close(fig)

# ================= Figure 2 : Exercise 2 =================
fig, ax = plt.subplots(figsize=(7.2, 5.4))
setup_axes(ax, 24, 22, "Exercise 2 (farmer): feasible region and profit lines")
draw_constraint(ax, lambda x: 20 - x, 20, "x+y = 20  (land)", "tab:red")
draw_constraint(ax, lambda x: (480 - 30 * x) / 20, 16,
                "30x+20y = 480  (budget)", "tab:purple")
draw_constraint(ax, lambda x: (36 - x) / 2, 36, "x+2y = 36  (man-days)",
                "tab:orange")
shade_feasible(ax, feasible2, 24, 22)
for c in (1200, 1800, 2320):
    profit_line(ax, c, 100, 120, 24, 22,
                label=f"P = {c}" if c == 2320 else None,
                color="green" if c != 2320 else "darkgreen",
                ls="--" if c != 2320 else "-")
bbox = dict(fc="white", ec="none", alpha=0.75)
for (vx, vy) in [(0, 0), (16, 0), (8, 12), (0, 18)]:
    ax.plot(vx, vy, "o", ms=6, color="black", zorder=5)
    ax.annotate(f"({vx},{vy}) P={100*vx+120*vy}", (vx, vy),
                textcoords="offset points", xytext=(8, 6), fontsize=9,
                bbox=bbox)
ax.plot(6, 15, "x", ms=8, color="gray", zorder=5)
ax.annotate("(6,15) infeasible\n(x+y=21>20)", (6, 15),
            textcoords="offset points", xytext=(20, -34), fontsize=8,
            color="gray", bbox=bbox)
ax.annotate("optimal (4,16)\nP = 2320", (4, 16), textcoords="offset points",
            xytext=(25, 20), fontsize=10, fontweight="bold", bbox=bbox,
            arrowprops=dict(arrowstyle="->", color="darkgreen"))
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
fig.savefig(f"{OUT}/fig_ex2_farmer.png", dpi=160)
plt.close(fig)

print("figures saved: fig_ex1_sheds.png, fig_ex2_farmer.png")
