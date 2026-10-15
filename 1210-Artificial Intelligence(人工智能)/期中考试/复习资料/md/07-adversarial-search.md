Adversarial Search
CS5491: Artificial Intelligence
Zhichao Lu
Content Credits:
Prof. Wei
's CS4486 Course
and
Prof. Boddeti
's AI Course

## Today

- Part 1: Deterministic Games
  - Adversarial games, minimax search
  - $\alpha$-$\beta$ pruning, depth-limited search
- Part 2: Games with Chance
  - Expectimax, utilities
- Reading
  - Today's Lecture: RN Chapter 5.1-5.3, 5.5, 16.1-16.3
  - Next Lecture (Oct 8): Linear and Integer Programming

## Agents Interacting with Agents

Other agents act in the same world, with goals of their own: some cooperate, some compete. Games are the fully specified version of this.

## Game Playing State-of-the-Art

- Checkers:
1950: first computer player. 1994: Chinook ends the 40-year reign of
          human champion Marion Tinsley, using a complete 8-piece endgame database. 2007: checkers solved: perfect play is a draw.
- Chess:
1997: Deep Blue defeats world
          champion Garry Kasparov in a six-game match: 200M positions per second, deep $\alpha$-$\beta$ search, a hand-tuned evaluation.
          Today's engines (Stockfish, Leela) add neural-network evaluation and are far beyond any human.
- Go:
$b > 300$: brute-force search fails,
          and no hand-written evaluation works. 2016: AlphaGo defeats Lee Sedol with Monte Carlo tree search plus learned policy and value
          networks. 2017: AlphaGo Zero and AlphaZero learn Go, chess and shogi from self-play alone.
- Imperfect information:
2017 and 2019:
          Libratus and Pluribus beat top professionals at no-limit poker. 2022: Cicero plays Diplomacy at human level, negotiating with a
          language model.

## Adversarial Games

## Types of Games

- Many different kinds of games.
- Axes:
  - Deterministic or stochastic?
  - One, two, or more players?
  - Zero sum?
  - Perfect information (can you see the state)?
- Want algorithms for calculating a strategy (policy)
which recommends a move from each state.

## Deterministic Games

- Many possible formalizations, one is:
  - States $S$ (start at $s_0$)
  - Players $P=\{1, \dots, N\}$ (usually take turns)
  - Actions $A$ (may depend on player / state)
  - Transition Function $S \times A \rightarrow S$
  - Terminal Test $S \rightarrow \{t,f\}$
  - Terminal Utilities $S \times P \rightarrow R$
- Solution for a player is a policy: $S \rightarrow A$

## Game Theory

- Zero-Sum Games
  - Agents have opposite utilities (values on outcomes)
  - Lets us think of a single value that one maximizes
and the other minimizes
  - Adversarial, pure competition
- General Games
  - Agents have independent utilities (values on outcomes)
  - Cooperation, indifference, competition, and more are all possible

## Adversarial Search

Single-Agent Trees
- Value of State:
The best achievable outcome (utility) from that state
- Terminal States:
$V(s)$ known
- Non-Terminal States:
$V(s) = \max_{s' \in children(s)} V(s')$

Adversarial Game Trees

Minimax Values
- States Under Agent’s Control:
$V(s) = \max_{s' \in successors(s)} V(s')$
- States Under Opponent's Control:
$V(s) = \min_{s' \in successors(s)} V(s')$
- Terminal States: $V(s)$ known

Tic-Tac-Toe

## Adversarial Search (Minimax)

- Deterministic, zero-sum games:
  - Tic-tac-toe, chess, checkers
  - One player maximizes result
  - The other minimizes result
- Minimax Search:
  - A state-space search tree
  - Players alternate turns
  - Compute each node’s
minimax value
:
                the best achievable utility against a rational (optimal) adversary

## Minimax Implementation

## Minimax Implementation (Dispatch)

## Minimax Example

## Minimax Properties

Optimal against a perfect player. Otherwise?
Minimax value 10, move left. The 100 on the right is bait: it needs the opponent to blunder, and the price of guessing wrong is 9.

## Minimax Efficiency

- How efficient is minimax?
  - Just like (exhaustive) DFS
  - Time: $\mathcal{O}(b^m)$
  - Space: $\mathcal{O}(bm)$
- Example: For chess, $b \approx 35$, $m \approx 100$
  - Exact solution is completely infeasible
  - But, do we need to explore the whole tree?

## Game Tree Pruning

## Minimax Pruning

## $\alpha$-$\beta$ Pruning: the Idea

- While searching, carry two numbers for the current path from the root:
  - $\alpha$
: the best value MAX is already guaranteed at a choice point above: a
floor
  - $\beta$
: the best value MIN is already guaranteed above: a
ceiling
- Only values strictly between $\alpha$ and $\beta$ can still change the decision at the root
- At a MIN node $n$, $v$ only goes down. Once $v \le \alpha$, MAX above will never choose $n$: stop expanding $n$
- At a MAX node, $v$ only goes up. Once $v \ge \beta$, MIN above will never allow it: stop

## $\alpha$-$\beta$ Implementation

- Pass down: the root calls max-value(state, $-\infty$, $+\infty$): no floor, no ceiling yet; every recursive call hands its current $(\alpha, \beta)$ to its children
- Test, then update: MAX: after each child, if $v \ge \beta$ return $v$ (MIN above will not allow it), else $\alpha \leftarrow \max(\alpha, v)$.
MIN: if $v \le \alpha$ return $v$, else $\beta \leftarrow \min(\beta, v)$

## $\alpha$-$\beta$ on the Example

| Call $(\alpha, \beta)$ received Children seen Returns
| root, MAX $(-\infty, +\infty)$
| left MIN $(-\infty, +\infty)$ 3, 12, 8: $v = 3$, never $\le \alpha$ 3; root sets $\alpha = 3$
| middle MIN $(3, +\infty)$ 2: $v = 2 \le \alpha$ 2 at once: the other two children are never generated
| right MIN $(3, +\infty)$ 14, 5, 2: $v$ stays above 3 until the last child 2; nothing to prune
| root $\max(3, 2, 2)$ 3: move left
Had the middle leaves come as 6, 4, 2, all three would have been seen: pruning depends on the order.

## $\alpha$-$\beta$ Pruning Properties

- This pruning has no effect
on minimax value computed for the root.
- Values of intermediate nodes might be wrong
  - Important: children of the root may have the wrong value
  - So the most naïve version won’t let you do action selection
- Good child ordering improves effectiveness of pruning
- With "perfect ordering":
  - Time complexity drops to $\mathcal{O}(b^{\frac{m}{2}})$
  - Doubles solvable depth
  - Full search of, e.g. chess, is still hopeless $\dots$
- This is a simple example of metareasoning
(computing about what to compute)

## Constrained Resources

- Problem: In realistic games, cannot search to leaves.
- Solution: Depth-limited search
  - Instead, search only to a limited depth in the tree
  - Replace terminal utilities with an evaluation function
for non-terminal positions
- Example:
  - Suppose we have 100 seconds, can explore 10K nodes / sec
  - So can check 1M nodes per move
  - $\alpha$-$\beta$ reaches about depth 8 – decent chess program
- Guarantee of optimal play is gone
- More depth makes a BIG difference
- Use iterative deepening for an anytime algorithm

## Summary: Adversarial Search

|
Minimax $\alpha$-$\beta$ pruning Depth-limited + evaluation
|
Answer Exact minimax value and move Same value, same move Approximate; as good as the evaluation function
|
Optimal against a perfect opponent? Yes Yes No guarantee
|
Time $\mathcal{O}(b^m)$ $\mathcal{O}(b^{m/2})$ with perfect move ordering $\mathcal{O}(b^d)$, choose $d$ to fit the clock
|
Space $\mathcal{O}(bm)$ $\mathcal{O}(bm)$ $\mathcal{O}(bd)$
|
What you give up Feasible only for tiny games Nothing; the gain depends on move ordering Optimality; horizon effects
- Chess: $b \approx 35$, $m \approx 100$. A million nodes per move buys depth 8 with $\alpha$-$\beta$; iterative deepening makes it anytime.

Q & A
