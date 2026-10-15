Informed Search
CS5491: Artificial Intelligence
Zhichao Lu
Content Credits:
Prof. Wei
's CS4486 Course
and
Prof. Boddeti
's AI Course

## Today (Part 2)

- Informed Search Methods
  - Heuristics
  - Greedy Search
  - $A^*$ Search
- Reading
  - Today's Lecture: RN Chapter 3.5-3.6
  - Next Lecture: RN Chapter 6

## Search Problems

Uninformed Search
- Methods we saw:
  - DFS
  - BFS
  - UCS
- Searching with your EYES CLOSED
Informed Search
- Methods we will see:
  - Greedy
  - $A^*$
- Searching with your EYES OPEN

Example: Pancake Problem
States: orderings of the stack · Action: flip the top
k
pancakes · Cost:
k
, the number flipped

## Heuristics

## Search Heuristics

- A heuristic is:
  - A function that estimates how close a state is to a goal
  - Designed for a particular search problem
  - Examples: Manhattan distance, Euclidean distance

Example: Heuristic Function

Example: Heuristic Function
- Eg: index of the largest pancake that is still out of place

## Greedy Search

## Greedy Search: Romania

- Expand the node that seems closest...
- What can go wrong?

## Greedy Search

- Strategy: expand a node that you think is closest to a goal state
  - Heuristic: distance estimate to nearest goal for each state
- A common case:
  - Best-first takes you straight to the (wrong) goal
- Worst-case: like a badly-guided DFS

## Greedy Demo

## $A^*$ Search

## Key Idea: Combine UCS and Greedy
## $A^*$ Search

## Combining UCS and Greedy

- Uniform-cost
orders by path cost, or backward cost $g(n)$.
- Greedy
orders by goal proximity, or forward cost $h(n)$.
- $A^*$ Search
orders by the sum: $f(n) = g(n) + h(n)$

## When should $A^*$ terminate?

- Should we stop when we enqueue a goal?
- No: only stop when we dequeue a goal

## Is $A^*$ optimal?

- What went wrong?
- Actual goal cost $\leq$ estimated goal cost
- We need estimates to be less than actual costs

## Admissibility

- Inadmissible (pessimistic) heuristics break optimality by trapping good plans on the fringe.
- Admissible (optimistic) heuristics slow down bad plans but never outweigh true costs

## Admissible Heuristics

- A heuristic $h$ is admissible (optimistic) if:
$$0 \leq h(n) \leq h^*(n)$$
- where $h^*(n)$ is the true cost to a nearest goal
- Example:
- In practice, coming up with an admissible heuristic is most of what is involved in using $A^*$.

## Optimality of $A^*$ Tree Search

- Assume:
  - A is an optimal goal node
  - B is a suboptimal goal node
  - h is admissible
- Claim:
  - A will exit the fringe before B

## Optimality of $A^*$ Tree Search

Proof:
- Imagine $B$ is on the fringe
- Some ancestor $n$ of $A$ is on the fringe too
- Claim: $n$ will be expanded before $B$
  - $f(n)$ is less or equal to $f(A)$
  - $f(A)$ is less than $f(B)$
  - $n$ expands before $B$
- All ancestors of $A$ expand before $B$
- A expands before B
- $A^*$ search is optimal
- \[
\begin{aligned}
f(n) &= g(n) + h(n) \nonumber \\
f(n) &\leq g(A)~{\rm{~admissibility~of~}} h \nonumber \\
g(A) &= f(A) ~~ h=0~{\rm{~~at~goal}} \nonumber
\end{aligned}
\]
- \[
\begin{aligned}
g(A) &< g(B) ~~ B {\rm{~is~suboptimal}} \nonumber \\
f(A) &< f(B) ~~ h=0 {\rm{~at~goal}} \nonumber
\end{aligned}
\]
- \[
\begin{aligned}
f(n) \leq f(A) < f(B) \nonumber
\end{aligned}
\]

## UCS vs $A^*$ Contours

- Uniform-cost expands equally in all "directions"
- $A^*$ expands mainly toward the goal, but does hedge its bets to ensure optimality

## $A^*$ Demo

## $A^*$ Applications

- Video games
- Pathing / routing problems
- Resource planning problems
- Robot motion planning
- Language analysis
- Machine translation
- Speech recognition
- ...

## Creating Admissible Heuristics

- Most of the work in solving hard search problems optimally is in coming up with admissible heuristics
- Often, admissible heuristics are solutions to relaxed problems, where new actions are available
- Inadmissible heuristics can often be useful too.

## $A^*$ Summary

- $A^*$ uses both backward costs and (estimates of) forward costs
- $A^*$ is optimal with admissible heuristics
- Heuristic design is key: often use relaxed problems

## Designing Heuristic as a Search Problem

##### Online Bin Packing
## Designing Heuristic as a Search Problem

##### Online Bin Packing
## Designing Heuristic as a Search Problem

##### Online Bin Packing
## Designing Heuristic as a Search Problem

##### Online Bin Packing
## Designing Heuristic as a Search Problem

Q & A
