# Constraint Satisfaction

CS5491: Artificial Intelligence

ZHICHAO LU

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

# TODAY

Part 1: Constraint Satisfaction Problems

• Formulation, examples, varieties

• Naive search over CSPs

Part 2: Backtracking Search

• Filtering, ordering, structure

Reading

• Today's Lecture: RN Chapter 6

MY HOBBY:

EMBEDDING NP-COMPLETE PROBLEMS IN RESTAURANT ORDERS

Next Lecture: RN Chapter 5

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Fa658c9f000b845278b6770419caf5fe5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089894&Signature=IixfJMVn6RqNzjxPMOAt5EK5MpY%3D)

# WHAT IS SEARCH FOR?

# WHAT IS SEARCH FOR?

Given assumptions about the world: a single agent, deterministic actions, fully observed state, discrete state space

# WHAT IS SEARCH FOR?

Given assumptions about the world: a single agent, deterministic actions, fully observed state, discrete state space

• Planning: sequences of actions

• The path to the goal is the important thing

• Paths have various costs, depths

• Heuristics give problem-specific guidance

# WHAT IS SEARCH FOR?

Given assumptions about the world: a single agent, deterministic actions, fully observed state, discrete state space

• Planning: sequences of actions

• The path to the goal is the important thing

• Paths have various costs, depths

• Heuristics give problem-specific guidance

• Identification: assignments to variables

• The goal itself is important, not the path

• All paths at the same depth (for some formulations)

• CSPs are a specialized class of identification problems

# CONSTRAINT SATISFACTION PROBLEMS

# WHAT ARE CONSTRAINT SATISFACTION PROBLEMS?

# WHAT ARE CONSTRAINT SATISFACTION PROBLEMS?

Standard search problems:

• State is a "black box": arbitrary data structure

• Goal test can be any function over states

• Successor function can also be anything

# WHAT ARE CONSTRAINT SATISFACTION PROBLEMS?

Standard search problems:

• State is a "black box": arbitrary data structure

• Goal test can be any function over states

• Successor function can also be anything

Constraint satisfaction problems (CSPs):

• A special subset of search problems

• State is defined by variables  $ \mathbf{X}_{i} $ with values from a domain  $ \mathcal{D} $ (sometimes  $ \mathcal{D} $ depends on i)

• Goal test is a set of constraints specifying allowable combinations of values for subsets of variables

# WHAT ARE CONSTRAINT SATISFACTION PROBLEMS?

Standard search problems:

- State is a "black box": arbitrary data structure

- Goal test can be any function over states

- Successor function can also be anything

Constraint satisfaction problems (CSPs):

• A special subset of search problems

• State is defined by variables  $ X_{i} $ with values from a domain D (sometimes D depends on i)

• Goal test is a set of constraints specifying allowable combinations of values for subsets of variables

Allows useful general-purpose algorithms with more power than standard search algorithms

# CSP EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F1905f7dd8c8a44fa8cdfb2eddf52d459.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089894&Signature=m%2BRHVGHn9w5nESfFDfOwklg2J5M%3D)

Western Australia

Northern Territory

Queensland

South Australia

New South Wales

Victoria

# EXAMPLE: MAP COLORING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Ffa9ef45265d14c17931e99eeeeb4db19.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089894&Signature=ICiwi6V1iGbN6DCKdklhlRbgDwU%3D)

# EXAMPLE: MAP COLORING

Variables: WA, NT, Q, NSW, V, SA, T

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Fd2a73694f52b466481d32b9e62bf7cbb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089894&Signature=oYdXmgSyer5MA29Amn7zM%2Fp0H2M%3D)

# EXAMPLE: MAP COLORING

Variables: WA, NT, Q, NSW, V, SA, T

Domains:  $ D = \{red, green, blue\} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F5389efb82ee24d7f923813a506d7e445.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089895&Signature=yB9760Fv1XW3LyBeAthWy%2Bwfj3U%3D)

# EXAMPLE: MAP COLORING

Variables: WA, NT, Q, NSW, V, SA, T

Domains:  $ D = \{red, green, blue\} $

Constraints: adjacent regions must have different colors

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F80e12055c3d049ff982f2fb814544983.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089895&Signature=421F21Nq%2F35O4fhpreUo2K8AUWQ%3D)

# EXAMPLE: MAP COLORING

Variables: WA, NT, Q, NSW, V, SA, T

Domains: D = {red, green, blue}

Constraints: adjacent regions must have different colors

• Implicit:  $ WA \neq NT $

• Explicit:  $ (WA, NT) \in \{(red, green), (red, blue), \ldots\} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Ff00b91aa73444dfcb28a080b67057c8c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089895&Signature=XfvGOQm7I%2BzL5Gn7%2Fn2q0jwarhk%3D)

# EXAMPLE: MAP COLORING

Variables: WA, NT, Q, NSW, V, SA, T

Domains: D = {red, green, blue}

Constraints: adjacent regions must have different colors

• Implicit:  $ WA \neq NT $

• Explicit:  $ (WA, NT) \in \{(red, green), (red, blue), \ldots\} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F2e82c1fb49074c24aeef19d882501930.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089895&Signature=VaUnhXUdEayjwMnKZz2MV%2FN%2B%2FQA%3D)

Solutions: Assignments that satisfy all constraints, e.g.:

# EXAMPLE: MAP COLORING

Variables: WA, NT, Q, NSW, V, SA, T

Domains: D = {red, green, blue}

Constraints: adjacent regions must have different colors

• Implicit:  $ WA \neq NT $

• Explicit:  $ (WA, NT) \in \{(red, green), (red, blue), \ldots\} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Fdc14c402919c4181a15e192f7426b1b3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089895&Signature=3wR2YHV8W9rT6QJztwrcNvvSaXc%3D)

Solutions: Assignments that satisfy all constraints, e.g.:

- {WA=red, NT=green, Q=red, NSW=green, V=red, SA=blue, T=green}

# CONSTRAINT GRAPHS

# CONSTRAINT GRAPHS

Binary CSP: each constraint relates two variables

# CONSTRAINT GRAPHS

Binary CSP: each constraint relates two variables

Constraint Graph: nodes are variables, arcs are constraints

# CONSTRAINT GRAPHS

Binary CSP: each constraint relates two variables

Constraint Graph: nodes are variables, arcs are constraints

General-purpose CSP algorithms use the graph structure to speed up search. E.g., Tasmania is an independent subproblem.

# CONSTRAINT GRAPHS

Binary CSP: each constraint relates two variables

Constraint Graph: nodes are variables, arcs are constraints

General-purpose CSP algorithms use the graph structure to speed up search. E.g., Tasmania is an independent subproblem.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Fff730b5edb304f8aadbeb9c36eb7c723.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089895&Signature=W8jtJ2g54lkg%2FLwyFGGttPb7xuY%3D)

# EXAMPLE: N QUEENS

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F027d6fe22b2b4b3bafab8a57a56dfa4f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089895&Signature=niHuaA%2ByLzjYLUc5%2FYh3f5JoqAM%3D)

# EXAMPLE: N QUEENS

Formulation 1:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Fa12ffe2ce08a4b03a81c24c5258ded96.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089895&Signature=bnPNg6WG9sRD6v2cGJ5S4DZ%2BsNs%3D)

# EXAMPLE: N QUEENS

Formulation 1:

Variables:  $ X_{ij} $

• Domains:  $ \{0, 1\} $

Constraints:

$$ \forall i,j,k(X_{i j},X_{i k})\in\{(0,0),(0,1),(1,0)\} $$

$$ \forall i,j,k(X_{i j},X_{k j})\in\{(0,0),(0,1),(1,0)\} $$

$$ \forall\;i,j,k\;(X_{i j},X_{i+k,j+k})\in\{(0,0),(0,1),(1,0)\} $$

$$ \forall i,j,k(X_{i j},X_{i+k,j-k})\in\{(0,0),(0,1),(1,0)\} $$

$$ \sum_{i j}X_{i j}=N $$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F5bb4441aed834cefa706996798c632f1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=%2BMiABfGGgJwh%2Bd8wwugFM%2FFiouU%3D)

# EXAMPLE: N QUEENS

<table><tr><td>Q1</td><td></td><td></td><td></td></tr><tr><td>Q2</td><td></td><td></td><td>业</td></tr><tr><td>Q3</td><td></td><td></td><td></td></tr><tr><td>Q4</td><td></td><td></td><td>业</td></tr></table>

# EXAMPLE: N QUEENS

Formulation 2:

# Q1 Q2 Q3 Q4

# EXAMPLE: N QUEENS

Formulation 2:

• Variables:  $ Q_{k} $

• Domains:  $ \{1, 2, 3, \ldots, N\} $

Constraints:

• Implicit:  $ \forall(i,j) $ non-threatening  $ (Q_i,Q_j) $

• Explicit:  $ (Q_{1}, Q_{2}) \in \{(1, 3), (1, 4), \ldots\} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Fe00f28a8352b446f992ebf5d5b2ce3fe.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=f73p2PfBXZm1SFRnnIBezba4URA%3D)



# V ARIETIES OF CSPS

Discrete Variables

# V ARIETIES OF CSPS

Discrete Variables

• Finite domains

# V ARIETIES OF CSPS

Discrete Variables

• Finite domains

• Size $d$ means $\mathcal{O}(d^{n})$ complete assignments

E.g., Boolean CSPs, including Boolean satisfiability (NP-complete)

# V ARIETIES OF CSPS

Discrete Variables

• Finite domains

• Size $d$ means $\mathcal{O}(d^{n})$ complete assignments

• E.g., Boolean CSPs, including Boolean satisfiability (NP-complete)

• Infinite domains (integers, strings, etc.)

E.g., job scheduling, variables are start/end times for each job

• Linear constraints solvable, nonlinear undecidable

# V ARIETIES OF CSPS

Discrete Variables

• Finite domains

• Size $d$ means $\mathcal{O}(d^{n})$ complete assignments

• E.g., Boolean CSPs, including Boolean satisfiability (NP-complete)

• Infinite domains (integers, strings, etc.)

E.g., job scheduling, variables are start/end times for each job

• Linear constraints solvable, nonlinear undecidable

Continuous variables

• E.g., start/end times for Hubble Telescope observations

• Linear constraints solvable in polynomial time by LP methods

# V ARIETIES OF CONSTRAINTS

Varieties of Constraints

# V ARIETIES OF CONSTRAINTS

Varieties of Constraints

• Unary constraints involve a single variable (equivalent to reducing domains), e.g.:  $ SA \neq green $

# V ARIETIES OF CONSTRAINTS

Varieties of Constraints

• Unary constraints involve a single variable (equivalent to reducing domains), e.g.:  $ SA \neq green $

• Binary constraints involve pairs of variables, e.g.:  $ SA \neq WA $

# V ARIETIES OF CONSTRAINTS

Varieties of Constraints

• Unary constraints involve a single variable (equivalent to reducing domains), e.g.:  $ SA \neq green $

- Binary constraints involve pairs of variables, e.g.:  $ SA \neq WA $

• Higher-order constraints involve 3 or more variables: e.g., cryptarithmetic column constraints

# V ARIETIES OF CONSTRAINTS

Varieties of Constraints

• Unary constraints involve a single variable (equivalent to reducing domains), e.g.:  $ SA \neq green $

- Binary constraints involve pairs of variables, e.g.:  $ SA \neq WA $

• Higher-order constraints involve 3 or more variables: e.g., cryptarithmetic column constraints

Preferences (soft constraints):

• E.g., red is better than green

• Often representable by a cost for each variable assignment

- Leads to constrained optimization problems

# REAL-WORLD CSPS

Scheduling problems: e.g., when can we all meet?

Timetabling problems: e.g., which class is offered when and where?

Assignment problems: e.g., who teaches what class

Hardware configuration

Transportation scheduling

Factory scheduling

Circuit layout

Fault diagnosis

# SOLVING CSPS

# STANDARD SEARCH FORMULATION

Standard search formulation of CSPs

# STANDARD SEARCH FORMULATION

Standard search formulation of CSPs

States defined by the values assigned so far (partial assignments)

- Initial state: the empty assignment, {}

Successor function: assign a value to an unassigned variable

• Goal test: the current assignment is complete and satisfies all constraints

# STANDARD SEARCH FORMULATION

Standard search formulation of CSPs

States defined by the values assigned so far (partial assignments)

- Initial state: the empty assignment, {}

Successor function: assign a value to an unassigned variable

• Goal test: the current assignment is complete and satisfies all constraints

Start with straightforward search and then improve.

# SEARCH METHODS

What would BFS do?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F1c85904bc5b34c328b352304d1de205a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=Zax3KtyzGWlhf59YyT8QnEvGJ7E%3D)

# SEARCH METHODS

What would BFS do?

• Expands every partial assignment first: no solution before depth n

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F1d4077fb4cd94549973ff22fedbe6b1f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=EtDz5JrA8J%2Bx%2FIuBhfGV9zQP%2F0w%3D)

# SEARCH METHODS

What would BFS do?

• Expands every partial assignment first: no solution before depth n

What would DFS do?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F789f39427775442a8725281797c6d8d8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=%2FCsnCNZ9IWHpwyq4WUflAXIdUng%3D)

# SEARCH METHODS

What would BFS do?

• Expands every partial assignment first: no solution before depth n

What would DFS do?

- Reaches depth n fast, but branches over every unassigned variable and value, and checks constraints only at the goal

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Fdd6239302c2142a79d6bc1b78b2ce690.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=6MLcfrgTwYw6Ft9MGYVh1x5Is2U%3D)

# SEARCH METHODS

# What would BFS do?

• Expands every partial assignment first: no solution before depth n

What would DFS do?

• Reaches depth n fast, but branches over every unassigned variable and value, and checks constraints only at the goal

What problems does naïve search have?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2Fcc75e319566e4bd8bed03d2729b71f4d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=PlM352Sxyz4OZNiiArZu0ZDrd3U%3D)

# SEARCH METHODS

What would BFS do?

• Expands every partial assignment first: no solution before depth n

What would DFS do?

- Reaches depth n fast, but branches over every unassigned variable and value, and checks constraints only at the goal

What problems does naïve search have?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F3f381e3f7a214acfbcf7a760ef4b38cc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=SocBTfmVcltYkwlITujAL1773Xo%3D)

• Ignores that assignments commute (n! orderings of the same assignment); detects violations only at the end

# Q & A

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F9c5b72d7abc24b119ade09a88c908be6%2Fmedia%2F5482571368224fb9921300d066ef2079.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089896&Signature=AweIpSoj1vBKdC%2BalamOTpAfSuA%3D)
