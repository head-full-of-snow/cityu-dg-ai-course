Convex Optimization

CS5491: Artificial Intelligence

ZHICHAO LU

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

# TODAY

Recognize convex sets, functions, and optimization problems.

Distinguish existence, global optimality, and uniqueness.

Calculate gradient-descent updates and explain the role of step size.

# LP, IP, AND CONVEX OPTIMIZATION

LP: a linear objective over a convex feasible region.

Adding integer restrictions generally makes the feasible set nonconvex.

A convex objective need not be linear. Its minimum can lie inside the feasible region.

Example: minimize $t^2$ on $[-1,1]$$. The optimum is $t=0$, not a vertex.

# CONVEX OPTIMIZATION: DEFINITION

# $$\min_{\{ \mathrm{mathbf{x}} \in \mathrm{F} \}} f(\mathrm{mathbf{x}})$$

The feasible set \mathcal{F}$ is convex.

The objective $f$ is convex on $\mathcal{F}$

Both conditions matter. We will examine each one.

# CONVEX COMBINATION

A point on the line segment joining $\mathrm{x}$ and $\mathrm{y}$:

# $$\mathrm{mathbf{z}}=\mathrm{\theta}+\mathrm{(1-\mathrm{\theta})}\mathrm{\theta}+\mathrm{(1-\mathrm{\theta})}\mathrm{\theta}+\mathrm{(1-\mathrm{\theta})}\mathrm{\theta}+\mathrm{(1-\mathrm{\theta})}\mathrm{\theta}+\mathrm

$\theta=0$ or $1$ gives an endpoint; $\theta=1/2$ gives the midpoint.

For $\mathrm{x}=(0,0)$ and $\mathrm{y}=(2,4)$, their midpoint is $(1,2)$.

When $0<\theta<1$, this is a strict convex combination.

# CONVEX SETS

Every line segment joining two points in the set stays inside the set.

$$\mathrm{mathbf{x}}, \mathrm{mathbf{y}} \in \mathrm{mathcal{F}}, \mathrm{0} \in \mathrm{theta} \in \mathrm{1} \in \mathrm{Longrightarrow} \in \mathrm{theta} \in \mathrm{mathbf{x}} + (1 - \mathrm{theta}) \in \mathrm{mathbf{y}} \in \mathrm{mathcal{F}}.$$

Nonconvex set

Convex set

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2Fbd1e6bec4a2c47649f8793994e4d90a5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089830&Signature=lz3ZtCOErqE3a5SpcqGSC7N0OVM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2F211338a41a004f5384680899c98fc07f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089830&Signature=GtQQkX2F5y0fWoBMFX4rMHukDCk%3D)

# QUIZ: CONVEX SETS

For $n\ge1$ and convex $\mathcal{F}$_1,\mathcal{F}$_2$, which sets must be convex?

<table><tr><td>Set</td><td>Answer and reason</td></tr><tr><td>$\mathrm{R}^n$</td><td>Convex: every segment stays in $\mathrm{R}^n$.</td></tr><tr><td>$\mathrm{R}^n$</td><td>Convex: no pair violates the definition.</td></tr><tr><td>$\mathrm{R}^n$</td><td>Convex: every combination equals $\mathrm{R}^n$.</td></tr><tr><td>$\mathrm{R}^n$</td><td>Convex if both sets are convex.</td></tr><tr><td>$\mathrm{R}^n$</td><td>Not necessarily: $\mathrm{R}^n$.</td></tr><tr><td>$\mathrm{R}^n$</td><td>$\mathrm{R}^n$.</td></tr><tr><td>$\mathrm{R}^n$</td><td>$\mathrm{R}^n$.</td></tr><tr><td>$\mathrm{R}^n$</td><td>$\mathrm{R}^n$.</td></tr><tr><td>$\mathrm{R}^n$</td><td>$\mathrm{R}^n$.</td></tr><tr><td>$\mathrm{R}^n</td><td></td></tr></table>

Set

Answer and reason

$\mathrm{Z}^{n}$

# Not convex: a midpoint need not be integral

# CONVEX FUNCTIONS

The value at a convex combination is no greater than the corresponding weighted average of values. For a convex domain $\mathcal{F}$, all $\mathcal{S}\backslash\mathbf{x},\backslash\mathbf{y}\backslash\mathbf{i}\backslash\mathbf{n}\backslash\mathbf{m}\backslash\mathbf{h}\backslash\mathbf{f}\backslash\mathbf{x},\backslash\mathbf{y}\backslash\mathbf{i}\backslash\mathbf{n}\backslash\mathbf{m}\backslash\mathbf{h}\backslash\mathbf{f}\backslash\mathbf{S}$ and $\mathcal{S}\backslash\mathbf{S}\backslash\mathbf{S}\backslash\mathbf{S}$

$$\backslash color\{cyan\}\{f(\theta\theta\theta\

Equality is allowed. In particular, every affine function is convex.

Strict convexity requires $\<$ whenever

$\mathrm{b f\{x\}}\\ne\\mathrm{b f\{y\}}$ and $0<\theta<1$.

# THE GRAPH LIES BELOW ITS CHORD

$q(t)=(t-2)^2+1$. Drag the endpoints and vary $\theta$.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2Fcf6c3b1d07124ca2b03642c680b14171.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089830&Signature=0Kpe%2FOsdxcXLIymweM0K5X6tAsk%3D)

Endpoint $a$: 0

Endpoint $b$: 4

Weight $\backslash$theta$: 0.5

Reset

$z=\theta a+(1-\theta a)b=$ 2

$q(z)=$ 1 $\le$ $ \theta a q(a)+(1-\theta a)q(b)=$ 5

For every $a,b\in\mathrm{mathbb{R}}$ and $\backslash\mathrm{theta}\backslash\in[0,1]$:

$\backslash\mathrm{underbrace{\theta(a)+(1-\theta(b)-q(z))_{t}}}$

$\mathrm{q(z)_{t}}\backslash\mathrm{text{gap}}=\backslash\mathrm{theta}(1-\backslash\mathrm{theta}(a-b)^{2}\backslash\mathrm{ge0.}$

Current gap: 4 • Strict inequality

# CHECKING CONVEXITY

Apply the defining inequality.

Use a nonnegative weighted sum of convex functions:

$$f(\mathrm{mathbf{x}})=\mathrm{sum\_i\,w\_i\,f\_i}(\mathrm{mathbf{x}}),\mathrm{quad\,w\_i}\mathrm{ge0}.\mathrm{$$

Compose a convex function with an affine map:

$$f(\mathrm{mathbf{x}})=g(\mathrm{A}\mathrm{mathbf{x}}+\mathrm{mathbf{b}}).\$$

# THE SECOND-DERIVATIVE TEST

For a twice continuously differentiable function on an open interval $I$:

$$f\backslash text{ is convex on }I\backslash quad\backslash Longleftrightarrow\quad quad f' (t)\backslash ge0\backslash text{ for all }t\backslash in I.\$$

Example: $q(t)=(t-2)^2+1$, for all real $t$.

$$q(t)=2(t-2),\backslash quad\ q'(t)=2>0.\$$

Therefore $q$ is convex (in fact, strictly convex).

# THE GRADIENT

## For a differentiable $f:\mathrm{mathbb}\{R\}^n\to\mathrm{mathbb}\{R\}\$: $\$\mathrm{nabla f(\mathrm{mathbf{x}})=\mathrm{begin}\mathrm{bmatrix}\mathrm{partial f}\mathrm{partial x\_1}\mathrm{vdots}\mathrm{partial f}\mathrm{partial x\_n}\mathrm{end}\mathrm{bmatrix}\}$ \in\mathrm{mathbb}\{R\}^n.\$

A vector of partial derivatives, evaluated at  $ \backslash $mathbf{x}\.

When nonzero, it points in the direction of steepest local increase under the Euclidean norm.

When the gradient is nonzero, its negative is a local descent direction.

# THE HESSIAN TEST

Let $U\subsetneq\operatorname{seteq}\backslash\operatorname{mathbb}\{R\}^{n}$ be open and convex, and let $f\setminus\operatorname{in}C^{2}(U)$.

$$H(\mathrm{mathbf{x}})=\mathrm{nabla^2 f(\mathrm{mathbf{x}}),\mathrm{quad H_{ij}}\\(\mathrm{mathbf{x}})=\mathrm{frac}\{\mathrm{partial^2 f}\}\{\mathrm{partial x\_i},\\\$f\text{ is convex on }U\ \mathrm{quad\Longleftarrows\Longleftarrows\Longleftarrows\quad

# A POSITIVE-SEMIDEFINITE HESSIAN

Thus $F$ is convex on $\backslash\mathrm{mathbb}\{R\}^{2}$$. The Hessian has eigenvalues $0$ and $4$.

# CONCAVITY AND CONVEXITY

$f$ is concave exactly when $-f$ is convex.

$$f(\theta\operatorname{math}bf\{x\}+(1-\theta\operatorname{math}bf\{y\})\ \theta\operatorname{math}bf\{x\})+(1-\theta\operatorname{math}bf\{y\}).$$

Maximizing a concave function over a convex set is equivalent to a convex minimization problem:

$$\max_{\{ \mathrm{mathbf{x}} \in \mathrm{F} \}} f(\mathrm{mathbf{x}})

\quad\Longleftrightarrow\quad\min_{\{\mathrm{mathbf{x}}\}\in\mathrm{mathcal}_{-f(\mathrm{mathbf{x}})}}.\$\

QUIZ: CONVEX FUNCTIONS

<table><tr><td>Function and domain</td><td>Answer and reason</td></tr><tr><td>$e^{at}$, $t\in\mathbb{R}$</td><td>Convex:</td></tr><tr><td>$a\in\mathbb{R}$</td><td>$f&#x27;=a^{2e}\{at\}\geq0$.</td></tr><tr><td>$\log t$, $t&gt;0$</td><td>Concave, not convex:</td></tr><tr><td></td><td>$f&#x27;=-1/t^{2}$</td></tr><tr><td>$\backslash\mathrm{mathbf{x}}\backslash\backslash_2$</td><td>Convex; not</td></tr><tr><td>$\backslash\mathrm{mathbf{x}}\backslash\in\mathbb{R}^n$</td><td>differentiable at</td></tr><tr><td></td><td>$\backslash\mathrm{mathbf{0}}$</td></tr><tr><td>$\backslash\mathrm{mathbf{x}}\backslash\wedge\mathrm{mathbf{y}}$</td><td>Convex iff $A=0$;</td></tr><tr><td>jointly in</td><td>otherwise neither</td></tr><tr><td>$\backslash\mathrm{mathbf{x}}\backslash\mathrm{mathbf{y}}$</td><td>Convex nor concave.</td></tr><tr><td>$t^{3}$, $t\in\mathbb{R}$</td><td>Neither: $f&#x27;=(t)=6t$</td></tr><tr><td></td><td>changes sign.</td></tr></table>

# LOCAL AND GLOBAL MINIMA

A global minimum occurs at a feasible point whose objective value is no greater than at any feasible point.

A local minimum occurs at a feasible point whose objective value is no greater than at nearby feasible points.

For a convex optimization problem, every local minimum is global.

If a better feasible point existed, moving a little toward it would already improve the objective.

# EXISTENCE AND UNIQUENESS

Convexity alone guarantees neither a minimum nor a unique point attaining it.

<table><tr><td>Convex problem</td><td>What happens?</td></tr><tr><td>$\min_{t\in\mathbb{R}}$</td><td>Minimum attained only at $t=2$.</td></tr><tr><td>$2^{2+1}$</td><td>$2^{2+1}$</td></tr><tr><td>$\min_{t\in\mathbb{R}}$</td><td>$2^{2+1}$</td></tr><tr><td>$2^{2}$</td><td>$2^{2}$</td></tr><tr><td>$2^{2}$</td><td>$2^{2}$</td></tr><tr><td>$2^{2}$</td><td>$2^{2}$</td></tr><tr><td>$2^{2}$</td><td>$2^{2}$</td></tr><tr><td>$2^{2}$</td><td>$2</td></tr></table>

With strict convexity, at most one point attains the minimum; existence is a separate question.

# FINDING ALL MINIMA

$$\min_{\{0\}}u,v\backslashle1\} F(u,v),\backslashqquad F(u,v)=(u+v-1)^2.\$$

A square is nonnegative: $F(u,v)\ge0$.

Equality holds exactly when $u+v=1$.

## $$F^\ast=0,\backslash\text{quad}\backslash\text{operatorname}\{\arg\min\}F=\{(u,1-u):0\backslash\text{le}u\backslash\text{le}1\}.\$$

Minima occur at $(0,1)$, $(1,0)$, and every point on the segment between them.

# GRADIENT DESCENT

For an unconstrained, differentiable objective:

$\mathrm{x}_{k+1}=\mathrm{mathbf{x}}_{k-k-alpha_{k-k-nabl}f(\mathrm{mathbf{x}}_{k},\mathrm{quad\alpha_{k}>0}.\$}$

L. Choose an initial point $\mathrm{x}$_0$.

2. Evaluate the gradient at the current point.

3. Take a step in the negative-gradient direction.

4. Repeat until a stopping criterion is satisfied.

# A GRADIENT-DESCENT UPDATE

#### $$q(t)=(t-2)^2+1,\quad\text{quad }t\_{0}=0,\quad\text{quad }\\$$ $$q'(t)=2(t-2),\quad\text{quad }q'(0)=-4.\$$ $$t\_{1}=0-\text{tfrac}14(-4)=1,\quad\text{quad }q(t\_{1})=2<q(t\_{0})=5.\$$ $$t\_{2}=1-\text{tfrac}14(-2)=\text{tfrac}32,\quad\text{quad }q(t\_{2})=\text{tfrac}54.\$$ The global minimum occurs at $t^*=2$, with value $q(t^*=1$

# I TERATES AND OBJECTIVE VALUES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2Fc1bb125e901948cb90e666e1f0721a00.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089830&Signature=5yKvpm2v%2FwJiuTwx7vUwBVGncxg%3D)

Take a step to see the parameter update.

Objective values

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2Fbe5e0fa62a55406fb1812acaa085f5e3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089831&Signature=q2JUU4Sba1r1UtPXM6MDvbncc08%3D)

Start $t_0$: 0 Step size $\backslash$alpha$: 0.25

Back

Next step

Restart

$t_k = $0

$q(t_k) = $5

$q'(t_k) = $ -4

Next: $t_{k+1}=t_{k-2}\alpha(t_{k-2})=1$

Approaches the minimum from one side.

Orange: current iterate. Values rounded.

# STEP SIZE MATTERS

For $q(t)=(t-2)^2+1$, the minimum occurs at $t^\star=2$.

$\begin{aligned} t_{k+1}&=t_{k-2}\\\text{gradient step}&\\\text{subtract }2&\\\text{color}&\\\text{orange}&\\\text{end}&\\\text{aligned}&\$\begin{aligned} t_{k-2}\\\text{alpha}(t_{k-2})\\t_{k-2}\\\text{alpha}(t_{k-2})\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan)\\t_{k-2}\\\text{color}(cyan}\\t_{k-2}\\\text{color}(cyan}\\t_{k-2}\\\text{color}(cyan}\\t_{k-2}\\\

Each step multiplies the signed error $t_k-2$ by $1-2\alpha$.

<table><tr><td>$\alpha $</td><td>Factor $1-2\alpha $</td><td>Starting at $t_0=0$</td><td>Behavior</td></tr><tr><td>$1/4$</td><td>$1/2$</td><td>$0,1,3/2,\ldots$</td><td>Converges to $2$.</td></tr><tr><td>$1$</td><td>$-1$</td><td>$0,4,0,4,\ldots$</td><td>Oscillates.</td></tr><tr><td>$5/4$</td><td>$-3/2$</td><td>$0,5,-5/2,\ldots$</td><td>Diverges.</td></tr></table>

Distance from $2$ shrinks when $|1-2\alpha|<1$, that is, $0<\alpha<1$.

# STOPPING AND OPTIMALITY

For unconstrained differentiable convex $f$, $\$\nablaf(\mathrm{mathbf{x}})=0$ certifies a global minimum.

In computation, monitor the gradient norm, objective changes, and an iteration limit.

A small update alone may reflect a tiny step size.

For $f(t)=t^2$, $t_0=100$, and $\backslash alpha=10^{12}$:

$$|t_1-t_0|=2\times10^{10}\cdot(-10),\backslash\text{quad }f(t_1)\backslash\text{approx}10000.$$

PRACTICE: ONE STEP AND THE OPTIMUM

<table><tr><td>$$r(t)=(t+1)^2+3,\\quad t_0=1,\\quad qquad\alpha=\\\quad tfrac14.\$</td></tr></table>

# PROJECTED GRADIENT DESCENT

Optional background; not assessed in the midterm.

For a nonempty, closed, convex feasible set \mathcal{F}$:

$$P_{\{\mathcal{F}\}}$$

(\mathb{f{z}})=\operatorname{argmin}_{_{\mathrm{mathbf{u}}}\mathrm{in\mathcal{C}}}\\

\mathrm{mathbf{z}}-\mathrm{mathbf{u}}\backslash\underline{{2^{2.}}}\$\

$$\mathrm{mathbf{x}}_{k+1}=\mathrm{P}_{k}\{\mathrm{mathcal}\{\mathrm{F}\}\}\mathrm{bigl}\{\mathrm{mathbf{x}}_{k}-\mathrm{alpha}_{k}\mathrm{nabla f}\{\mathrm{mathbf{x}}_{k}\}\mathrm{bigr}.\$$

Start with $\mathrm{x}_0\mathrm{in}\mathrm{mathcal{F}}$. Take a gradient step, then project back to the feasible set.

# SOLUTION METHODS AND SCOPE

Core: recognize convexity and interpret global minima.

Core: solve $\nabl\ a\ f=0$ and calculate gradient-descent updates for simple unconstrained examples.

Optional background: projected gradient descent.

Newton, interior-point, and subgradient methods are outside this lecture's assessed techniques.

# APPLYING CONVEX OPTIMIZATION

L. Define the variables, objective, and feasible set.

2. Establish convexity of both objective and feasible set.

3. Solve the model and check feasibility and solver status.

4. Interpret the solution in the original problem.

Tools include CVXPY, CVX, and CVXOPT. Modeling systems such as CVXPY recognize specific convex forms; a mathematically convex expression may need rewriting.

# KEY POINTS

Convex sets contain their line segments; convex functions lie below their chords.

Local minima are global, but existence and uniqueness are separate issues.

Gradient descent updates parameters using the negative gradient; step size affects convergence.

Be able to check convexity, calculate an update, and describe all minima of a simple example.

WHY DO WHALES JUMP WHY DO TESTICLES MOVE WHY ARE THERE SPLASHES IN THE BIBLE WHY ARE WITCHES GREEN WHY ARE HATS SO EXPENSES WHY DO TWINS HAVE DIFFERENT FINGERPRINTS WHY IS HITPS CROSSED OUT IN RED WHY ARE THERE MIRRORS ABOVE BEDS WHY DO YOUR BOODS HURT WHY ARE AMERICANS AFRAID OF DRAGONS WHY IS THERE A LINE THROUGH HITPS WHY DO I SAY WHY

WHY IS SEA SALT BETTER

WHY ARE THERE TREES IN THE MIDDLE OF FIELDS

WHY IS THERE NOT A POKEMON MMO

WHY IS THERE LAUGHING IN TV SHOWS

WHY ARE THERE DOORS ON THE FREEWAY

WHY ARE THERE SO MANY SUCHOSTEDE RUNNING

WHY AREN THERE ANY COUNTRIES IN ANTARCTICA

WHY ARE THERE SOARY SOUNDS IN MINECRAFT

WHY IS THERE KICKING IN MY STOMPACH

WHY ARE THERE TWO SLASHES AFTER HITTP

# QUESTIONS FOUND IN GOOGLE AUTOCOMPLETE

WHY AREN'T MY

ARMS GROWING

WHY DO SNAKES EXIST

WHY DO OYSTERS HAVE PEARLS

WHY ARE DUCKS CALLED DUCKS

WHY DO THEY CALL IT THE CLAP

WHY ARE KYLE AND CARTMAN FRIENDS

WHY IS THERE AN ARROW ON AANG'S HEAD

WHY ARE TEXT MESSAGES BLUE

WHY ARE THERE PHELOMUS

WHY ARE THERE SO MANY CROWS IN ROCHESTER, MIN

WHY ARE MY EARS RINGING

WHY DO CHILDREN GET CANCER

WHY DO POSEIDON ANGRY WITH ODYSSEUS

WHY IS THERE ICE IN SPACE

WHY ARE THERE MUSTAGHS ON CLOTHES WHY ARE THERE MUSTAGHS ON CARS WHY ARE THERE MUSTAGHS EVERYWHERE WHY ARE THERE SO MANY BIRDS IN OHIO WHY IS THERE SO MUCH RAIN IN OHIO WHY IS OHIO WEATHER SO WEIRD WHY IS EARTH TILTED WHY IS SPACE BLACK WHY IS OUTER SPACE SO COLD WHY ARE THERE PYRAMIDS ON THE MOON WHY IS NASA SHUTTING DOWN

WHY ARE THERE MALE AND FEMALE BIKES ☎ WHY ARE THERE BRIDESMIPIDS WHY ARE THERE TINY SPIDERS IN MY HOUSE WHY ARE NOT THERE VARDOSE ARIDRES WHY ARE OLD RUNSIONS DIFFERENT

WHY ARE THERE

SQUIRRELS

WHY ARE THERE HUGE SPIDERS IN MY HOUSE WHY ARE THERE LOTS OF SPIDERS IN MY HOUSE WHY ARE THERE SPIDERS IN MY ROOM WHY ARE THERE SO MANY SPIDERS IN MY ROOM WHY DO SPIDER BITES ITCH WHY IS DYING SO SCARY

WHY IS PROGRAMMING SO HARD WHY AREN'T THERE E GRADES WHY IS THERE A O OHM ROCKTOR WHY DO AMERICANS HATE SOCER WHY DO RIMMES SOUND GOOD WHY DO BOYS LIKE ME WHY DO TREES DIE WHY DON'T BOYS LIKE ME WHY IS THERE NO SOUND ON ON WHY AREN'T POKEMON REAL WHY ARE THERE RED DOTS ON MY THGES WHY AREN'T BULLETS SHARP WHY IS LYING GOOD WHY DO DREAMS SEEM SO REAL WHY IS SEX SO IMPORTANT

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2F37efbf7f983641ed8bd649f201acdbc9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089831&Signature=re7mA%2FhUudOEc6qoOAa%2FhBL322g%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2F7aee7c8d691e4ebba38b2e9b3cc58204.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089831&Signature=TNDBAa1aKgeRLRDzGExuPWwcu20%3D)

WHY IS THERE AN OWL IN MY BACKYARD

WHY IS THERE AN OWL OUTSIDE MY WINDOW

WHY IS THERE AN OWL ON THE DOLLAR BILL

WHY DO OWLS ATTACK PEOPLE

WHY ARE AK47s SO EXPENSIVE

WHY ARE THERE HELICOPTERS CIRCLING MY HOUSE

WHY ARE THERE GODS WHY ARE MY BOOBS ITCHY

WHY ARE THERE TWO SPOOKS WHY ARE CIGARETTES LEGAL

WHY IS MT VESUVIUS THERE WHY DO THEY SAY T MINUS WHY ARE THERE OBELISKS WHY ARE WRESTLERS ALWAYS WET WHY ARE OCEANS BECOMING MORE ACIDIC WHY IS ARWEN DYING

WHY IS JESUS WHITE CWHY IS THERE LIQUID IN MY EPR WHY DO Q TIPS FEEL GOOD WHY DO GOOD PEOPLE DIE

WHY AREN'T THERE GUNS IN HARRY POTTER

WHY AREN'T MY QUAIL LAYING EGGS WHY ARE ULTRASOUNDS IMPORTANT WHY AREN'T MY QUAIL EGGS HATCHING WHY IS STEALING WRONG WHY AREN'T THERE ANY FOREIGN MILITARY BASES IN AMERICA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2Ffbed7680a1d247de83cae242ed44749d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089831&Signature=J80vnjQbZK0jogVPZsOmjZSA974%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2F93d2a876616645b58c8c91a9d3764659.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089831&Signature=8%2FRQQXrbzKery%2BGemGNusOS5d38%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fcaf1dcb8c5ce4f2885c2db08cd805763%2Fmedia%2F5f4fd2e3508b440686f5f289a7d4bc81.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089831&Signature=yl4MBQBm1%2BGNzUi6dobE8uKBQ54%3D)
