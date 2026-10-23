# Constraint Satisfaction - II

CS5491: Artificial Intelligence

ZHICHAO LU

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

# TODAY

Backtracking Search

Improvements to Backtracking Search:

Problem Structure

• Ordering

• Filtering

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F2a286469bc2848eabec05918cc6b7ddb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089982&Signature=S%2F8zJY8FwGqfGbNcFvTmKwaA%2Fzo%3D)

Backtracking search on the map

Reading

• Today's Lecture: RN Chapter 6

• Next Lecture: RN Chapter 5.1-5.3

# BACKTRACKING SEARCH

# BACKTRACKING SEARCH

# BACKTRACKING SEARCH

Backtracking search is the basic uninformed algorithm for solving CSPs

# BACKTRACKING SEARCH

Backtracking search is the basic uninformed algorithm for solving CSPs

Idea 1: One variable at a time

# BACKTRACKING SEARCH

Backtracking search is the basic uninformed algorithm for solving CSPs

Idea 1: One variable at a time

• Variable assignments are commutative, so fix ordering

• Problem is commutative if order of application of any given set of actions has no effect on outcome.

i.e., [WA = red then NT = green] same as [NT = green then WA = red]

• Only need to consider assignments to a single variable at each step

# BACKTRACKING SEARCH

Backtracking search is the basic uninformed algorithm for solving CSPs

Idea 1: One variable at a time

• Variable assignments are commutative, so fix ordering

• Problem is commutative if order of application of any given set of actions has no effect on outcome.

i.e., [WA = red then NT = green] same as [NT = green then WA = red]

Only need to consider assignments to a single variable at each step

Idea 2: Check constraints as you go

i.e. consider only values which do not conflict with previous assignments

• Might have to do some computation to check the constraints

• "Incremental goal test"

# BACKTRACKING SEARCH

Backtracking search is the basic uninformed algorithm for solving CSPs

• Variable assignments are commutative, so fix ordering

• Problem is commutative if order of application of any given set of actions has no effect on outcome.

i.e., [WA = red then NT = green] same as [NT = green then WA = red]

Only need to consider assignments to a single variable at each step

Idea 2: Check constraints as you go

i.e. consider only values which do not conflict with previous assignments

• Might have to do some computation to check the constraints

"Incremental goal test"

DFS with these two improvements is called backtracking search (not the best name)

Can solve n-queens for  $ n \approx 25 $

# BACKTRACKING EXAMPLE

# BACKTRACKING EXAMPLE

# BACKTRACKING EXAMPLE

# BACKTRACKING EXAMPLE

$$ \begin{array}{c} \downarrow\quad\downarrow\quad\downarrow\\ \downarrow\quad\downarrow\\ \downarrow\quad\downarrow\end{array} $$

# BACKTRACKING SEARCH

function BACKTRACKING-SEARCH(csp) returns solution/failure

return RECURSIVE-BACKTRACKING({ }, csp)

function RECURSIVE-BACKTRACKING(assignment, csp) returns soln/failure

if assignment is complete then return assignment

var ← SELECT-UNASSIGNED-VARIABLE(VARIABLES[csp], assignment, csp)

for each value in ORDER-DOMAIN-VALUES(var, assignment, csp) do

if value is consistent with assignment given CONSTRAINTS[csp] then

add {var = value} to assignment

result ← RECURSIVE-BACKTRACKING(assignment, csp)

if result ≠ failure then return result

remove {var = value} from assignment

return failure

# Backtracking = DFS + variable-ordering + fail-on-violation

# I MPROVING BACKTRACKING SEARCH

# I MPROVING BACKTRACKING SEARCH

General-purpose ideas give huge gains in speed

• Backtracking is uninformed; these ideas play the role that heuristics played in search

# I MPROVING BACKTRACKING SEARCH

General-purpose ideas give huge gains in speed

• Backtracking is uninformed; these ideas play the role that heuristics played in search

Ordering:

# I MPROVING BACKTRACKING SEARCH

General-purpose ideas give huge gains in speed

• Backtracking is uninformed; these ideas play the role that heuristics played in search

# Ordering:

• Which variable should be assigned next?

• In what order should its values be tried?

# I MPROVING BACKTRACKING SEARCH

General-purpose ideas give huge gains in speed

• Backtracking is uninformed; these ideas play the role that heuristics played in search

Ordering:

• Which variable should be assigned next?

• In what order should its values be tried?

Filtering: Can we detect inevitable failure early?

# I MPROVING BACKTRACKING SEARCH

General-purpose ideas give huge gains in speed

• Backtracking is uninformed; these ideas play the role that heuristics played in search

Ordering:

• Which variable should be assigned next?

• In what order should its values be tried?

Filtering: Can we detect inevitable failure early?

Structure: Can we exploit the problem structure?

# ORDERING

# ORDERING: MINIMUM REMAINING VALUE

# ORDERING: MINIMUM REMAINING VALUE

Variable Ordering: Minimum remaining values (MRV):

• Choose the variable with the fewest legal values left in its domain

# ORDERING: MINIMUM REMAINING VALUE

Variable Ordering: Minimum remaining values (MRV):

• Choose the variable with the fewest legal values left in its domain

• After WA = red and Q = green, SA has one legal value left: assign SA next

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fc97b3b8f19314fcf9f977489bf9586c6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089982&Signature=4BEpOqB%2FaWK9bCO0wqoC4CqH%2Frg%3D)

NSW

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fda61e557166d4b9fbcd31ac7f41de3d7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089982&Signature=9MgEwMtSzb23Iyb9niUZh9dMOuM%3D)

# ORDERING: MINIMUM REMAINING VALUE

Variable Ordering: Minimum remaining values (MRV):

• Choose the variable with the fewest legal values left in its domain

• After WA = red and Q = green, SA has one legal value left: assign SA next

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fd7f29a76a1644e86bf8fb13b9d1ad83d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089982&Signature=7wrJFXazkCe%2B7XjZJ4U9JqVud18%3D)

NSW

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fbde013b9b5c3449988bc08b194cb6cd3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=oDoTf6h7BPKHIrO4a8nzfD83FSA%3D)

Why min rather than max?

# ORDERING: MINIMUM REMAINING VALUE

Variable Ordering: Minimum remaining values (MRV):

• Choose the variable with the fewest legal values left in its domain

• After WA = red and Q = green, SA has one legal value left: assign SA next

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F1f22ee8f91f64b3ca5ce81c7e6930350.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=e41zyhs6qWAhkeTpcKdGoqrxt5A%3D)

NSW

SA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F73257f28c9444cd7b96a8272b5b6eaec.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=ZvP75%2Fq1GXlSLL9HiiWAIRyN5ps%3D)

Why min rather than max?

Also called "most constrained variable"

# ORDERING: MINIMUM REMAINING VALUE

Variable Ordering: Minimum remaining values (MRV):

• Choose the variable with the fewest legal values left in its domain

• After WA = red and Q = green, SA has one legal value left: assign SA next

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F67f7412be7824c1aa79701a03d99b871.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=BXFpr8DfkchgxPII%2BeW7Aydj06M%3D)

NSW

SA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fbfef91aa2b0441e0900b8af017c4d2ac.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=CZm86OilL3OKidU9Bp5j0sJcT9E%3D)

Why min rather than max?

Also called "most constrained variable"

"Fail-fast" ordering

# ORDERING: LEAST CONSTRAINING VALUE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Ff3ef966e81174a2d96cae10b3a9d61ea.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=5%2BWGER%2BMXCg4JFB6HkMF4l3H0bM%3D)

# ORDERING: LEAST CONSTRAINING VALUE

Value Ordering: Least Constraining Value

• Given a choice of variable, choose the least constraining value

i.e., the one that rules out the fewest values in the remaining variables

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F3a7b00b29b41493990407142d7961396.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=08xwfse20fXoMRhBAHY32F%2B077E%3D)

# ORDERING: LEAST CONSTRAINING VALUE

Value Ordering: Least Constraining Value

• Given a choice of variable, choose the least constraining value

i.e., the one that rules out the fewest values in the remaining variables

Why least rather than most?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F671752464aa34da2a442980dc482d14b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=4%2Bv9oKDDmfbF4ocQxgZYRikEyn0%3D)

# ORDERING: LEAST CONSTRAINING VALUE

Value Ordering: Least Constraining Value

• Given a choice of variable, choose the least constraining value

i.e., the one that rules out the fewest values in the remaining variables

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F19bbf96fc60f43b299a0261703501ddb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089983&Signature=Y393AP%2FYG4JNe68PInvKARdmuYk%3D)

Why least rather than most?

Combining these ordering ideas makes 1000 queens feasible

# FILTERING

# FILTERING: FORWARD CHECKING

# FILTERING: FORWARD CHECKING

Filtering: Keep track of domains for unassigned variables and cross off bad options.

WA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fd23642fb24ab402fb920e4cd27528d75.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=u5RXiAXStG4WxQeFHNvyMHRlAlA%3D)

NSW

SA

# FILTERING: FORWARD CHECKING

Filtering: Keep track of domains for unassigned variables and cross off bad options.

Forward checking: Cross off values that violate a constraint when added to the existing assignment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fa5e9f511a91542c9a2695d73ec5a4101.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=GTs0gXWEwIuB2YQpasY7yt0%2B%2Fj4%3D)

# FILTERING: FORWARD CHECKING

Filtering: Keep track of domains for unassigned variables and cross off bad options.

Forward checking: Cross off values that violate a constraint when added to the existing assignment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F4344d2d39a394e28b0a74a63219a827f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=djcX8o1sIi1Zw3Sr6VQqVrQ%2BAUw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fa3a13ec5946c45319eb7d580209febc2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=G0D0dAqYlnzYEt1SBW%2F7u8X5BJg%3D)

# FILTERING: FORWARD CHECKING

Filtering: Keep track of domains for unassigned variables and cross off bad options.

Forward checking: Cross off values that violate a constraint when added to the existing assignment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fbe9f5b8b7fe746bcbea920dac55ae28e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=k42EWp66nYM0FWBzRXWA2nfqq8k%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F938b0b4a0fd64d278b7792d42d945542.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=kSe%2FrsSZw6jfMmqvb6IyrGQJkyo%3D)

# FILTERING: CONSTRAINT PROPAGATION

Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F28cb6f9efb324dd0ab016aa1b314784c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=s2WeLe4V0LHiU88iMxhO5agSmTU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fe4f06e182e564683a0288cae5246d9fa.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=dsbkMho2UpDimZcFsq3IP%2FcyvqE%3D)

# FILTERING: CONSTRAINT PROPAGATION

Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F4b32a508cf5941eb9777b3f308babd6a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=qnp8xILH%2FO6rY9j6cbOuP%2BwnY64%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Ff615dcc562d446b6b21a052bb24ce63f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089984&Signature=raRVFdqbQrMZ1%2F97GxkJLlnQxH4%3D)

NT and SA cannot both be blue!

# FILTERING: CONSTRAINT PROPAGATION

Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fd0f3a9740aeb410685f57272a26e984c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089985&Signature=49INz4cLVsZQLEs9FQvvxNVUVIo%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Febd84a0a20fc40ff949fddd3c3bdcc1b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089985&Signature=TShIMEkCDhY37k%2BthurEJLhr650%3D)

NT and SA cannot both be blue!

Why didn't we detect this yet?

# FILTERING: CONSTRAINT PROPAGATION

Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F26941be3032c44b2aca1650cf6f98999.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089985&Signature=sDNZhLzymJVT5xve5z2Y2ksg730%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F80a9e09142d343e4a9afcfc96498944c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089985&Signature=02ONJVJBi%2BGcrCkNLndnDkNiEbc%3D)

NT and SA cannot both be blue!

Why didn’t we detect this yet?

Constraint propagation: reason from constraint to constraint

# CONSISTENCY OF A SINGLE ARC

An arc X → Y is consistent iff for every x in the tail there is some y in the head which could be assigned without violating a constraint.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fcba5a52b0e064d70b7653bdc11c8d887.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089985&Signature=ZVPn54LhvmFsdvbXWMNEe9GGmZ4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F498fbea8264c48b283772f480672d437.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089985&Signature=Uc1QyQgQEBRgkd7n4RkxU%2ByzWjA%3D)

# CONSISTENCY OF A SINGLE ARC

An arc X → Y is consistent iff for every x in the tail there is some y in the head which could be assigned without violating a constraint.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fdd172bcdf05741da9662e7651c5a8e2d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089985&Signature=HEmVQILREZMDi53As3Z8wXHHeFs%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F8314da52f4db4979a9f85def594abed7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089985&Signature=UyJ0foHpD9IXsDEVNH6gsFizvv8%3D)

Forward checking: Enforcing consistency of arcs pointing to each new assignment.

Delete from the tail !!

# ARC CONSISTENCY OF AN ENTIRE CSP

A simple form of propagation makes sure all arcs are consistent:

$$ V\rightarrow N S W $$

$$ S A\rightarrow N S W $$

$$ N S W\rightarrow S A $$

$$ V\rightarrow N S W $$

$$ S A\rightarrow N T $$

# ARC CONSISTENCY OF AN ENTIRE CSP

A simple form of propagation makes sure all arcs are consistent:

$$ V\rightarrow N S W $$

$$ S A\rightarrow N S W $$

$$ N S W\rightarrow S A $$

$$ V\rightarrow N S W $$

$$ S A\rightarrow N T $$

Important: If X loses a value, neighbors of X need to be recheck.

Arc consistency detects failure earlier than forward checking

Can be run as a preprocessor or after each assignment

What is the downside of enforcing arc consistency?

# ENFORCING ARC CONSISTENCY IN A CSP: AC

function AC-3(csp) returns the CSP, possibly with reduced domains inputs: csp, a binary CSP with variables \{X_{1}, X_{2}, \ldots, X_{n}\} local variables: queue, a queue of arcs, initially all the arcs in csp while queue is not empty do

$ (X_{i}, X_{j}) \leftarrow \text{REMOVE-FIRST}(queue) $

if REMOVE-INCONSISTENT-VALUES( $ X_{i} $,  $ X_{j} $) then

for each  $ X_{k} $ in NEIGHBORS[ $ X_{i} $] do

add ( $ X_{k} $,  $ X_{i} $) to queue

function REMOVE-INCONSISTENT-VALUES(X_{i}, X_{j}) returns true iff succeeds

removed←false

for each x in DOMAIN[X_{i}] do

if no value y in DOMAIN[X_{j}] allows (x,y) to satisfy the constraint X_{i} \leftrightarrow X_{j}

then delete x from DOMAIN[X_{i}]; removed←true

return removed

Runtime:  $ \mathcal{O}(n^{2}d^{3}) $, can be reduced to  $ \mathcal{O}(n^{2}d^{2}) $

But detecting all possible future problems is NP-hard.

# LIMITATIONS OF ARC CONSISTENCY

After enforcing arc consistency:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F1d5f2e0a8c3d4fefb12fea7476b59403.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=qw8hhpmV7NShwKj%2BwZIgkeC0WzE%3D)

Top: arc consistent, solutions exist. Bottom: arc consistent, no solution.

# LIMITATIONS OF ARC CONSISTENCY

After enforcing arc consistency:

• Can have one solution left

• Can have multiple solutions left

• Can have no solutions left (and not know it)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F6f3c3ca2797e41198fd1ba6d4a4e5c98.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=vru8%2BWexymXt5eM5OIZwByLMq%2Bw%3D)

Top: arc consistent, solutions exist. Bottom: arc consistent, no solution.

# LIMITATIONS OF ARC CONSISTENCY

After enforcing arc consistency:

• Can have one solution left

• Can have multiple solutions left

• Can have no solutions left (and not know it)

Arc consistency still runs inside a backtracking search.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fe2065400b8034163a87881b23fb40bdb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=DjFumTLCHQ%2BdhcQ2gTuZFWAXBRM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fd019c9b9397c4b3ebffe1027d260116d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=U9YU9BEScoZaQKfAs9fo2UCWV80%3D)

Top: arc consistent, solutions exist. Bottom: arc consistent, no solution.

# PROBLEM STRUCTURE

# PROBLEM STRUCTURE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F92fc621a1f9547b0b2f5e06cf927375b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=BEDogJQGABGeB4HilHTWBEfAj98%3D)

# PROBLEM STRUCTURE

Real world problem can be decomposed into many subproblems.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F88bb14551ce545a2902ce55d61e363bd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=A%2Bq%2FXzA2NDCvV5ZR52pjf4fH%2Fas%3D)

# PROBLEM STRUCTURE

Real world problem can be decomposed into many subproblems.

Extreme case: independent subproblems

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F1dfe67fa643d452db098b0b6734e3701.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=Fq6U9h48ijeS7QDkE93CUytBOSI%3D)

# PROBLEM STRUCTURE

Real world problem can be decomposed into many subproblems.

Extreme case: independent subproblems

• Tasmania and mainland are independent subproblems

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F8e4cdf97837f402c840fa393fefac151.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=NqZo7%2B%2BQHHVGdurLJErvRKUSeMg%3D)

# PROBLEM STRUCTURE

Real world problem can be decomposed into many subproblems.

Extreme case: independent subproblems

• Tasmania and mainland are independent subproblems

Independent subproblems are identifiable as connected components of constraint graph

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Ff0974f9cdbcd46c99e48927c12974027.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=%2FGGBuJCFqflOu39my6JZBR7eYPI%3D)

# PROBLEM STRUCTURE

Real world problem can be decomposed into many subproblems.

Extreme case: independent subproblems

• Tasmania and mainland are independent subproblems

Independent subproblems are identifiable as connected components of constraint graph

Suppose a graph of n variables can be broken into subproblems of only c variables:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fd81b8b753ef249bab19508887f048232.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089986&Signature=wwV04SiWnyc6IzlQK%2FGpQnSjYmU%3D)

# PROBLEM STRUCTURE

Real world problem can be decomposed into many subproblems.

Extreme case: independent subproblems

• Tasmania and mainland are independent subproblems

Independent subproblems are identifiable as connected components of constraint graph

Suppose a graph of n variables can be broken into subproblems of only c variables:

• Worst-case solution cost is  $ \mathcal{O}((n/c)(d^{c})) $, linear in n

$$ \bullet \quad \mathsf{E.g.},n=80,d=2,c=20 $$

$ 2^{80} = 4 $ billion years at 10 million nodes/sec

(4) $ (2^{20}) = 0.4 $ seconds at 10 million nodes/sec

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Ff9c5e10a039746fcb08253ff80dfb8c7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=BZbsVofSN1pN4pdy9kVErJvtN%2BE%3D)

# PROBLEM STRUCTURE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F22ed4ab7a69b4dd8be7de48d4bb353ca.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=frES3TaloCOUXAD6%2BZfjP6JW%2F5s%3D)

Theorem: if the constraint graph has no loops, the CSP can be solved in  $ \mathcal{O}(nd^{2}) $ time

• Compare to general CSPs, where worst-case time is  $ \mathcal{O}(d^{m}) $

This property also applies to probabilistic reasoning (later): an example of the relation between syntactic restrictions and the complexity of reasoning.

# PROBLEM STRUCTURE

Algorithm for tree-structured CSPs:

Order: Choose a root variable, order variables so that parents precede children

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fa12c1815d5f5480c9e125f7ee75a9977.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=TtXDOkj8ViikGuMBIWnHcOq9Ob0%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fae246e95224d4f9e9d3e2f47c73d3dea.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=iruxsfjoolcnV6jSNa1E%2F2IZXAg%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fc403056fdd254de09506437532e68331.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=SOdtaoD1o0%2F8%2Fkkr%2FuZYdaPc19s%3D)

- Remove backward: For  $ i = n $ down to 2, apply RemoveInconsistent(Parent( $ X_{i} $), $ X_{i} $)

• Assign forward: For i = 1 to n, assign  $ X_i $ consistently with Parent( $ X_i $)

# PROBLEM STRUCTURE

Algorithm for tree-structured CSPs:

• Order: Choose a root variable, order variables so that parents precede children

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F6027447f1abd4bd7bed7b4d083c7d67e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=u5J1l5bD%2FMQzaIc%2BBN2FKk3XsGo%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F8267c84fa10944ea9f10bee37fdcb49e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=3yh%2B6f7pvAEV%2F6H0pgZ2c6vIwrM%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F5aa66f317ac643a29ba4e11911ec3ccb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=2I%2BiWp5hRXdHPDDRsMqFc9F5g0I%3D)

- Remove backward: For i = n down to 2, apply RemoveInconsistent(Parent(X_i), X_i)

• Assign forward: For i = 1 to n, assign  $ X_{i} $ consistently with Parent( $ X_{i} $)

Runtime:  $ \mathcal{O}(nd^{2}) $

# PROBLEM STRUCTURE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2F035feb31f18e4bdc9ae99221c7b6d27e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089987&Signature=sxe13Jp1d%2BFiXpSk8FOFBIlQtm0%3D)

Conditioning: instantiate a variable, prune its neighbors' domains

Cutset conditioning: instantiate (in all ways) a set of variables such that the remaining constraint graph is a tree

Cutset size c gives runtime  $ \mathcal{O}((d^{c})(n - c)d^{2}) $, very fast for small c.

# Q & A

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Ff6f94b78b17640dfa9b7399d6c430e83%2Fmedia%2Fdbb4a30d8d40467cbcce545e6ac2e065.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089988&Signature=Qsv0BNhjx%2BizyfCvZICFxG1dk08%3D)
