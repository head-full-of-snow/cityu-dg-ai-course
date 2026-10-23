Convex Optimization
CS5491: Artificial Intelligence
Zhichao Lu
Content Credits:
Prof. Wei
's CS4486 Course
and
Prof. Boddeti
's AI Course

## Today

- Recognize convex sets, functions, and optimization problems.
- Distinguish existence, global optimality, and uniqueness.
- Calculate gradient-descent updates and explain the role of step size.

## LP, IP, and Convex Optimization

- LP:
a linear objective over a convex feasible region.
- Adding integer restrictions generally makes the feasible set nonconvex.
- A convex objective need not be linear. Its minimum can lie inside the feasible region.
Example: minimize $t^2$ on $[-1,1]$. The optimum is $t=0$, not a vertex.

## Convex Optimization: Definition

$$\min_{\mathbf{x}\in\mathcal{F}} f(\mathbf{x})$$
- The feasible set $\mathcal{F}$ is convex.
- The objective $f$ is convex on $\mathcal{F}$.
Both conditions matter. We will examine each one.

## Convex Combination

A point on the line segment joining $\mathbf{x}$ and $\mathbf{y}$:
$$\mathbf{z}=\theta\mathbf{x}+(1-\theta)\mathbf{y},\qquad 0\le\theta\le1.$$
- $\theta=0$ or $1$ gives an endpoint; $\theta=1/2$ gives the midpoint.
- For $\mathbf{x}=(0,0)$ and $\mathbf{y}=(2,4)$, their midpoint is $(1,2)$.
- When $0<\theta<1$, this is a strict convex combination.

## Convex Sets

Every line segment joining two points in the set stays inside the set.
$$\mathbf{x},\mathbf{y}\in\mathcal{F},\ 0\le\theta\le1
        \ \Longrightarrow\ \theta\mathbf{x}+(1-\theta)\mathbf{y}\in\mathcal{F}.$$
Nonconvex set
Convex set

## Quiz: Convex Sets

For $n\ge1$ and convex $\mathcal{F}_1,\mathcal{F}_2$, which sets must be convex?
| Set Answer and reason
| $\mathbb{R}^n$ Convex: every segment stays in $\mathbb{R}^n$.
| $\emptyset$ Convex: no pair violates the definition.
| $\{\mathbf{x}_0\}$ Convex: every combination equals $\mathbf{x}_0$.
| $\mathcal{F}_1\cap\mathcal{F}_2$ Convex if both sets are convex.
| $\mathcal{F}_1\cup\mathcal{F}_2$ Not necessarily: $\{0\}\cup\{2\}$ omits $1$.
| $\mathbb{Z}^n$ Not convex: a midpoint need not be integral.

## Convex Functions

The value at a convex combination is
no greater than
the corresponding weighted average of values.
For a convex domain $\mathcal{F}$, all $\mathbf{x},\mathbf{y}\in\mathcal{F}$ and $\theta\in[0,1]$:
$$\color{cyan}{f(\theta\mathbf{x}+(1-\theta)\mathbf{y})}
      \le \color{orange}{\theta f(\mathbf{x})+(1-\theta)f(\mathbf{y})}.$$
Equality is allowed. In particular, every affine function is convex.
Strict convexity requires $<$ whenever $\mathbf{x}\ne\mathbf{y}$ and $0<\theta<1$.

## The Graph Lies Below Its Chord

$q(t)=(t-2)^2+1$. Drag the endpoints and vary $\theta$.
A quadratic curve and the chord joining two movable points
Use the endpoint and weight sliders below to explore the convexity inequality.
Endpoint $a$:
0.00
Endpoint $b$:
4.00
Weight $\theta$:
0.50
Reset
$z=\theta a+(1-\theta)b=$
2.00
$q(z)=$
1.00
$\le$
$\theta q(a)+(1-\theta)q(b)=$
5.00
For every $a,b\in\mathbb{R}$ and $\theta\in[0,1]$:
        $\underbrace{\theta q(a)+(1-\theta)q(b)-q(z)}_{\text{gap}}=\theta(1-\theta)(a-b)^2\ge0.$
Current gap:
4.00
·
Strict inequality

## Checking Convexity

- Apply the defining inequality.
- Use a nonnegative weighted sum of convex functions:
$$f(\mathbf{x})=\sum_i w_i f_i(\mathbf{x}),\qquad w_i\ge0.$$
- Compose a convex function with an affine
map:
          $$f(\mathbf{x})=g(A\mathbf{x}+\mathbf{b}).$$

## The Second-Derivative Test

For a twice continuously differentiable function on an open interval $I$:
$$f\text{ is convex on }I\quad\Longleftrightarrow\quad f''(t)\ge0\text{ for all }t\in I.$$
Example: $q(t)=(t-2)^2+1$, for all real $t$.
$$q'(t)=2(t-2),\qquad q''(t)=2>0.$$
Therefore $q$ is convex (in fact, strictly convex).

## The Gradient

For a differentiable $f:\mathbb{R}^n\to\mathbb{R}$:
$$\nabla f(\mathbf{x})=
      \begin{bmatrix}\partial f/\partial x_1\\\vdots\\\partial f/\partial x_n\end{bmatrix}
      \in\mathbb{R}^n.$$
- A vector of partial derivatives, evaluated at $\mathbf{x}$.
- When nonzero, it points in the direction of steepest local increase under the Euclidean norm.
- When the gradient is nonzero, its negative is a local descent direction.

## The Hessian Test

Let $U\subseteq\mathbb{R}^n$ be
open and convex
, and let $f\in C^2(U)$.
$$H(\mathbf{x})=\nabla^2 f(\mathbf{x}),\qquad
      H_{ij}(\mathbf{x})=\frac{\partial^2 f}{\partial x_i\,\partial x_j}.$$
$$f\text{ is convex on }U
      \quad\Longleftrightarrow\quad H(\mathbf{x})\succeq0\text{ for every }\mathbf{x}\in U.$$
Positive semidefinite means $\mathbf{z}^T H(\mathbf{x})\mathbf{z}\ge0$ for every $\mathbf{z}$.
At each $\mathbf{x}$, this is equivalent to all eigenvalues of the symmetric matrix $H(\mathbf{x})$ being nonnegative.

## A Positive-Semidefinite Hessian

$$F(u,v)=(u+v-1)^2.$$
$$\nabla F=2(u+v-1)\begin{bmatrix}1\\1\end{bmatrix},\qquad
      H=\begin{bmatrix}2&2\\2&2\end{bmatrix}.$$
$$\mathbf{z}^T H\mathbf{z}=2(z_1+z_2)^2\ge0.$$
Thus $F$ is convex on $\mathbb{R}^2$. The Hessian has eigenvalues $0$ and $4$.

## Concavity and Convexity

$f$ is concave exactly when $-f$ is convex.
$$f(\theta\mathbf{x}+(1-\theta)\mathbf{y})
        \ge\theta f(\mathbf{x})+(1-\theta)f(\mathbf{y}).$$
Maximizing a concave function over a convex set is equivalent to a convex minimization problem:
$$\max_{\mathbf{x}\in\mathcal{F}}f(\mathbf{x})
        \quad\Longleftrightarrow\quad\min_{\mathbf{x}\in\mathcal{F}}[-f(\mathbf{x})].$$

## Quiz: Convex Functions

| Function and domain Answer and reason
| $e^{at}$, $t\in\mathbb{R}$, $a\in\mathbb{R}$ Convex: $f''=a^2e^{at}\ge0$.
| $\log t$, $t>0$ Concave, not convex: $f''=-1/t^2$.
| $\|\mathbf{x}\|_2$, $\mathbf{x}\in\mathbb{R}^n$ Convex; not differentiable at $\mathbf{0}$.
| $\mathbf{x}^T A\mathbf{y}$, jointly in $(\mathbf{x},\mathbf{y})$ Convex iff $A=0$; otherwise neither convex nor concave.
| $t^3$, $t\in\mathbb{R}$ Neither: $f''(t)=6t$ changes sign.

## Local and Global Minima

- A global minimum
occurs at a feasible point whose objective value is no greater than at any feasible point.
- A local minimum
occurs at a feasible point whose objective value is no greater than at nearby feasible points.
For a convex optimization problem, every local minimum is global.
If a better feasible point existed, moving a little toward it would already improve the objective.

## Existence and Uniqueness

Convexity alone guarantees neither a minimum nor a unique point attaining it.
| Convex problem What happens?
| $\min_{t\in\mathbb{R}}[(t-2)^2+1]$ Minimum attained only at $t=2$.
| $\min_{t\in\mathbb{R}}e^t$ Infimum $0$, but no attained minimum.
| $\min_{0\le u,v\le1}(u+v-1)^2$ Minimum attained at infinitely many points.
With strict convexity,
at most one point
attains the minimum; existence is a separate question.

## Finding All Minima

$$\min_{0\le u,v\le1} F(u,v),\qquad F(u,v)=(u+v-1)^2.$$
- A square is nonnegative: $F(u,v)\ge0$.
- Equality holds exactly when $u+v=1$.
$$F^*=0,\qquad
        \operatorname{argmin}F=\{(u,1-u):0\le u\le1\}.$$
Minima occur at $(0,1)$, $(1,0)$, and every point on the segment between them.

## Gradient Descent

For an unconstrained, differentiable objective:
$$\mathbf{x}_{k+1}=\mathbf{x}_k-\alpha_k\nabla f(\mathbf{x}_k),\qquad\alpha_k>0.$$
- Choose an initial point $\mathbf{x}_0$.
- Evaluate the gradient at the current point.
- Take a step in the negative-gradient direction.
- Repeat until a stopping criterion is satisfied.

## A Gradient-Descent Update

$$q(t)=(t-2)^2+1,\qquad t_0=0,\qquad\alpha=\tfrac14.$$
$$q'(t)=2(t-2),\qquad q'(0)=-4.$$
$$t_1=0-\tfrac14(-4)=1,\qquad q(t_1)=2<q(t_0)=5.$$
$$t_2=1-\tfrac14(-2)=\tfrac32,\qquad q(t_2)=\tfrac54.$$
The global minimum occurs at $t^*=2$, with value $q(t^*)=1$.

## Iterates and Objective Values

Gradient-descent iterates and their objective values
Use Next step to update the parameter and see its objective value in both plots.
Start $t_0$:
0
Step size $\alpha$:
0.25
Back
Next step
Restart
$k=$
0
$t_k=$
0
$q(t_k)=$
5
$q'(t_k)=$
−4
Next: $t_{k+1}=t_k-2\alpha(t_k-2)=$
1
Approaches the minimum from one side.

## Step Size Matters

For $q(t)=(t-2)^2+1$, the minimum occurs at $t^*=2$.
$\begin{aligned}
        t_{k+1}&=t_k-2\alpha(t_k-2) &&\text{gradient step}\\
        t_{k+1}-2&=(t_k-2)-2\alpha(t_k-2) &&\text{subtract }2\\
        \color{cyan}{t_{k+1}-2}&=\color{orange}{(1-2\alpha)}\color{cyan}{(t_k-2)} &&\text{factor}
      \end{aligned}$
Each step multiplies the
signed error $t_k-2$
by
$1-2\alpha$
.
| $\alpha$ Factor $1-2\alpha$ Starting at $t_0=0$ Behavior
| $1/4$ $1/2$ $0,1,3/2,\ldots$ Converges to $2$.
| $1$ $-1$ $0,4,0,4,\ldots$ Oscillates.
| $5/4$ $-3/2$ $0,5,-5/2,\ldots$ Diverges.
Distance from $2$ shrinks when $|1-2\alpha|<1$, that is, $0<\alpha<1$.

## Stopping and Optimality

- For unconstrained differentiable convex $f$, $\nabla f(\mathbf{x})=0$ certifies a global minimum.
- In computation, monitor the gradient norm, objective changes, and an iteration limit.
- A small update alone may reflect a tiny step size.
For $f(t)=t^2$, $t_0=100$, and $\alpha=10^{-12}$:
$$|t_1-t_0|=2\times10^{-10},\qquad f(t_1)\approx10000.$$

## Practice: One Step and the Optimum

$$r(t)=(t+1)^2+3,\qquad t_0=1,\qquad\alpha=\tfrac14.$$
| Calculate Answer
| $r'(t)$ and $r''(t)$ $2(t+1)$ and $2$; hence convex.
| $r'(t_0)$ $r'(1)=4$.
| The next iterate $t_1$ $1-\tfrac14(4)=0$.
| Global minimum: location and value $t^*=-1$, $r(t^*)=3$.

## Projected Gradient Descent

Optional background; not assessed in the midterm.
For a nonempty, closed, convex feasible set $\mathcal{F}$:
$$P_{\mathcal{F}}(\mathbf{z})=\operatorname{argmin}_{\mathbf{u}\in\mathcal{F}}
        \|\mathbf{z}-\mathbf{u}\|_2^2.$$
$$\mathbf{x}_{k+1}=P_{\mathcal{F}}\bigl(\mathbf{x}_k-\alpha_k\nabla f(\mathbf{x}_k)\bigr).$$
Start with $\mathbf{x}_0\in\mathcal{F}$. Take a gradient step, then project back to the feasible set.

## Solution Methods and Scope

- Core:
recognize convexity and interpret global minima.
- Core:
solve
$\nabla f=0$
and calculate gradient-descent updates for simple unconstrained examples.
- Optional background:
projected gradient descent.
- Newton, interior-point, and subgradient methods are outside this lecture's assessed techniques.

## Applying Convex Optimization

- Define the variables, objective, and feasible set.
- Establish convexity of both objective and feasible set.
- Solve the model and check feasibility and solver status.
- Interpret the solution in the original problem.
Tools include CVXPY, CVX, and CVXOPT. Modeling systems such as CVXPY recognize specific convex forms; a mathematically convex expression may need rewriting.

## Key Points

- Convex sets contain their line segments; convex functions lie below their chords.
- Local minima are global, but existence and uniqueness are separate issues.
- Gradient descent updates parameters using the negative gradient; step size affects convergence.
Be able to check convexity, calculate an update, and describe all minima of a simple example.

Q & A
