# Assignment 1 — Perceptron, ADALINE, MLP and RBF Networks

All experiments are implemented in pure Python (NumPy + Matplotlib), no
neural-network toolbox is used. Random seeds are fixed, so every number and
figure below is reproducible.

## Files

| File | Content |
|---|---|
| `q1_perceptron_adaline.py` | Q1: bipolar Perceptron + ADALINE on OR / XOR |
| `q2_mlp_rbf.py`            | Q2: sigmoid MLP + Gaussian RBF network on XOR |
| `figures/q1_convergence.png`         | Q1 convergence behaviours |
| `figures/q1_decision_boundaries.png` | Q1 decision boundaries |
| `figures/q2_mlp.png`                 | Q2 MLP: SSE curve + output map |
| `figures/q2_rbf.png`                 | Q2 RBF: SSE curve + output map |

Run with:

```bash
python q1_perceptron_adaline.py
python q2_mlp_rbf.py
```

---

## Q1 — Perceptron (bipolar) & ADALINE on OR and XOR

**Setup.** Bipolar inputs `x1, x2 ∈ {−1, +1}`, bipolar targets `t ∈ {−1, +1}`.

| Model | Activation | Learning rule | lr | Init |
|---|---|---|---|---|
| Perceptron | `f(net) = +1 if net ≥ 0 else −1` | error-correction `w ← w + lr·(t−y)·x` (update only when misclassified) | 1.0 | random U(−0.5, 0.5) |
| ADALINE | linear during learning, bipolar step for classification | LMS / delta rule `w ← w + lr·(t−net)·x` | 0.05 | random U(−0.5, 0.5) |

### Results

| Model | Data | Convergence | Final result |
|---|---|---|---|
| Perceptron | **OR** | **converged in 3 epochs** (0 errors) | w = [2.27, 1.94], b = 2.0 — 4/4 correct |
| Perceptron | **XOR** | **never converges** — #errors oscillates forever | best epochs still get only 3/4 |
| ADALINE | **OR** | SSE converges smoothly to **1.0** | w → [0.49, 0.47], b → 0.50 — 4/4 correct |
| ADALINE | **XOR** | SSE converges to **4.0** | weights decay to ≈ 0 — classification fails |

### Observations

1. **OR is linearly separable**, so the Perceptron learning rule is guaranteed
   to converge (perceptron convergence theorem) — here in 3 epochs.
2. **XOR is not linearly separable**: no straight line can separate the two
   classes, so the Perceptron error-correction rule keeps oscillating forever
   and ADALINE cannot classify it either.
3. ADALINE minimises the squared error, so it always settles at the
   **least-squares optimum**, which can be computed analytically
   (`w = (AᵀA)⁻¹Aᵀt`):
   * OR: `w = [0.5, 0.5], b = 0.5`, minimum SSE = **1.0** — the SSE cannot
     reach 0 with bipolar ±1 targets, yet `sign(w·x+b)` still classifies all
     4 patterns correctly.
   * XOR: `w = [0, 0], b = 0`, minimum SSE = **4.0** — the best linear map is
     the trivial one that predicts ≈ 0 everywhere (‖t‖² = 4). This is the
   clearest demonstration that a *single* linear neuron cannot solve XOR.
4. Difference between the two rules: the Perceptron updates only on
   misclassification (its error curve is a step-like oscillation), while
   ADALINE updates continuously and therefore has a smooth, monotonically
   settling SSE curve.

---

## Q2 — MLP (unipolar sigmoid) & RBF (Gaussian) on XOR

**Setup.** Binary inputs `x1, x2 ∈ {0, 1}`, targets `t ∈ {0, 1}`:
`(0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0`.

### (a) MLP 2–2–1, back-propagation

* Hidden and output units: unipolar sigmoid `f(u) = 1/(1+e^(−u))`
* Sequential (pattern-by-pattern) back-propagation, lr = 0.5, seed = 7
* Stopped when SSE < 10⁻³

**Converged in 12,393 epochs (final SSE = 1.0 × 10⁻³).**
The SSE curve shows the classic XOR plateau (SSE ≈ 0.5 for several thousand
epochs) followed by a rapid descent — plain gradient descent escapes this
plateau very slowly.

Output values for the four training samples:

| input | target | MLP output |
|:---:|:---:|:---:|
| (0, 0) | 0 | **0.0145** |
| (0, 1) | 1 | **0.9835** |
| (1, 0) | 1 | **0.9835** |
| (1, 1) | 0 | **0.0156** |

All four patterns classified correctly (threshold 0.5).

*Remark:* with unlucky initialisations the 2–2–1 network can stall forever in
the local minimum at SSE ≈ 0.5 where two outputs stay near 0.48 — observed
e.g. with seeds 2, 11, 42. Re-initialising the weights resolves it.

### (b) RBF network with Gaussian hidden units

* 4 Gaussian hidden units, centers = the 4 training samples:
  `φ_j(x) = exp(−‖x − c_j‖² / (2σ²))`, σ = 0.5
* Linear output layer trained with the delta rule (lr = 0.1);
  the pseudo-inverse solution `w = Φ⁺t` is computed as a cross-check and
  matches the LMS-trained weights to 4 decimals.

**Converged in 157 epochs (final SSE = 9 × 10⁻⁹).**

Output values for the four training samples:

| input | target | RBF output |
|:---:|:---:|:---:|
| (0, 0) | 0 | **0.0001** |
| (0, 1) | 1 | **1.0000** |
| (1, 0) | 1 | **1.0000** |
| (1, 1) | 0 | **0.0000** |

LMS-trained output weights: `[−0.281, 1.057, 1.057, −0.281]`
(same as the pseudo-inverse solution).

### Observations

1. Both networks solve XOR, which neither single-layer model could — the
   hidden layer provides the nonlinearity needed to bend the decision surface
   (MLP) or to place localised bumps on it (RBF).
2. The RBF network converges **two orders of magnitude faster** than the MLP
   (157 vs 12,393 epochs): only the linear output weights are learned, so the
   problem becomes linear regression in the hidden space, at the cost of
   having to choose the centers/spread in advance.
3. The RBF outputs are essentially exact (SSE ≈ 10⁻⁸) because with one center
   per training sample the interpolation matrix is invertible, while the MLP
   outputs saturate gradually (SSE ≈ 10⁻³) since sigmoid units approach 0/1
   only asymptotically.
