Integer Programming
CS5491: Artificial Intelligence
Zhichao Lu
Content Credits:
Prof. Wei
's CS4486 Course
and
Prof. Boddeti
's AI Course

## Today

- Formulate decisions with integer and binary variables.
- Use an LP relaxation to bound an integer program.
- Solve an integer program by branch and bound.

## LP Recap: The Diet Problem

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).
$$\begin{aligned}
        \min\quad &x_1+0.4x_2\\
        \text{s.t.}\quad &2000\le100x_1+50x_2\le2500,\\
        &3x_1+4x_2\le100,\\
        &20x_1+70x_2\ge700,\\
        &x_1,x_2\ge0.
        \end{aligned}$$
Unique optimum: $(12,16)$.
Minimum cost: $18.4$.

## Finding a Vertex

Choose $n$ independent constraint boundaries for $n$ variables.
Diet example
Calorie minimum and sugar limit:
$$\begin{aligned}100x_1+50x_2&=2000,\\3x_1+4x_2&=100.\end{aligned}$$
Solving gives $(x_1,x_2)=(12,16)$.
Notation for $A\mathbf{x}\le\mathbf{b}$
$I$: indices of the selected constraints.
$A_I$: selected rows of $A$.
$\mathbf{b}_I$: matching entries of $\mathbf{b}$.
Set these constraints to equality:
$$A_I\mathbf{x}=\mathbf{b}_I.$$
Check
all original constraints
before accepting the point as a vertex.

## Discrete Decisions

| Decision Variable Domain
| Number of fixed 8 oz servings $n$ $\mathbb{Z}_{\ge0}$
| Whether to select an item $z$ $\{0,1\}$
| Amount of a divisible resource $t$ $\mathbb{R}_{\ge0}$
Define the unit before writing the model.
For $n$ servings of 8 oz stir-fry: amount $=8n$ oz, cost $=8n$, calories $=800n$.

## LP, ILP and MILP

Linear objective and linear constraints:
$$\min_{\mathbf{x}}\ \mathbf{c}^T\mathbf{x}\qquad\text{subject to }A\mathbf{x}\le\mathbf{b}.$$
| Model Variable domains
| Linear program (LP) $x_i\in\mathbb{R}$ for all $i$
| Pure integer linear program (ILP) $x_i\in\mathbb{Z}$ for all $i$
| Binary integer program $x_i\in\{0,1\}$ for all $i$
| Mixed-integer linear program (MILP) Some variables integer; others continuous

## Integer Programming Example

$$\begin{aligned}
        \min_{x,y}\quad &z=x-4y\\
        \text{subject to}\quad &-10x+20y\le22,\\
        &5x+10y\le49,\\
        &0\le x\le5,\quad y\ge0,\\
        &x,y\in\mathbb{Z}.
        \end{aligned}$$
We will use this model for relaxation, rounding and branching.

## Integer Feasible Points

LP: every point in the shaded region. IP: only the integer points inside it.

## LP Relaxation

Integer program
$$\begin{aligned}\min\quad&\mathbf{c}^T\mathbf{x}\\\text{s.t.}\quad&A\mathbf{x}\le\mathbf{b},\\&\mathbf{x}\in\mathbb{Z}^n.\end{aligned}$$
LP relaxation
$$\begin{aligned}\min\quad&\mathbf{c}^T\mathbf{x}\\\text{s.t.}\quad&A\mathbf{x}\le\mathbf{b},\\&\mathbf{x}\in\mathbb{R}^n.\end{aligned}$$
Drop integrality. Keep the objective, constraints and variable bounds.

## Why Relaxation Gives a Bound

Every integer feasible point is also LP feasible:
$$P_{\mathrm{IP}}\subseteq P_{\mathrm{LP}}.$$
Minimizing over a larger set cannot increase the optimum:
$$z^*_{\mathrm{LP}}\le z^*_{\mathrm{IP}}.$$
The LP optimum is a
lower bound
for minimization.

## Connection to Informed Search

- In informed search, solving a relaxed problem can give an optimistic cost estimate.
- At a branch-and-bound node, the LP relaxation bounds the best integer solution allowed by that node.
- This bound helps rule out branches that cannot improve the current solution.
A* uses $g(n)+h(n)$ to estimate total cost. Here, the node LP bounds the
total objective directly
.

## Check Your Understanding

For a minimization IP and its LP relaxation with finite optima:
| Statement Always true?
| $z^*_{\mathrm{LP}}\le z^*_{\mathrm{IP}}$ Yes: the LP has a larger feasible set.
| $\mathbf{x}^*_{\mathrm{LP}}=\mathbf{x}^*_{\mathrm{IP}}$ No: the LP optimum may be fractional.
| An LP-optimal point with integer coordinates solves the IP. Yes: it is feasible and reaches the lower bound.

## Why Rounding Can Fail

LP optimum: $(3.8,3)$, value $-8.2$.
Nearest rounding gives $(4,3)$:
$5(4)+10(3)=50>49$.
Infeasible.
Nearby feasible $(4,2)$ costs $-4$, but $(2,2)$ costs $-6$.
A nearby feasible point need not be optimal.

## Branch and Bound

Incumbent:
the best feasible integer solution found so far.
- Solve the LP relaxation at the current node.
- Close the node if it is infeasible, integral, or cannot improve the incumbent.
- Otherwise, branch on a fractional integer variable.
- Explore the children, keeping all ancestor constraints.
When no open nodes remain, the best integer solution found is optimal.

## The Branching Rule

Choose an integer-constrained variable with fractional value $x_i^*$.
$$x_i\le\lfloor x_i^*\rfloor\qquad\text{or}\qquad x_i\ge\lceil x_i^*\rceil.$$
Example: $x_i^*=3.8$.
$$x_i\le3\qquad\text{or}\qquad x_i\ge4.$$
Both children exclude the current fractional solution.
Every integer feasible solution belongs to one of the children.

## Bounds and the Incumbent

- Node lower bound $L$: the optimal value of its LP relaxation.
- Incumbent: the best feasible integer solution found so far.
- Global upper bound $U$: the incumbent's objective value.
Start with $U=+\infty$ if no feasible integer solution is known.
When a better integer solution of value $z$ is found, set $U\leftarrow z$ and store that solution.

## Three Ways to Close a Node

| Case Action and reason
| LP is infeasible No integer solution can satisfy this node's constraints.
| LP optimum is integral Update the incumbent if better. This node is solved.
| Bound: $L\ge U$ No integer solution in this node can improve the incumbent.
Example: $L=-5.4$ and $U=-6$. Prune because $-5.4\ge-6$.

## Example: The First Branch

Root: $(3.8,3)$, $L=-8.2$. Branch on $x$ and explore $x\ge4$ first.

## The First Incumbent

Within $x\ge4$, the LP optimum is $(4,2.9)$ with $L=-7.6$.
Branch on $y$: $y\le2$ or $y\ge3$.
| Additional constraint LP result Action
| $y\le2$ $(4,2)$, value $-4$ Integer: set $U=-4$.
| $y\ge3$ Infeasible Close this node.
The $x\ge4$ subtree is finished. Return to $x\le3$.

## Improving the Incumbent

Within $x\le3$: LP optimum $(3,2.6)$, $L=-7.4$. Entering this subtree: $U=-4$.
| Additional constraints LP result Action
| $y\ge3$ Infeasible Close.
| $y\le2$ $(1.8,2)$; $L=-6.2$ Branch on $x$.
| $y\le2,\ x\ge2$ $(2,2)$; value $-6$ Integer: update $U=-6$.
| $y\le2,\ x\le1$ $(1,1.6)$; $L=-5.4$ Prune: $-5.4\ge-6$.
Every row inherits $x\le3$ and the original constraints.

## The Complete Search Tree

Incumbent: $U=+\infty\ \longrightarrow\ -4\ \longrightarrow\ -6$. Every leaf is closed.

## Optimality Certificate

$$\mathbf{x}^*=(2,2),\qquad z^*_{\mathrm{IP}}=2-4(2)=-6.$$
Every leaf is infeasible, solved integrally, or unable to improve $-6$.
Therefore no unexplored branch can contain a better solution.
| Can we stop at the first integer solution? No. Here $-4$ improved to $-6$.
| Why does a lower bound of $-5.4$ allow pruning? Every integer descendant costs at least $-5.4>-6$.

Q & A
