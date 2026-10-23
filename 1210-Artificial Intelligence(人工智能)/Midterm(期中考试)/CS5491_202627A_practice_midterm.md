# CityU CS5491 AI Practice Midterm

Semester A, 2026/27

Original question paper: Spring 2026, Version A

Name: ___

Student ID: ___

# Practice instructions

Allow 110 minutes for 40 marks. Use physical notes/books only; no electronic devices. The five original question pages follow. This practice paper illustrates question styles; this year's assessed scope also includes integer and convex optimization.

# Conventions and clarifications

Practice scoring: ignore the negative-marking note on the next page. No part can score below zero. The accompanying solutions specify partial credit.

Q1: “Expand” means generate successors. Merely visiting a node at the depth limit is not expansion. Forward checking changes only unassigned neighbors of the newly assigned variable.

Q2: use tree search, keeping different paths to a state separately. A visit is removal from the frontier; test for a goal then. Break ties alphabetically by endpoint label, then by earlier insertion for identical labels. Repeat a state whenever visited again.

Q2 iterative deepening: start at depth limit 0, then 1, 2, and so on. Include visits to cutoff nodes; explore children alphabetically. "Path length" in the original answer spaces means total edge cost, not the number of edges.

Q3: explore left to right; alpha-beta cuts when  $ \alpha \geq \beta $, including equality. Full minimax values and bounds returned after a cutoff need not be identical.

Q4: back-to-back classes do not overlap. Treat each time interval as including its start and excluding its end.

Q5: include  $ x \geq 0 $ and  $ y \geq 0 $, and treat the variables as continuous for the LP. Clearly indicate any feasible region that extends beyond the plotting window.

Marks: Q1: 10 | Q2: 9 | Q3: 9 | Q4: 5 | Q5: 7 | Total: 40

# 1 Multiple Choice Questions

Note: incorrect answers will incur negative points proportional to the number of choices. For example, a 1 point true-false question will receive 1 point if correct, -1 if incorrect, and zero if left blank. Only make informed guesses.

(a) (1 pt) Who are you? Write your name and student ID at the top of the cover page.

(b) (2 pts) Admissible Heuristics. If $f(s)$, $g(s)$, and $h(s)$ are all admissible heuristics then which of the following are also guaranteed to be admissible heuristics:

○ $f(s) + g(s) + h(s)$

○ $f(s)/3 + g(s)/3 + h(s)/3$

○ $f(s)/6 + g(s)/3 + h(s)/2$

○ $f(s) * g(s) * h(s)$

○ $min(f(s), g(s), h(s))$

○ $max(f(s), g(s), h(s))$

(c) (1 pt each - total of 2 pts) CSP. The graph below is a constraint graph for a CSP that has only binary constraints. Initially, no variables have been assigned. For each of the following scenarios, mark all variables for which the specified filtering might result in their domain being changed.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0d1a340f3585432e88ea9e6876ab2337%2Fmedia%2Fd457194e1a1145d3889bf25b1bf3d81f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090792&Signature=4QfxCr9DFZHYhEK69IpvaC7kB%2F0%3D)

i) A value is assigned to A. Which domains might be changed as a result of running forward checking for A?

○ A ○ B ○ C ○ D ○ E ○ F

11) A value is assigned to A, and then forward checking is run for A. Then a value is assigned to B. Which domains might be changed as a result of running forward checking for B?

○ A ○ B ○ C ○ D ○ E ○ F

(c) (1 pt each - total of 5 pts) True or False Circle the correct answer.

i) T F The game, Tic-tac-toe, is fully-observable.

ii) T F In a graph where the goal is neither the root nor at depth one, iterative deepening search will definitely expand more nodes than breadth-first search.

iii) T F A* search with the heuristic h(n) = 0 is equivalent to uniform-cost search.

iv) T F A two variable integer programming problem cannot be solved by the graphical method.

v) T F The union of two convex sets may or may not be convex.

# 2 Informed Search

Given the graph below, suppose you want to go from start state “S” to goal state “G”, write down the order in which the states are visited and the path found by the following search algorithms. Ties (e.g., which child to first explore in depth-first search) should be resolved alphabetically (i.e., prefer A before Z). Remember to include the start and goal states in your answer. Assume that algorithms execute the goal check when nodes are visited, not when their parent is expanded to create them as children. If a state is visited more than once, write it each time.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0d1a340f3585432e88ea9e6876ab2337%2Fmedia%2F7b7585d49cca4437ad7347224eff58f9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090792&Signature=iNqiM2OL7VW6T92loPnFxS5BapU%3D)

(a) (3 pts) Iterative deepening depth first search:

Visited order: ___

Solution (path length: ): ___

(b)  $ (3\ \text{pts}) $ Uniform Cost Search:

Visited order: ___

Solution (path length: ___): ___

(a)  $ (3\ \text{pts})\ \text{A}^*\ \text{Search}\ (\text{assume}\ f(n) = g(n) + h(n)) $:

Visited order: ___

Solution (path length: ___): ___

# 3 Minimax Search

Consider the mini-max tree, whose root is a max node, shown below. Assume that children are explored left to right.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0d1a340f3585432e88ea9e6876ab2337%2Fmedia%2Fe7f004e671c34c4081d978656a3da90f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090792&Signature=Iof%2B%2FUqY4Ivb%2FzqpXK%2BgLbHW%2Bk8%3D)

(a) (2 pts) Fill in the mini-max values for each of the nodes in the tree that aren’t leaf nodes. What is the minimax value for the root?

(b) (5 pts) If  $ \alpha $- $ \beta $ pruning were run on this tree, which branches would be cut? Mark the branches with a slash or a swirl (like a cut) and shade the nodes that don’t get explored.

(c) (2 pts) Is there another ordering for the children of the root for which more pruning would result? If so, state the order.

# 4 Course Scheduling

You are in charge of scheduling electrical engineering classes that meet on Mondays, Wednesdays, and Fridays. There are 5 classes that meet on these days and 3 professors who will be teaching these classes. You are constrained by the fact that each professor can only teach one class at a time.

The classes are:

1. Class 1 - Circuits and Systems: meets from 8:00 - 9:00 am

2. Class 2 - Digital Logic Fundamentals: meets from 8:30 - 9:30 am

3. Class 3 - Electromagnetic Fields and Waves: meets from 9:00 - 10:00 am

4. Class 4 - Control Systems: meets from 9:00 - 10:00 am

5. Class 5 - Microprocessors and Digital Systems: meets from 9:30 - 10:30 am

The professors are:

1. Professor A, who is qualified to teach Classes 3 and 4.

2. Professor B, who is qualified to teach Classes 2, 3, 4, and 5.

3. Professor C, who is qualified to teach Classes 1, 2, 3, 4, and 5.

(2 pts) Formulate this problem as a CSP problem in which there is one variable per class, stating the domains, and constraints. Constraints should be specified formally and precisely, but may be implicit rather than explicit.

(b) (2 pts) Draw the constraint graph associated with your CSP.

(c) (1 pts) Give one solution to this CSP (i.e., a solution that satisfies all constraints).

# 5 Linear Programming

In order to supplement his daily diet, someone wishes to take some Xtravit and some Yeastalife tablets. Their content of iron, calcium, and vitamins (in milligrams per tablet) are shown in the table below.

<table><tr><td>Tablet</td><td>Iron</td><td>Calcium</td><td>Vitamin</td></tr><tr><td>Xtravit</td><td>6</td><td>3</td><td>2</td></tr><tr><td>Yeastalife</td><td>2</td><td>3</td><td>4</td></tr></table>

(2 pts) By taking x tablets of Xtravit and y tablets of Yeastalife, the person expects to receive at least 18 milligrams of iron, 21 milligrams of calcium, and 16 milligrams of vitamins. Write these conditions down as three inequalities in terms of x and y.

(b) (3 pts) In the provided coordinate plane below, illustrate the region of those points  $ (x, y) $ which simultaneously satisfy all the constraints.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0d1a340f3585432e88ea9e6876ab2337%2Fmedia%2F2a871e2476914796a5c14abd91ca71cb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090792&Signature=NfzBncCtaTqwlRy1jH42hBVYgWE%3D)

(c) (2 pts) If Xtravit tablets cost $10 each and the Yeastalife tablets cost $5 each, how many tablets of each should the person take in order to satisfy the above requirements at minimum cost?
