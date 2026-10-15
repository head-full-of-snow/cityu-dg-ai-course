Adversarial Search - II
CS5491: Artificial Intelligence
Zhichao Lu
Content Credits:
Prof. Wei
's CS4486 Course
and
Prof. Boddeti
's AI Course

## Today

- Part 2: Games with Chance
  - Expectimax search
  - Modeling the opponent
  - Utilities
- Reading
  - Today's Lecture: RN Chapter 5.5, 16.1-16.3
  - Next Lecture (Oct 8): Linear and Integer Programming
Chance nodes replace the adversary

## Uncertain Outcomes

## Worst Case vs Average Case

- Idea:
Uncertain outcomes controlled by chance, not an adversary.

## Stochastic Games

- Why would we not know what the result of an action will be?
  - Explicit randomness: rolling dice
  - Unpredictable opponents: the ghosts respond randomly
  - Actions can fail: when moving a robot, wheels might slip
- Values should now reflect average-case (expectimax) outcomes, not worst-case (minimax) outcomes

## Expectimax Search

- Expectimax search: compute the average score under optimal play
  - Max nodes as in minimax search
  - Chance nodes are like min nodes but the outcome is uncertain
  - Calculate their expected utilities
  - i.e., take weighted average (expectation) of children
- Later, we will learn how to formalize the underlying uncertain-result problems as Markov Decision Processes

## Expectimax Implementation

$$ v = \tfrac{1}{2} \cdot 8 + \tfrac{1}{3} \cdot 24 + \tfrac{1}{6} \cdot (-12) = 10 $$

## Expectimax Example

Children of each chance node are equally likely

## Expectimax Pruning

- Left node is 8. The middle node's first child is 2: can we stop? No
: an unseen child could be arbitrarily large.
- Pruning needs bounds on the utilities: if all values lie in $[0, 10]$, the middle node is at most $(2 + 10 + 10)/3 \approx 7.3 < 8$, prune.

## Depth-Limited Expectimax

## Probabilities

## Primer: Probabilities

- A random variable
represents an event whose outcome is unknown.
- A probability distribution
is an assignment of weights to outcomes
- Example: Traffic on freeway
  - Random variable: $T$ = whether there is traffic
  - Outcomes: $T \in \{none, mild, heavy\}$
  - Distribution: $P(T=none) = 0.25$, $P(T=mild) = 0.50$, $P(T=heavy) = 0.25$

## Primer: Probabilities...

- Some laws of probability (more later):
  - Probabilities are always non-negative
  - Probabilities over all possible outcomes sum to one
- As we get more evidence, probabilities may change:
  - $P(T=heavy) = 0.25$, $P(T=heavy \mid Hour=8am) = 0.60$
  - We will talk about methods for reasoning and updating probabilities later

## Primer: Expectations

- The expected value of a function of a random variable is the average, weighted by the probability distribution over outcomes
- Example: How long to get to the airport?

## What probabilities to use?

- In expectimax search, we have a probabilistic model of how the opponent (or environment) will behave in any state
  - Model could be a simple uniform distribution (roll a die)
  - Model could be sophisticated and require a great deal of computation
  - We have a chance node for any outcome out of our control: opponent or environment
  - The model might say that adversarial actions are likely.
- For now, assume each chance node magically comes along with probabilities that specify the distribution over its outcomes

## Quiz: Informed Probabilities

- Let us say you know that your opponent is actually running a depth 2 minimax, using the result 80% of the time, and moving randomly otherwise.
- Question: What tree search should you use?
- Answer: Expectimax
  - To figure out EACH chance node’s probabilities, you have to run a simulation of your opponent
  - This kind of thing gets very slow very quickly
  - Even worse if you have to simulate your opponent simulating you
  - Except for minimax, which has the nice property that it all collapses into one game tree

## Modeling Assumptions

## The Dangers of Optimism and Pessimism

- Dangerous Optimism
  - Assuming chance when the world is adversarial
- Dangerous Pessimism
  - Assuming the worst case when it is not likely

## Assumptions vs Reality

- Pacman used depth 4 search with an eval function that avoids trouble
- Ghost used depth 2 search with an eval function that seeks Pacman
|
Adversarial Ghost
Random Ghost
|
Minimax Pacman
- Won 5/5
- Avg. Score: 483
|
- Won 5/5
- Avg. Score: 493
|
Expectimax Pacman
- Won 1/5
- Avg. Score: -303
|
- Won 5/5
- Avg. Score: 503

## Mixed Agent Games

- E.g. Backgammon
- Expectiminimax
  - Environment is an extra "random agent" player that moves after each min/max agent
  - Each node computes the appropriate combination of its children

## Mixed Agent Games: Backgammon

- Dice rolls increase b: 21 possible rolls with 2 dice
  - $\approx$ 20 legal moves
  - Four plies (two moves each): $20 \times (21 \times 20)^3 \approx 1.5 \times 10^9$
- As depth increases, probability of reaching a given search node shrinks
  - So usefulness of search is diminished
  - So limiting depth is less damaging
  - But pruning is trickier
- Historic AI: TD-Gammon (1992) uses depth-2 search + an evaluation function learned by reinforcement learning from self-play: world-class play
- The first program to reach that level by learning; a preview of the RL lectures

## Utilities

## Maximum Expected Utility

- Why should we average utilities? Why not minimax?
- Principle of maximum expected utility:
  - A rational agent should chose the action that maximizes its expected utility, given its knowledge
- Questions:
  - Where do utilities come from?
  - How do we know such utilities even exist?
  - How do we know that averaging even makes sense?
  - What if our behavior (preferences) cannot be described by utilities?

## What utilities to use?

- For worst-case minimax reasoning, terminal function scale does not matter
  - We just want better states to have higher evaluations (get the ordering right)
  - We call this insensitivity to monotonic transformations
.
- For average-case expectimax reasoning, we need magnitudes to be meaningful
  - Read the trees above with chance nodes: averages 20 vs 25 (go right) become 800 vs 650 after squaring (go left)

## Utilities

- Utilities are functions from outcomes (states of the world) to real numbers that describe an agent's preferences
- Where do utilities come from?
  - In a game, may be simple $(+1/-1)$
  - Utilities summarize the agent's goals
  - Theorem (von Neumann and Morgenstern, 1944): any "rational" preferences can be summarized as a utility function
- We hard-wire utilities and let behaviors emerge
  - Why don't we let agents pick utilities?
  - Why don't we prescribe behaviors?

Q & A
