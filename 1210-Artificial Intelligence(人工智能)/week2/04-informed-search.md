# Informed Search

**CS5491: Artificial Intelligence**
**Zhichao Lu**

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

Part 2: the same tree-search loop, now with a hint about where the goal is.

---

## Today (Part 2)

- Informed Search Methods
- Heuristics
- Greedy Search
- A* Search

Reading: RN Chapter 3.5-3.6

---

## Search Problems

### Uninformed Search
- Methods we saw: DFS, BFS, UCS
- Searching with your **EYES CLOSED**

### Informed Search
- Methods we will see: Greedy, A*
- Searching with your **EYES OPEN**

---

## Example: Pancake Problem

States: orderings of the stack
Action: flip the top k pancakes
Cost: k, the number flipped

![Pancake State Space](images/04-informed-search/pancakes-state-space.png)

- Gates and Papadimitriou, 1979: Bill Gates's one research paper
- The picture is the whole state space for four pancakes
- How many states for n pancakes? (n factorial: 24 here, about 3.6 million for 10)

---

## Heuristics

### Search Heuristics

- A heuristic is:
  - A function that estimates how close a state is to a goal
  - Designed for a particular search problem
  - Examples: Manhattan distance, Euclidean distance

![Pacman Distance](images/04-informed-search/pacman-distance.png)

- A heuristic h(state) estimates the cost to the nearest goal
- Cheap to compute, designed for the problem at hand
- It is a hint, not the truth

### Example: Heuristic Function

![Romania Heuristic](images/04-informed-search/romania-heuristic.png)

- Straight-line distance to Bucharest
- Arad 366, Sibiu 253, Fagaras 178, Rimnicu Vilcea 193, Pitesti 98
- It is never more than the road distance → admissibility

### Example: Pancake Heuristic

![Pancake Heuristic](images/04-informed-search/pancake-heuristic.png)

- h(x) = the number of the largest pancake still out of place
- Sorted stack: 0. Largest pancake on top: 4
- Why sensible: any flip that moves pancake k costs at least k

---

## Greedy Search

- **Strategy**: expand a node that you think is closest to a goal state
- **Heuristic**: distance estimate to nearest goal for each state

### Greedy Search: Romania

![Greedy Romania 1](images/04-informed-search/greedy-romania-01.svg)

![Greedy Romania 2](images/04-informed-search/greedy-romania-02.svg)

![Greedy Romania 3](images/04-informed-search/greedy-romania-03.svg)

![Greedy Romania 4](images/04-informed-search/greedy-romania-04.svg)

![Romania Distances](images/04-informed-search/romania-distances.png)

- Expand the fringe node with the smallest h
- Arad → Sibiu (253) → Fagaras (178) → Bucharest (0)
- This route is 450 km. Via Rimnicu Vilcea and Pitesti it is 418
- Greedy never looked at a road length

### Greedy Properties

- A common case: best-first takes you straight to the (wrong) goal
- Worst-case: like a badly-guided DFS
- Never optimal (ignores path cost)

---

## A* Search

### Key Idea: Combine UCS and Greedy

- **Uniform-cost** orders by path cost: g(n) (backward cost)
- **Greedy** orders by goal proximity: h(n) (forward cost)
- **A* Search** orders by the sum: **f(n) = g(n) + h(n)**

### Combining UCS and Greedy

![A* Example 1](images/04-informed-search/0025-01.svg)
![A* Example 2](images/04-informed-search/0025-02.svg)
![A* Example 3](images/04-informed-search/0025-03.svg)
![A* Example 4](images/04-informed-search/0025-04.svg)

![A* Tree](images/04-informed-search/0026.svg)

- g is what you have paid, h is your guess of what remains
- f(n) = estimated total cost of the best plan that goes through n

### When should A* terminate?

![A* Termination](images/04-informed-search/0027.svg)

- **No**: only stop when we dequeue a goal (not when we enqueue)
- Rule: stop when a goal is dequeued, exactly as in UCS

### Is A* optimal?

![A* Optimality Counter-example](images/04-informed-search/0028.svg)

- What went wrong? h(A) claims 6 remain when only 2 do
- The estimate exceeded the truth, so the good plan was stuck behind a bad one
- We need estimates that never exceed the actual cost

---

## Admissibility

- **Inadmissible (pessimistic)** heuristics break optimality by trapping good plans on the fringe
- **Admissible (optimistic)** heuristics slow down bad plans but never outweigh true costs

### Admissible Heuristics

A heuristic h is **admissible (optimistic)** if:

$$0 \leq h(n) \leq h^*(n)$$

where h*(n) is the true cost to a nearest goal

![Admissible Examples](images/04-informed-search/pacman-distance.png)

- Manhattan distance for Pacman: walls can only make the real path longer
- Largest misplaced pancake: any flip that moves it costs at least that number
- In practice, finding a good admissible heuristic is most of the work of using A*

---

## Optimality of A* Tree Search

**Assume:**
- A is an optimal goal node
- B is a suboptimal goal node
- h is admissible

**Claim:** A will exit the fringe before B

**Proof:**

1. f(n) = g(n) + h(n) ≤ g(A) (admissibility of h)
2. g(A) = f(A) (h=0 at goal)
3. g(A) < g(B) (B is suboptimal)
4. f(A) < f(B) (h=0 at goal)
5. ∴ f(n) ≤ f(A) < f(B)
6. n expands before B
7. All ancestors of A expand before B
8. **A* search is optimal** ✓

---

## UCS vs A* Contours

![UCS vs A* Contours](images/04-informed-search/contours-ucs-astar.svg)

- **Uniform-cost**: expands equally in all "directions" (circles of equal g)
- **A***: expands mainly toward the goal, but hedges to ensure optimality (contours of equal f)
- A better heuristic makes the contours thinner
- A perfect one would be a straight line to the goal

---

## Creating Admissible Heuristics

Most of the work in solving hard search problems optimally is in coming up with admissible heuristics

**Recipe**: relax the problem by adding actions, solve the relaxed problem exactly, and use that cost

- Straight-line distance = allow flying
- Manhattan distance = allow walking through walls
- A relaxed problem can only be cheaper, so the heuristic is admissible for free

Inadmissible heuristics can often be useful too (faster, with solutions slightly worse than optimal)

---

## A* Summary

- A* uses both backward costs and (estimates of) forward costs
- A* is optimal with admissible heuristics
- Heuristic design is key: often use relaxed problems

---

## Designing Heuristic as a Search Problem

![Nature Cover](images/04-informed-search/nature_coverpage.png)

**FunSearch** (DeepMind, Nature, December 2023):
- A language model proposes small programs
- An evaluator scores each on benchmark instances
- The best are kept and mutated
- Evolutionary search over the space of programs

### Online Bin Packing

![Online Packing](images/04-informed-search/online_packing.png)

- Items arrive one at a time and must be placed immediately into a fixed-size bin
- Minimise the number of bins used
- The decision rule is a heuristic that scores every open bin

![FunSearch Illustration](images/04-informed-search/funsearch_illustration.webp)

### Discovered Heuristic

![Best Fit](images/04-informed-search/best_fit_heur.png)

![FunSearch Heuristic](images/04-informed-search/funsearch_heur.png)

- Left: best fit (textbook rule) - put the item where it leaves the least space
- Right: discovered heuristic - penalises bins that would be left with a small useless gap
- The output is code you can read and check, not a black box

---

## Summary Table

| Algorithm | Uses h(n)? | Uses g(n)? | Complete? | Optimal? |
|-----------|-----------|-----------|-----------|----------|
| UCS | No | Yes | Yes | Yes |
| Greedy | Yes | No | No* | No |
| A* | Yes | Yes | Yes** | Yes*** |

\* Can loop without cycle detection
\** With finite branching factor and positive arc costs
\*** With admissible heuristic

---

## Key Formulas

- **Heuristic**: h(n) = estimated cost from n to goal
- **Path cost**: g(n) = actual cost from start to n
- **Evaluation function**: f(n) = g(n) + h(n)
- **Admissibility**: 0 ≤ h(n) ≤ h*(n)

---

Source: https://www.cs.cityu.edu.hk/~zhichalu/teaching/SS25-CS5491-AI/slides/04-informed-search/index.html
