Linear Programming
CS5491: Artificial Intelligence
Zhichao Lu
Content Credits:
Prof. Wei
's CS4486 Course
and
Prof. Boddeti
's AI Course

## Announcements

- Project proposal: 15 October 2026, 23:59 (BJT)
Submit through Canvas. The group project is worth 30% of the course grade.
- Midterm: 22 October 2026
Worth 20% of the course grade. Check Canvas for preparation materials.

## What to eat?

- We want to meet the given nutrition targets at minimum cost.
- We can choose the amount of stir-fry
(ounces) and
boba
(fluid ounces).
Nutrition targets
$2000 \leq \text{Calories} \leq 2500$
$\text{Sugar} \leq 100\,\text{g}$
$\text{Calcium} \geq 700\,\text{mg}$
|
Food
Cost
(units)
Calories
Sugar
(g)
Calcium
(mg)
|
stir-fry
(per oz)
| 1
100
3
20
|
Boba
(per fl oz)
| 0.4
50
4
70
- What is the cheapest way to meet these targets with this menu?
- How much stir-fry
(ounces) and
boba
(fluid ounces) should we buy?

## Can Search Algorithms Help?

- Essence of search algorithms:
  - explore candidate states until a goal is reached
  - use additional information to avoid unnecessary search
- Can we adopt a similar strategy here?

## Optimization

Problem Description
Optimization Representation
          $$\begin{aligned}
          \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
          s.t. && \mathbf{A}\mathbf{x} \leq \mathbf{b}
          \end{aligned}$$
Graphical Representation

## What to eat?: Constraints

- We want to meet the given nutrition targets at minimum cost.
- We can choose the amount of stir-fry
(ounces) and
boba
(fluid ounces).
Nutrition targets
$2000 \leq \text{Calories} \leq 2500$
$\text{Sugar} \leq 100\,\text{g}$
$\text{Calcium} \geq 700\,\text{mg}$
|
Food
Cost
(units)
Calories
Sugar
(g)
Calcium
(mg)
|
stir-fry
(per oz)
| 1
100
3
20
|
Boba
(per fl oz)
| 0.4
50
4
70
- What is the cheapest way to meet these targets with this menu?
- How much stir-fry
(ounces) and
boba
(fluid ounces) should we buy?

## Constraint Satisfaction Problems

Map Coloring
        $$
        \begin{aligned}
        Any &~\mathbf{x} \\
        s.t. &~\mathbf{x} {\rm{~satisfies~constraints}}
        \end{aligned}
        $$

## What to eat?: Costs

- We want to meet the given nutrition targets at minimum cost.
- We can choose the amount of stir-fry
(ounces) and
boba
(fluid ounces).
Nutrition targets
$2000 \leq \text{Calories} \leq 2500$
$\text{Sugar} \leq 100\,\text{g}$
$\text{Calcium} \geq 700\,\text{mg}$
|
Food
Cost
(units)
Calories
Sugar
(g)
Calcium
(mg)
|
stir-fry
(per oz)
| 1
100
3
20
|
Boba
(per fl oz)
| 0.4
50
4
70
- What is the cheapest way to meet these targets with this menu?
- How much stir-fry
(ounces) and
boba
(fluid ounces) should we buy?

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Nutrition targets
$2000 \leq \text{Calories} \leq 2500$
$\text{Sugar} \leq 100\,\text{g}$
$\text{Calcium} \geq 700\,\text{mg}$
|
Food
Cost
(units)
Calories
Sugar
(g)
Calcium
(mg)
|
stir-fry
(per oz)
| 1
100
3
20
|
Boba
(per fl oz)
| 0.4
50
4
70
Diet Problem
          $$
          \begin{aligned}
          \min_{\mathbf{x}}~&~cost(\mathbf{x}) \\
          s.t.~&~\mathbf{x} {\rm{~satisfies~constraints}}
          \end{aligned}
          $$

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Nutrition targets
$2000 \leq \text{Calories} \leq 2500$
$\text{Sugar} \leq 100\,\text{g}$
$\text{Calcium} \geq 700\,\text{mg}$
|
Food
Cost
(units)
Calories
Sugar
(g)
Calcium
(mg)
|
stir-fry
(per oz)
| 1
100
3
20
|
Boba
(per fl oz)
| 0.4
50
4
70
Diet Problem
          $$
          \begin{aligned}
          \min_{\mathbf{x}}~&~cost(\mathbf{x}) \\
          s.t.~&~calories(\mathbf{x}) \leq 2500 \\
         ~&~calories(\mathbf{x}) \geq 2000 \\
         ~&~sugar(\mathbf{x}) \leq 100 \\
         ~&~calcium(\mathbf{x}) \geq 700
          \end{aligned}
          $$

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Nutrition targets
$2000 \leq \text{Calories} \leq 2500$
$\text{Sugar} \leq 100\,\text{g}$
$\text{Calcium} \geq 700\,\text{mg}$
|
Food
Cost
(units)
Calories
Sugar
(g)
Calcium
(mg)
|
stir-fry
(per oz)
| 1
100
3
20
|
Boba
(per fl oz)
| 0.4
50
4
70
Diet Problem
          $$
          \begin{aligned}
          \min_{\mathbf{x}} && 1x_1 + 0.4x_2 \\
          s.t. && 100x_1 + 50x_2 \geq 2000 \\
          && 100x_1 + 50x_2 \leq 2500 \\
          && 3x_1 + 4x_2 \leq 100 \\
          && 20x_1 + 70x_2 \geq 700
          \end{aligned}
          $$

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Diet Problem
        $$
        \begin{aligned}
        \min_{\mathbf{x}} && c_1x_1 + c_2x_2 \\
        s.t. && a_{1,1}x_1 + a_{1,2}x_2 \geq b_1 \\
        && a_{2,1}x_1 + a_{2,2}x_2 \leq b_2 \\
        && a_{3,1}x_1 + a_{3,2}x_2 \leq b_3 \\
        && a_{4,1}x_1 + a_{4,2}x_2 \geq b_4
        \end{aligned}
        $$
$$A=\begin{bmatrix}100 & 50 \\ 100 & 50 \\ 3 & 4 \\ 20 & 70\end{bmatrix} ~~
        b=\begin{bmatrix}2000 \\ 2500 \\ 100 \\ 700\end{bmatrix} {\rm{~and~}}~c=\begin{bmatrix}1 \\ 0.4\end{bmatrix}$$

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Diet Problem
        $$
        \begin{aligned}
        \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x}\\
        s.t. && a_{1,1}x_1 + a_{1,2}x_2 \geq b_1 \\
        && a_{2,1}x_1 + a_{2,2}x_2 \leq b_2 \\
        && a_{3,1}x_1 + a_{3,2}x_2 \leq b_3 \\
        && a_{4,1}x_1 + a_{4,2}x_2 \geq b_4
        \end{aligned}
        $$
$$A=\begin{bmatrix}100 & 50 \\ 100 & 50 \\ 3 & 4 \\ 20 & 70\end{bmatrix} ~~
        b=\begin{bmatrix}2000 \\ 2500 \\ 100 \\ 700\end{bmatrix} {\rm{~and~}}~c=\begin{bmatrix}1 \\ 0.4\end{bmatrix}$$

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Diet Problem
        $$
        \begin{aligned}
        \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
        s.t. && -a_{1,1}x_1 - a_{1,2}x_2 \leq -b_1 \\
        && a_{2,1}x_1 + a_{2,2}x_2 \leq b_2 \\
        && a_{3,1}x_1 + a_{3,2}x_2 \leq b_3 \\
        && -a_{4,1}x_1 - a_{4,2}x_2 \leq -b_4
        \end{aligned}
        $$
$$A=\begin{bmatrix}100 & 50 \\ 100 & 50 \\ 3 & 4 \\ 20 & 70\end{bmatrix} ~~
        b=\begin{bmatrix}2000 \\ 2500 \\ 100 \\ 700\end{bmatrix} {\rm{~and~}}~c=\begin{bmatrix}1 \\ 0.4\end{bmatrix}$$

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Diet Problem
        $$
        \begin{aligned}
        \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
        s.t. && a_{1,1}x_1 + a_{1,2}x_2 \leq b_1 \\
        && a_{2,1}x_1 + a_{2,2}x_2 \leq b_2 \\
        && a_{3,1}x_1 + a_{3,2}x_2 \leq b_3 \\
        && a_{4,1}x_1 + a_{4,2}x_2 \leq b_4
        \end{aligned}
        $$
$$A=\begin{bmatrix}-100 & -50 \\ 100 & 50 \\ 3 & 4 \\ -20 & -70\end{bmatrix} ~~
        b=\begin{bmatrix}-2000 \\ 2500 \\ 100 \\ -700\end{bmatrix} {\rm{~and~}}~c=\begin{bmatrix}1 \\ 0.4\end{bmatrix}$$

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Diet Problem
        $$
        \begin{aligned}
        \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
        s.t. && \mathbf{A}\mathbf{x} \leq \mathbf{b},\quad \mathbf{x}\geq\mathbf{0}
        \end{aligned}
        $$
$$A=\begin{bmatrix}-100 & -50 \\ 100 & 50 \\ 3 & 4 \\ -20 & -70\end{bmatrix} ~~
        b=\begin{bmatrix}-2000 \\ 2500 \\ 100 \\ -700\end{bmatrix} {\rm{~and~}}~c=\begin{bmatrix}1 \\ 0.4\end{bmatrix}$$

## Linear Programming

- Linear objective with linear constraints
$$
        \begin{aligned}
        \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
        s.t. && \mathbf{A}\mathbf{x} \leq \mathbf{b}
        \end{aligned}
        $$
- As opposed to general optimization
$$
        \begin{aligned}
        \min_{\mathbf{x}} && f(\mathbf{x}) \\
        s.t. && g_i(\mathbf{x}) \leq 0, i=1,\dots,M \\
        && h_i(\mathbf{x}) = 0, i=1,\dots,P
        \end{aligned}
        $$

## Linear Programming

- Different formulations
Inequality Form
$$
          \begin{aligned}
          \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
          s.t. && \mathbf{A}\mathbf{x} \leq \mathbf{b} \\
          && ~~
          \end{aligned}
          $$
General Form
$$
          \begin{aligned}
          \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} + d \\
          s.t. && \mathbf{G}\mathbf{x} \leq \mathbf{h} \\
          && \mathbf{A}\mathbf{x} = \mathbf{b} \\
          \end{aligned}
          $$
Standard Form (here)
$$
          \begin{aligned}
          \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
          s.t. && \mathbf{A}\mathbf{x} = \mathbf{b} \\
          && \mathbf{x} \geq \mathbf{0}
          \end{aligned}
          $$

## Optimization

Problem Description
Optimization Representation
          $$\begin{aligned}
          \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
          s.t. && \mathbf{A}\mathbf{x} \leq \mathbf{b}
          \end{aligned}$$
Graphical Representation

## Graphical Representation

- What shape does this inequality represent?
$$
      a_1x_1 + a_2x_2 \leq b_1
      $$

## Cost Contours

Illustration: $\mathbf{c}=[1,1]^T$.
Each line has constant cost:
$$\mathbf{c}^T\mathbf{x}=x_1+x_2=k.$$
$k\in\{-2,-1,0,1,2\}$.
The contours are parallel. The vector $\mathbf{c}$ is perpendicular to them and points toward
increasing cost
.

## LP Graphical Representation

- Inequality Form
$$
      \begin{aligned}
      \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
      s.t. && \mathbf{A}\mathbf{x} \leq \mathbf{b}
      \end{aligned}
      $$
- Start with no constraints
- Add one constraint at a time

## Optimization

Problem Description
Optimization Representation
          $$\begin{aligned}
          \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
          s.t. && \mathbf{A}\mathbf{x} \leq \mathbf{b}
          \end{aligned}$$
Graphical Representation

## Optimization Formulation

$x_1$: stir-fry (oz); $x_2$: boba (fl oz). $\mathbf{x}\in\mathbb{R}_{\geq0}^2$.
Diet Problem
        $$
        \begin{aligned}
        \min_{\mathbf{x}} && \mathbf{c}^T\mathbf{x} \\
        s.t. && \mathbf{A}\mathbf{x} \leq \mathbf{b},\quad \mathbf{x}\geq\mathbf{0}
        \end{aligned}
        $$
$$A=\begin{bmatrix}-100 & -50 \\ 100 & 50 \\ 3 & 4 \\ -20 & -70\end{bmatrix} ~~
        b=\begin{bmatrix}-2000 \\ 2500 \\ 100 \\ -700\end{bmatrix} {\rm{~and~}}~c=\begin{bmatrix}1 \\ 0.4\end{bmatrix}$$

## Solving an LP

For a nonempty, bounded feasible polyhedron,
at least one optimal solution is a vertex
.
For this diet model, the optimal vertex is unique.
In two dimensions, a vertex is a feasible intersection of independent constraint boundaries.

## Diet Problem: Optimal Solution

The calorie lower bound and sugar upper bound are binding:
$$\begin{aligned}
          100x_1+50x_2&=2000,\\
          3x_1+4x_2&=100.
          \end{aligned}$$
Unique optimum: $(x_1,x_2)=(12,16)$
12 oz stir-fry and 16 fl oz boba.
Minimum cost: 18.4 units
$12+0.4(16)=18.4$.
The other vertices cost $19.5$, $24$, and $24\frac{2}{3}$.

## Possible LP Outcomes

| Outcome Example Meaning
| Finite optimum $\min x$
subject to $x\geq0$ Optimal value $0$ at $x=0$
| Infeasible $\min x$
subject to $x\geq1$, $x\leq0$ No point satisfies all constraints
| Unbounded objective $\min -x$
subject to $x\geq0$ The objective can decrease without limit
An unbounded feasible region can still have a finite optimum, as in the first example.

## Algorithms and Integer Decisions

- Simplex: moves between adjacent feasible vertices, seeking a better objective value.
- Interior-point methods: approach an optimum through the interior.
- Requiring integer decisions gives an integer program. Rounding an LP solution may be infeasible or suboptimal.
- Branch and bound: uses LP relaxations to bound and prune a search tree.
Open graphical LP and integer-programming demonstrations →

Q & A
