Optimization

CS5491: Artificial Intelligence

ZHICHAO LU

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

# ANNOUNCEMENTS

Midterm: Thursday, 22 October 2026

20% of the course grade; attend your enrolled session.

Printed-materials-only open book; no electronic devices.

Project proposal: 15 October, 11:59 pm BJT.

Use the practice paper and solutions to prepare.

# TODAY: MODELING OPTIMIZATION

LP and IP are examples of a more general framework.

Identify the decision variables, feasible set, and objective.

Distinguish a feasible point, an optimal solution, and the optimal value.

Formulate examples and check what a solver returns.

# AN OPTIMIZATION MODEL

$$ \operatorname*{m i n}_{\mathbf{x}\in\mathcal{F}}f(\mathbf{x}) $$

<table><tr><td>Component</td><td>Meaning</td></tr><tr><td>Decision variables  $ \mathbf{x} $</td><td>Quantities we choose.</td></tr><tr><td>Feasible set  $ \mathbf{F} $</td><td>Choices satisfying all domain restrictions and constraints.</td></tr><tr><td>Objective  $ f: \mathcal{F} \rightarrow \mathbb{R} $</td><td>The value we want to minimize.</td></tr></table>

$$ f(\mathbf{x})=\mathbf{c}^{T}\mathbf{x},\mathcal{F}=\{\mathbf{x}:A\mathbf{x}\leq\mathbf{b}\} $$

V ARIABLE DOMAINS AND CONSTRAINTS

<table><tr><td>Variable</td><td>Example</td><td>Example decision</td></tr><tr><td>type</td><td>domain</td><td></td></tr><tr><td>Continuous</td><td>$ a \in \mathbb{R} $</td><td>A regression slope.</td></tr><tr><td>Discrete</td><td>$ z \in \{0, 1\} $</td><td>Whether to select an item.</td></tr><tr><td>Mixed</td><td>$ (a, z) \in \mathbb{R} \times \{0, 1\} $</td><td>A quantity and an on/off choice.</td></tr><tr><td colspan="3">Additional constraints can further restrict these choices.</td></tr><tr><td colspan="3">Unconstrained optimization here means  $ \mathcal{F} = \mathbb{R}^n $.</td></tr><tr><td colspan="3">Example: requiring a nonnegative slope gives  $ \mathcal{F} = [0, \infty) $</td></tr></table>

# OPTIMAL SOLUTIONS AND VALUES

When a minimum is attained:

$$ \underset{\mathbf{x}\in\mathcal{F}}{\mathbf{x}^{*}\in\operatorname{a r g m i n}_{\mathbf{x}\in\mathcal{F}}f(\mathbf{x}),}\qquad f^{*}=\operatorname*{m i n}_{\mathbf{x}\in\mathcal{F}}f(\mathbf{x})=f(\mathbf{x}^{*}). $$

argmin: the set of all optimal choices.

$ f^{*} $: the optimal objective value, a number.

Example: minimize  $ t^2 $ over  $ \mathcal{F} = \{-1, 1\} $.

$$ \operatorname{a r g m i n}_{t\in\mathcal{F}}t^{2}=\{-1,1\},\qquad f^{*}=1. $$

DOES AN OPTIMAL SOLUTION EXIST?

<table><tr><td>Problem</td><td>Outcome</td></tr><tr><td>$ \min t, t \in [0, 1] $</td><td>Attained:  $ t^* = 0 $, value 0.</td></tr><tr><td>$ \min t, t \in \mathbb{R} $</td><td>Unbounded below.</td></tr><tr><td>$ \min t, t &gt; 1 $ and  $ t \leq 0 $</td><td>Infeasible: no allowed choice.</td></tr></table>

# MINIMIZATION AND MAXIMIZATION

Define  $ g(\mathbf{x}) = -f(\mathbf{x}) $ on the same feasible set.

$$ \operatorname{a r g m i n}_{\mathbf{x}\in\mathcal{F}}f(\mathbf{x})=\operatorname{a r g m a x}_{\mathbf{x}\in\mathcal{F}}g(\mathbf{x}). $$

The optimal choices are the same. When attained, the optimal values satisfy  $ g^{*} = -f^{*} $.

Example:  $ \mathcal{F} = \{2, 5\}, f(t) = t $, and  $ g(t) = -t $.

$ t^{*}=2 $ in both problems;

$$ f^{*}=2,\quad g^{*}=-2. $$

# TRAVELING SALESMAN PROBLEM

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2Fca66afe2d2c0458cbb46e1f882452ae4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089756&Signature=b5QOhQJkmLLtix6lYz9dPyvKHzA%3D)

Data: distances $d(i, j)$.

Decision: a visiting order $\mathbf{x} = (x_{1}, \ldots, x_{n})$.

Feasible set: all permutations of the n cities.

$$ f(\mathbf{x})=\sum_{k=1}^{n-1}d(x_{k},x_{k+1})+d(x_{n},x_{1}). $$

The closing edge returns to the start; this tour has length 10.

# 8

QUEENS AS A FEASIBILITY PROBLEM

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2F2cc4a5aaeab3421a85e79ed9f9fc2c38.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089756&Signature=xaADSoLTpM0isEsuq%2FE1VT2B9Cg%3D)

$ x_{i} $: row of the queen in column i.

$$ x_{i}\in\{1,\dots,8\}. $$

For every  $ 1 \leq i < j \leq 8 $:

$$ \begin{array}{r}{x_{i}\neq x_{j},}\\ {}\\ {|x_{i}-x_{j}|\neq|i-j|.}\end{array} $$

One queen per column is built into the representation. Minimize the constant objective  $ f(\mathbf{x}) = 0 $ over these constraints. Every feasible placement is optimal.

**FITTING A LINE THROUGH THE ORIGIN**

Given observations:  $ (1, 2.1) $,  $ (2, 3.98) $,  $ (3, 7.0) $.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2Fe79b8d788240483495303af712eec92a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089756&Signature=kSmT8OtJUN0AFqKEb8Itl%2BaL%2Flg%3D)

Decision: slope  $ a \in \mathbb{R} $. Prediction:  $ \hat{y}_i = ax_i $.

Residual:  $ e_i(a) = y_i - ax_i $. The pictured  $ a = 2 $ is a candidate.

**CHOOSE AN ERROR OBJECTIVE**

What objective would make the residuals $e_{i}(a)=y_{i}-ax_{i}$ small?

Absolute error

Squared error

$$ L_{1}(a)=\sum_{i=1}^{3}|y_{i}-a x_{i}|.\qquad L_{2}(a)=\sum_{i=1}^{3}(y_{i}-a x_{i})^{2}. $$

At a = 2, the residuals are (0.10, -0.02, 1.00):

$ L_{1}(2) = 1.12 \text{ and } L_{2}(2) = 1.0104. $

Compare candidates using the same loss; these two values have different scales.

**THE LOSS CHANGES THE BEST FIT**

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2F2411660c840b4d588c9f99ea60d155aa.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089756&Signature=UmV0%2FWRQaC3IcgQoTMaW2qxhgdk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2Fa2735f9c1d4c4df7a20cccff7d5b557c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089756&Signature=zis4qjGdfWnY9Basl9VXdRnTM1s%3D)

Absolute error has an interval of best slopes. Squared error has one best slope. Both are convex; convexity does not guarantee uniqueness.

**RECOGNIZING PROBLEM STRUCTURE**

<table><tr><td>Model</td><td>Structure that matters</td></tr><tr><td>Linear program</td><td>Linear objective and linear constraints; continuous variables.</td></tr><tr><td>Integer / mixed-integer program</td><td>Some or all variables must take integer values.</td></tr><tr><td>Convex minimization</td><td>Convex objective over a convex feasible set.</td></tr></table>

LP is a special case of convex optimization.

Integer restrictions generally make a feasible set nonconvex.

Both regression losses are nonlinear but convex.

**SOLVING AND CHECKING A MODEL**

1. Formulate the variables, constraints, and objective.

2. Choose a method suited to the model's structure.

3. Solve and inspect the reported status.

4. Check feasibility and recompute the objective.

5. Interpret the result in the original problem.

A feasible point need not be optimal. A solver may also report infeasibility, unboundedness, or an unfinished search.

**CHECK THE MODEL**

Fit  $ \hat{y}_i = ax_i $ to the same observations, requiring  $ a \geq 0 $ and minimizing squared error.

<table><tr><td>Question</td><td>Answer</td></tr><tr><td>What is chosen?</td><td>The slope  $ a $.</td></tr><tr><td>What data are given?</td><td>The observations  $ (x_i, y_i) $.</td></tr><tr><td>What is the feasible set?</td><td>$ \mathcal{F} = [0, \infty) $.</td></tr><tr><td>What is the objective?</td><td>$ f(a) = \sum_{i=1}^{3} (y_i - ax_i)^2 $.</td></tr><tr><td>Is this a linear program?</td><td>No: the objective is quadratic in  $ a $.</td></tr></table>

**KEY POINTS**

Separate what is chosen from what is known.

Feasibility, optimality, and the optimal value are different concepts.

The representation and objective determine the optimization problem.

Check a solver's result before interpreting it.

Next: how do convex sets and convex objectives help us solve these models?

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

**QUESTIONS FOUND IN GOOGLE AUTOCOMPLETE**

WHY AREN'T MY

ARMS GROWING

WHY DO SNAKES EXIST

WHY DO OYSTERS HAVE PEARLS

WHY ARE DUCKS CALLED DUCKS

WHY DO THEY CALL IT THE CLAP

WHY ARE KYLE AND OARTMAN FRIENDS

WHY IS THERE AN ARROW ON AANG'S HEAD

WHY ARE TEXT MESSAGES BLUE

WHY ARE THERE PHEMOUS

WHY ARE THERE SO MANY CROWS IN ROCHESTER, MIN

WHY ARE MY EARS RINGING

WHY DO CHILDREN GET CANCER

WHY DO POSEIDON ANGRY WITH ODYSSEUS

WHY IS THERE ICE IN SPACE

WHY ARE THERE MUSTAGHS ON CLOTHES WHY ARE THERE MUSTAGHS ON CARS WHY ARE THERE MUSTAGHS EVERYWHERE WHY ARE THERE SO MANY BIRDS IN OHIO WHY IS THERE SO MUCH RAIN IN OHIO WHY IS OHIO WEATHER SO WEIRD WHY IS EARTH TILTED WHY IS SPACE BLACK WHY IS OUTER SPACE SO COLD WHY ARE THERE PYRAMIDS ON THE MOON WHY IS NASA SHUTTING DOWN

WHY ARE THERE MALE AND FEMALE BIKES ☎ WHY ARE THERE BRIDESMIPIDS WHY ARE THERE TINY SPIDERS IN MY HOUSE WHY ARE NOT THERE VARDOSE ARIDRES WHY ARE OLD RUNSIONS DIFFERENT

WHY ARE THERE

SQUIRRELS

WHY ARE THERE HUGE SPIDERS IN MY HOUSE

WHY ARE THERE LOTS OF SPIDERS IN MY HOUSE

WHY ARE THERE SPIDERS IN MY ROOM

WHY ARE THERE SO MANY SPIDERS IN MY ROOM

WHY DO SPIDER BITES ITCH

WHY IS DYING SO SCARY

WHY IS PROGRAMMING SO HARD WHY AREN'T THERE E GRADES WHY IS THERE A O OHM ROCKTOR WHY DO AMERICANS HATE SOCER WHY DO RIMMES SOUND GOOD WHY DO BOYS LIKE ME WHY DO TREES DIE WHY DON'T BOYS LIKE ME WHY IS THERE NO SOUND ON ON WHY AREN'T POKEMON REAL WHY ARE THERE RED DOTS ON MY THINGS WHY AREN'T BULLETS SHARP WHY IS LYING GOOD WHY DO DREAMS SEEM SO REAL WHY IS SEX SO IMPORTANT

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2F13fae5a316474cfc8dd339ee343a3fe3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089756&Signature=8HQUxmu4sGm5cWXMli3WgszTMKQ%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2Fcc959988e0c6471fbbe1f592d29627dd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089757&Signature=Xtfo%2FmaA%2FGBlUB8PI%2F2LjnqzI%2FE%3D)

WHY IS THERE AN OWL IN MY BACKYARD

WHY IS THERE AN OWL OUTSIDE MY WINDOW

WHY IS THERE AN OWL ON THE DOLLAR BILL

WHY DO OWLS ATTACK PEOPLE

WHY ARE AK475 SO EXPENSIVE

WHY ARE THERE HELICOPTERS CIRCLING MY HOUSE

WHY ARE THERE GODS WHY ARE MY BOOBS ITCHY

WHY ARE THERE TWO SPOOKS WHY ARE CIGARETTES LEGAL

WHY IS MT VESUVIUS THERE WHY DO THEY SAY T MINUS WHY ARE THERE OBELISKS WHY ARE WRESTLERS ALWAYS WET WHY ARE OCEANS BECOMING MORE ACIDIC WHY IS ARWEN DYING

WHY IS JESUS WHITE CWHY IS THERE LIQUID IN MY EPR WHY DO Q TIPS FEEL GOOD WHY DO GOOD PEOPLE DIE

WHY AREN'T THERE GUNS IN HARRY POTTER

WHY AREN'T MY QUAIL LAYING EGGS WHY ARE ULTRASOUNDS IMPORTANT WHY AREN'T MY QUAIL EGGS HATCHING WHY IS STEALING WRONG WHY AREN'T THERE ANY FOREIGN MILITARY BASES IN AMERICA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2F05088f1bb68e4f34b56ffcaa57addf2d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089757&Signature=Rmk808LKqm%2FNEvM9DLuwYNjXJr8%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2Fbab689ce99314185a0d23a13378ed2db.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089757&Signature=24nyJJWml8%2B%2BaPkqqthVN4goYHY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F18f4b3c051b54db3aebcf422ca5ce71f%2Fmedia%2Fa6f9f3f719ab48cdadff32794d186406.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089757&Signature=QI7nSYfbBIUOY7aO8EA43qYwxW4%3D)
