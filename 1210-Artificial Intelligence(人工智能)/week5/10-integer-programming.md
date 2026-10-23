Integer Programming

CS5491: Artificial Intelligence

ZHICHAO LU

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

# TODAY

Formulate decisions with integer and binary variables.

Use an LP relaxation to bound an integer program.

Solve an integer program by branch and bound.

# LP RECAP: THE DIET PROBLEM

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$$\\begin{aligned} \\min\\quad \\&x_1+0.4x_2\\\\text{s.t.} \\quad \\&2000\\\\left\\100x_1+50x_2\\\\left\\2500,\\\\&3x_1+4x_2\\\\left\\100,\\\\&20x_1+70x_2\\\\left\\700,\\\\&x_1,x_2\\\\end{aligned}$

Unique optimum:

$(12,16).$

Minimum cost: $18.4$.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2F486957624024411eb19fb3d4c846c34b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089732&Signature=EmxDLvt4Y2AuDC9DqXzpK%2FX7Czw%3D)

# FINDING A VERTEX

Choose $n$ independent constraint boundaries for $n$ variables.

Calorie minimum and sugar limit:

Solving gives $(x_1, x_2) = (12, 16)$.

$A_1$: selected rows of $A$.

$\backslash$mathbf{b}_1: matching

entries of $\backslash$mathbf{b}$$.

Set these constraints to

equality:

$$A_I\mathrm{mathbf{x}}=\mathrm{mathbf{b}}_{I}.\$$

Check all original constraints before accepting the point as a vertex.

DISCRETE DECISIONS

<table><tr><td>Decision</td><td>Variable</td><td>Domain</td></tr><tr><td>Number of fixed 8 oz servings</td><td>$n$</td><td>$\mathrm{Z}_{\mathrm{\text{ge0}}}$</td></tr><tr><td>Whether to select an item</td><td>$z$</td><td>$\{0,1\}$</td></tr><tr><td>Amount of a divisible resource</td><td>$t$</td><td>$\mathrm{R}_{\mathrm{\text{ge0}}}$</td></tr><tr><td colspan="3">Define the unit before writing the model. For $n$ servings of 8 oz stir-fry: amount $=8n$ oz, cost $=8n$, calories $=800n$.</td></tr></table>

# LP, ILP AND MILP

<table><tr><td>Model</td><td>Variable domains</td></tr><tr><td>Linear program (LP)</td><td>$x_i\in\mathbb{R}$ for all $i$</td></tr><tr><td>Pure integer linear program (ILP)</td><td>$x_i\in\mathbb{R}$ for all $i$</td></tr><tr><td>Binary integer program</td><td>$x_i\in\mathbb{R}$ for all $i$</td></tr><tr><td>Mixed-integer linear program (MILP)</td><td>Some variables integer; others continuous</td></tr></table>

INTEGER PROGRAMMING EXAMPLE

\begin{aligned}

We will use this model for relaxation, rounding and branching.

# I NTEGER FEASIBLE POINTS

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2Fb24fb22df55e4927ba456bd5146a0557.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089732&Signature=C2xxtskKolaohSQib%2BQYp%2FLDcwo%3D)

LP: every point in the shaded region. IP: only the integer points inside it

# LP RELAXATION

# I nteger program

$$\begin{aligned}&\text{aligned}\begin{aligned}\end{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\begin{aligned}\end{aligned}\begin{aligned}\begin{aligned}\begin{aligned}\begin

# WHY RELAXATION GIVES A BOUND

Every integer feasible point is also LP feasible:

$$P_{\{\mathrm{mathrm{IP}}\}\setminus\mathrm{subseteq P}_{\{\mathrm{mathrm{LP}}\}\}.$$$

Minimizing over a larger set cannot increase the optimum:

$$z^\ast_{\{\mathrm{mathrm{LP}}\}\setminus\mathrm{le z}^\ast_{\{\mathrm{mathrm{IP}}\}\}.}$$$

The LP optimum is a lower bound for minimization.

# CONNECTION TO INFORMED SEARCH

In informed search, solving a relaxed problem can give an optimistic cost estimate.

At a branch-and-bound node, the LP relaxation bounds the best integer solution allowed by that node.

This bound helps rule out branches that cannot improve the current solution.

A* uses $g(n)+h(n)$ to estimate total cost. Here, the node LP bounds the total objective directly.

# CHECK YOUR UNDERSTANDING

For a minimization IP and its LP relaxation with finite optima:

# Statement

$z^\*_\{\mathrm{LP}\}\le z^\*_\{\mathrm{IP}\}$

$\mathrm{x}^{*}_{\_}\{\mathrm{mathrm}\{\mathrm{LP}\}\}=\mathrm{mathbf}\{\mathrm{x}\}^{*}_{\_}\{\mathrm{mathrm}\{\mathrm{IP}\}\}$

An LP-optimal point with integer coordinates solves the IP.

# WHY ROUNDING CAN FAIL

LP optimum: $(3.8,3)$, value $-8.2$.

Nearest rounding gives $(4,3)$:

$5(4)+10(3)=50>49$.

Infeasible.

Nearby feasible $(4,2)$$ costs $-4$, but $(2,2)$$ costs $-6$.

A nearby feasible point need not be optimal.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2Fb1bb9149fa1e4b6987ebe93e3b551e6c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089732&Signature=FkRgnkqNJ8hKsU8gTYe6VLUBvjc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2F3499095ef117459686ba42a1e2f1d16c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089732&Signature=rsxXYaZsZq5HT5Ws4MI8Wi2criM%3D)

Incumbent: the best

feasible integer solution

found so far.

L. Solve the LP relaxation at the current node.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2F687be0c58c7e464396372561d0b8aedd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089733&Signature=7B0xNV7xjnLYlAvLsIAeuXyAwL4%3D)

2. Close the node if it is infeasible, integral, or cannot improve the incumbent.

B. Otherwise, branch on a fractional integer variable.

4. Explore the children, keeping all ancestor constraints.

When no open nodes remain, the best integer solution found is optimal.

# THE BRANCHING RULE

Choose an integer-constrained variable with fractiona value $x_i^*$.

$$x_i\backslash\lfe\lfloor x_i^*\backslashrfloor\qquad\text{or}\backslashqquad x_i\backslashge\lceil\lce{x_i}^*\backslashr\ce{c}\$

Example: $x_i^*=3.8$.

$$x_i\backslash\lfe3\quad\text{or}\backslashqquad x_i\backslashge4.$$

Both children exclude the current fractional solution. Every integer feasible solution belongs to one of the children.

# BOUNDS AND THE INCUMBENT

Node lower bound $L$: the optimal value of its LP relaxation.

Incumbent: the best feasible integer solution found so far.

Global upper bound $U$: the incumbent's objective value.

Start with $U=+\infty$ if no feasible integer solution is known.

When a better integer solution of value $z$ is found, set $U\left\langle\begin{array}{l}\text { The } \\ \text { } \end{array}\right. \text { and store that solution.}$

THREE WAYS TO CLOSE A NODE

<table><tr><td>Case</td><td>Action and reason</td></tr><tr><td>LP is infeasible</td><td>No integer solution can satisfy this node&#x27;s constraints.</td></tr><tr><td>LP optimum is integral</td><td>Update the incumbent if better. This node is solved.</td></tr><tr><td>Bound:  $ \L\backslash ge\ U\ $</td><td>No integer solution in this node can improve the incumbent.</td></tr></table>

Example: $L=-5.4$ and $U=-6$. Prune because $-5.4\ge-6$.

# EXAMPLE: THE FIRST BRANCH

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2F95348e678681497187926d0913ea22c8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089733&Signature=sNE5v%2FseQ5GetpwLUw7UcvClP3Q%3D)

Root: $(3.8,3)$, $L=-8.2$. Branch on $x$ and explore $x\backslash ge4$ first.

# THE FIRST INCUMBENT

Within $x\ge4$, the LP optimum is $(4,2.9)$ with $L=-7.6$.

Branch on $y$: $y\le2$ or $y\ge3$.

<table><tr><td>Additional constraint</td><td>LP result</td><td>Action</td></tr><tr><td>$y\le2$</td><td>$(4,2)$, value</td><td>Integer: set</td></tr><tr><td></td><td>$-4$</td><td>$U=-4$.</td></tr><tr><td>$y\ge3$</td><td>Infeasible</td><td>Close this node.</td></tr><tr><td colspan="3">The $x\ge4$ subtree is finished. Return to $x\ge3$.</td></tr></table>

# I MPROVING THE INCUMBENT

Within $x\le3$: LP optimum $(3,2.6)$, $L=-7.4$. Entering this subtree: $U=-4$.

<table><tr><td>Additional constraints</td><td>LP result</td><td>Action</td></tr><tr><td>$y\ge3$</td><td>Infeasible</td><td>Close.</td></tr><tr><td>$y\le2$</td><td>$(1.8,2)$; $L=-6.2$</td><td>Branch on $x$.</td></tr><tr><td>$y\le2,\times\ge2$</td><td>$(2,2)$; value $-6$</td><td>Integer: update $U=-6$.</td></tr><tr><td>$y\le2,\times\le1$</td><td>$(1,1.6)$; $L=-5.4$</td><td>Prune: $-5.4\ge-6$.</td></tr></table>

Every row inherits $x\le3$ and the original constraints.

# THE COMPLETE SEARCH TREE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2F2d6e7cd5975c454784cf5288a2367038.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089733&Signature=RE%2F9CbtRc1YBtHIMDNpjcuoYwro%3D)

Incumbent: $U=+\infty\backslash\backslash longrightarrow\backslash\backslash -4\backslash\backslash longrightarrow\backslash\backslash -6$. Every leaf is closed.

# OPTIMALITY CERTIFICATE

## $$\backslash mathbf\{x\}^\star=(2,2),\backslash qquad z^\star __{\backslash mathrm\{IP\}}=2-4(2)=-6.$$

<table><tr><td>$\$\\mathbf{x}^*=(2,2),\\quad z^{*}_\{\\\mathrm{IP}\}=2-4(2)=-6.\$\)</td></tr><tr><td>Every leaf is infeasible, solved integrally, or unable to improve $-6$.</td></tr><tr><td>Therefore no unexplored branch can contain a better solution.</td></tr><tr><td>Can we stop at the first integer solution?</td></tr><tr><td>No. Here $-4$ improved to $-6$.</td></tr><tr><td>Why does a lower bound of $-5.4$ allow pruning?</td></tr><tr><td>Every integer descendant costs at least $-5.4&gt;-6$.</td></tr></table>

Every leaf is infeasible, solved integrally, or unable to improve $-6$.

Therefore no unexplored branch can contain a better solution.

WHY DO WHALES JUMP WHY DO TESTICLES MOVE WHY ARE THERE SPLASHES IN THE BIBLE WHY ARE WITCHES GREEN WHY ARE HATS SO EXPENSES WHY DO TWINS HAVE DIFFERENT FINGERPRINTS WHY IS HITPS CROSSED OUT IN RED WHY ARE THERE MIRRORS ABOVE BEDS WHY DO YOUR BOOGS HURT WHY ARE AMERICANS AFRAID OF DRAGONS WHY IS THERE A LINE THROUGH HITPS WHY DO I SAY WHY

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

WHY ARE KYLE AND OARTMAN FRIENDS

WHY IS THERE AN ARROW ON AANG'S HEAD

WHY ARE TEXT MESSAGES BLUE

WHY ARE THERE PHEMOUS

WHY ARE THERE SO MANY CROWS IN ROCHESTER, MIN

WHY ARE MY EARS RINGING

WHY DO CHILDREN GET CANCER

WHY DO POSEIDON ANGRY WITH ODYSSEUS

WHY IS THERE ICE IN SPACE

WHY ARE THERE MUSTACHES ON CARS WHY IS EARTH TILTED WHY ARE THERE MUSTACHES EVERYWHERE WHY IS SPACE BLACK WHY IS THERE SO MUCH RAIN IN OHIO WHY IS OUTER SPACE SO COLD WHY ARE THERE PYRANDS ON THE HOON WHY IS OHIO WEATHER SO WEIRD WHY IS NASA SHUTTING DOWN

WHY ARE THERE MALE AND FEMALE BIKES ☎ WHY ARE THERE BRIDESMIPDS WHY ARE THERE TINY SPIDERS IN MY HOUSE WHY ARE NOT THERE VARDOSE ARIDRES WHY ARE OLD RUNSONS DIFFERENT

WHY ARE THERE

SQUIRRELS

WHY ARE THERE HUGE SPIDERS IN MY HOUSE WHY ARE THERE LOTS OF SPIDERS IN MY HOUSE WHY ARE THERE SPIDERS IN MY ROOM WHY ARE THERE SO MANY SPIDERS IN MY ROOM WHY DO SPIDER BITES ITCH WHY IS DYING SO SCARY

WHY IS PROGRAMMING SO HARD WHY AREN'T THERE E GRADES WHY THERE A O CHM REGARD WHY DO AMERICANS HATE SOCDER WHY DO BOYS LIKE ME WHY DO TREES DIE WHY DON'T BOYS LIKE ME WHY IS THERE NO SOUND ON ON WHY IS THERE, ALWAYS A JAMA UPDATE WHY AREN'T POKEMON REAL WHY ARE THERE RED DOTS ON MY THIGHS WHY AREN'T BULLETS SHARP WHY IS LYING GOOD WHY IS SEX SO IMPORTANT

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2F5945cebf621a46e383aedddeaa2fbd73.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089733&Signature=vivUav3%2BhplpTSOHNJSpYqeRu6o%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2F1d31fdedfe6d497b87efdbf827e48eea.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089733&Signature=Brj3GRkdpVE5TvZTaMfe7aLK0kA%3D)

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

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2Fec894f4150904186a72d0f1d1a026daa.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089733&Signature=g1Brw%2BAe0%2FyqtCjlXDpwK%2BEnsIk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2F57a51edc91784c108268a2eb51ad4385.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089733&Signature=i5pWfnsYK9%2F6eJ4TOazkkm5NKPA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F213d20278904467bbbe4f8af076b15fb%2Fmedia%2Fb4d926e1fd794c7c80504a876ebebdc0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089733&Signature=1HooamiYu6Yh3y0EuTJ9jLIq4b4%3D)
