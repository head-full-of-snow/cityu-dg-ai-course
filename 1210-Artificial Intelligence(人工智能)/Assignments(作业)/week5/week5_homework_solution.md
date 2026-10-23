# CS5491 Week 5 Tutorial — Linear Programming: Solutions

## Exercise 1 (Section 2 — Formulation): Garden Sheds

*A small firm builds two types of garden sheds.*
- *Type A requires 2 hours of machine time and 5 hours of craftsman time.*
- *Type B requires 3 hours of machine time and 5 hours of craftsman time.*
- *Each day there are 30 hours of machine time and 60 hours of craftsman time available.*
- *The profit on each Type A shed is \$60 and on each Type B shed is \$84.*

**Formulate the appropriate linear programming problem.**

### (a) Unknowns

$$x = \text{number of Type A sheds built per day}, \qquad y = \text{number of Type B sheds built per day}$$

### (b) Constraints

**Machine time** — each Type A uses 2 h and each Type B uses 3 h, with 30 h available:

$$2x + 3y \leq 30$$

**Craftsman time** — each type uses 5 h, with 60 h available:

$$5x + 5y \leq 60$$

**Non-negativity / integrality** — you cannot build a negative or fractional shed:

$$x \geq 0,\; y \geq 0, \quad x, y \in \mathbb{Z}$$

### (c) Profit

$$P = 60x + 84y$$

### Summary of the linear programming problem

| | |
|---|---|
| **maximize** | $P = 60x + 84y$ |
| **subject to** | $2x + 3y \leq 30$ |
| | $5x + 5y \leq 60$ |
| | $x \geq 0,\; y \geq 0$ and $x, y \in \mathbb{Z}$ |

*(The exercise only asks for the formulation. For completeness, solving it graphically — see figure below — gives corner points (0,0), (12,0), (0,10) and (6,6); the last is the intersection of $2x+3y=30$ and $x+y=12$, and it is already an integer point. The maximum profit is $P = 60\times 6 + 84\times 6 = \boxed{\$864}$ at $x = 6,\; y = 6$.)*

![Exercise 1: feasible region and profit lines](fig_ex1_sheds.png)

---

## Exercise 2 (Section 3 — Graphical Solution): Barley and Swedes

*A farmer has 20 hectares for growing barley and swedes.*
- *Cost: barley \$30/ha, swedes \$20/ha; budget \$480.*
- *Labour: barley 1 man-day/ha, swedes 2 man-days/ha; 36 man-days available.*
- *Profit: barley \$100/ha, swedes \$120/ha.*

**Find the number of hectares of each crop the farmer should sow to maximize profit.**

### (a) Unknowns

$$x = \text{hectares of barley}, \qquad y = \text{hectares of swedes}$$

### (b) Constraints

**Land** — 20 ha in total:

$$x + y \leq 20$$

**Budget** — costs \$30 and \$20 per hectare respectively, \$480 budgeted:

$$30x + 20y \leq 480$$

**Man-days** — 1 and 2 man-days per hectare respectively, 36 available:

$$x + 2y \leq 36$$

**Non-negativity**:

$$x \geq 0, \; y \geq 0$$

*(Hectares may in principle be fractional, so no integrality restriction is imposed.)*

### (c) Profit

$$P = 100x + 120y$$

### Summary of the linear programming problem

| | |
|---|---|
| **maximize** | $P = 100x + 120y$ |
| **subject to** | $x + y \leq 20$ |
| | $30x + 20y \leq 480$ |
| | $x + 2y \leq 36$ |
| | $x \geq 0,\; y \geq 0$ |

### Graphical solution

Plot the three constraint lines and shade out the inadmissible side of each; the remaining (unshaded/blue) region is the feasible region:

![Exercise 2: feasible region and profit lines](fig_ex2_farmer.png)

The family of profit lines $P = 100x + 120y$ (e.g. $P = 1200$, $P = 1800$, $P = 2320$ in the figure) are parallel straight lines. As the line moves towards the top-right corner, the profit increases; the maximum occurs at the **last point touched** before the line leaves the feasible region.

**Corner points of the feasible region** (found by intersecting pairs of binding constraints):

| Corner point | How obtained | Feasible? | $P = 100x + 120y$ |
|---|---|---|---|
| $(0, 0)$ | axes | ✓ | $0$ |
| $(16, 0)$ | $30x+20y=480$ with $y=0$ | ✓ ($16\le 20$, $16\le 36$) | $1600$ |
| $(8, 12)$ | $30x+20y=480 \cap x+y=20$ | ✓ ($8+24=32\le 36$) | $2240$ |
| $(4, 16)$ | $x+y=20 \cap x+2y=36$ | ✓ ($120+320=440\le 480$) | $\mathbf{2320}$ |
| $(0, 18)$ | $x+2y=36$ with $x=0$ | ✓ ($360\le 480$, $18\le 20$) | $2160$ |
| $(6, 15)$ | $30x+20y=480 \cap x+2y=36$ | ✗ ($x+y=21 > 20$) | — |

Details of the two decisive intersections:

- $x+y=20$ and $x+2y=36$: subtracting gives $y = 16$, hence $x = 4$ — feasible, since $30(4)+20(16)=440 \leq 480$.
- $30x+20y=480$ and $x+2y=36$: solving gives $(6, 15)$ — **infeasible**, since $x+y = 21 > 20$.

**Conclusion.** The profit is maximized at $(x, y) = (4, 16)$:

$$P = 100 \times 4 + 120 \times 16 = 400 + 1920 = \$2320$$

The farmer should sow **4 hectares of barley and 16 hectares of swedes**, for a maximum profit of **\$2320**.
