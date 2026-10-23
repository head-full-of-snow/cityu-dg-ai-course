Optimization
CS5491: Artificial Intelligence
Zhichao Lu
Content Credits:
Prof. Wei
's CS4486 Course
and
Prof. Boddeti
's AI Course

## Announcements

- Midterm: Thursday, 22 October 2026
20% of the course grade; attend your enrolled session.
- Printed-materials-only open book; no electronic devices.
- Project proposal: 15 October, 11:59 pm BJT.
- Use the practice paper and solutions to prepare.

## Today: Modeling Optimization

LP and IP are examples of a more general framework.
- Identify the decision variables, feasible set, and objective.
- Distinguish a feasible point, an optimal solution, and the optimal value.
- Formulate examples and check what a solver returns.

## An Optimization Model

$$\min_{\mathbf{x}\in\mathcal{F}} f(\mathbf{x})$$
| Component Meaning
| Decision variables $\mathbf{x}$ Quantities we choose.
| Feasible set $\mathcal{F}$ Choices satisfying all domain restrictions and constraints.
| Objective $f:\mathcal{F}\to\mathbb{R}$
| The value we want to minimize.
LP example: $f(\mathbf{x})=\mathbf{c}^T\mathbf{x}$, $\mathcal{F}=\{\mathbf{x}:A\mathbf{x}\le\mathbf{b}\}$.
Given: $A,\mathbf{b},\mathbf{c}$. Choose: $\mathbf{x}$.

## Variable Domains and Constraints

| Variable type Example domain Example decision
| Continuous $a\in\mathbb{R}$ A regression slope.
| Discrete $z\in\{0,1\}$ Whether to select an item.
| Mixed $(a,z)\in\mathbb{R}\times\{0,1\}$ A quantity and an on/off choice.
- Additional constraints can further restrict these choices.
- Unconstrained optimization here means $\mathcal{F}=\mathbb{R}^n$.
- Example: requiring a nonnegative slope gives $\mathcal{F}=[0,\infty)$.

## Optimal Solutions and Values

When a minimum is attained:
$$\mathbf{x}^*\in\operatorname{argmin}_{\mathbf{x}\in\mathcal{F}} f(\mathbf{x}),
      \qquad f^*=\min_{\mathbf{x}\in\mathcal{F}} f(\mathbf{x})=f(\mathbf{x}^*).$$
- $\operatorname{argmin}$:
the set of all optimal choices.
- $f^*$:
the optimal objective value, a number.
Example: minimize $t^2$ over $\mathcal{F}=\{-1,1\}$.
$$\operatorname{argmin}_{t\in\mathcal{F}}t^2=\{-1,1\},\qquad f^*=1.$$

## Does an Optimal Solution Exist?

| Problem Outcome
| $\min t$, $t\in[0,1]$ Attained: $t^*=0$, value $0$.
| $\min t$, $t\in\mathbb{R}$ Unbounded below.
| $\min t$, $t\ge1$ and $t\le0$ Infeasible: no allowed choice.

## Minimization and Maximization

Define $g(\mathbf{x})=-f(\mathbf{x})$ on the same feasible set.
$$\operatorname{argmin}_{\mathbf{x}\in\mathcal{F}} f(\mathbf{x})
      =\operatorname{argmax}_{\mathbf{x}\in\mathcal{F}} g(\mathbf{x}).$$
The optimal choices are the same. When attained, the optimal values satisfy $g^*=-f^*$.
Example: $\mathcal{F}=\{2,5\}$, $f(t)=t$, and $g(t)=-t$.
$$t^*=2\text{ in both problems};\qquad f^*=2,\quad g^*=-2.$$

## Traveling Salesman Problem

Data:
distances $d(i,j)$.
Decision:
a visiting order $\mathbf{x}=(x_1,\ldots,x_n)$.
Feasible set:
all permutations of the $n$ cities.
$$f(\mathbf{x})=\sum_{k=1}^{n-1}d(x_k,x_{k+1})+\color{orange}{d(x_n,x_1)}.$$
The closing edge returns to the start; this tour has length $10$.

## 8 Queens as a Feasibility Problem

$x_i$: row of the queen in column $i$.
$$x_i\in\{1,\ldots,8\}.$$
For every $1\le i<j\le8$:
$$x_i\ne x_j,$$
          $$|x_i-x_j|\ne|i-j|.$$
One queen per column is built into the representation.
Minimize the constant objective $f(\mathbf{x})=0$ over these constraints. Every feasible placement is optimal.

## Fitting a Line Through the Origin

Given observations: $(1,2.1)$, $(2,3.98)$, $(3,7.0)$.
Decision:
slope $a\in\mathbb{R}$. Prediction: $\hat y_i=ax_i$.
Residual:
$e_i(a)=y_i-ax_i$. The pictured $a=2$ is a candidate.

## Choose an Error Objective

What objective would make the residuals $e_i(a)=y_i-ax_i$ small?
Absolute error
$$L_1(a)=\sum_{i=1}^3|y_i-ax_i|.$$
Squared error
$$L_2(a)=\sum_{i=1}^3(y_i-ax_i)^2.$$
At $a=2$, the residuals are $(0.10,-0.02,1.00)$:
$L_1(2)=1.12$ and $L_2(2)=1.0104$.
Compare candidates using the same loss; these two values have different scales.

## The Loss Changes the Best Fit

Absolute error has an interval of best slopes.
Squared error has one best slope.
Both are convex; convexity does not guarantee uniqueness.

## Recognizing Problem Structure

| Model Structure that matters
| Linear program Linear objective and linear constraints; continuous variables.
| Integer / mixed-integer program Some or all variables must take integer values.
| Convex minimization Convex objective over a convex feasible set.
- LP is a special case of convex optimization.
- Integer restrictions generally make a feasible set nonconvex.
- Both regression losses are nonlinear but convex.

## Solving and Checking a Model

- Formulate the variables, constraints, and objective.
- Choose a method suited to the model's structure.
- Solve and inspect the reported status.
- Check feasibility and recompute the objective.
- Interpret the result in the original problem.
A feasible point need not be optimal. A solver may also report infeasibility, unboundedness, or an unfinished search.

## Check the Model

Fit $\hat y_i=ax_i$ to the same observations, requiring $a\ge0$ and minimizing squared error.
| Question Answer
| What is chosen? The slope $a$.
| What data are given? The observations $(x_i,y_i)$.
| What is the feasible set? $\mathcal{F}=[0,\infty)$.
| What is the objective? $f(a)=\sum_{i=1}^3(y_i-ax_i)^2$.
| Is this a linear program? No: the objective is quadratic in $a$.

## Key Points

- Separate what is chosen from what is known.
- Feasibility, optimality, and the optimal value are different concepts.
- The representation and objective determine the optimization problem.
- Check a solver's result before interpreting it.
Next: how do convex sets and convex objectives help us solve these models?

Q & A
