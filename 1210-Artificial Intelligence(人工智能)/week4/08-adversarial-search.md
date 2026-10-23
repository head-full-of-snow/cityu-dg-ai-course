Prof. Wei

Prof. Boddeti

# TODAY

Part 2: Games with Chance

• Expectimax search

• Modeling the opponent

• Utilities

Reading

• Today's Lecture: RN Chapter 5.5, 16.1-16.3

• Next Lecture (Oct 8): Linear and Integer Programming

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2Fb9da36b0f78a4fa786a8bd5c42b19cd0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090062&Signature=wTfBZyeZCKWM6mjjZc9z%2F3nXcrc%3D)

Chance nodes replace the adversary

# UNCERTAIN OUTCOMES

# WORST CASE VS AVERAGE CASE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F9f947d14723e47fdb3744fddbd7ff559.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090062&Signature=fXRnxCI4ACYM2kYcX1fDQHmftAY%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F734bdf23e66d48ccb76c530f77032753.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090062&Signature=4AB1Nw0KYDAwFagGXqTmvYpG4FY%3D)

Idea: Uncertain outcomes controlled by chance, not an adversary.

# STOCHASTIC GAMES

Why would we not know what the result of an action will be?

• Explicit randomness: rolling dice

• Unpredictable opponents: the ghosts respond randomly

• Actions can fail: when moving a robot, wheels might slip

Values should now reflect average-case (expectimax) outcomes, not worst-case (minimax) outcomes

# EXPECTIMAX SEARCH

Expectimax search: compute the average score under optimal play

• Max nodes as in minimax search

• Chance nodes are like min nodes but the outcome is uncertain

• Calculate their expected utilities

• i.e., take weighted average (expectation) of children

Later, we will learn how to formalize the underlying uncertain-result problems as Markov Decision Processes

# EXPECTIMAX IMPLEMENTATION

# Dispatch:

# Function value(state)

# MAX Agent:

Function max-value(state)

v ← -∞;

for each successor of state do

v ← max(v, value(successor));

return v;

end

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F5b309bea882a4b6bb11d9e1234172cd7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090062&Signature=Iz6SceE29D%2F9TWZTZzvPsbthFo4%3D)

# EXP Agent:

$ v \leftarrow 0; $

for each successor of state do

p  $ \leftarrow $ probability(successor);

v  $ \leftarrow $ v + p  $ \times $ value(successor));

return v;

end

# EXPECTIMAX IMPLEMENTATION

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2Ffbdd335184654fd6a56336726fd20849.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090063&Signature=tkJWuKdho7IPeKLT2kc%2B7c15LdU%3D)

$$ v=\frac{1}{2}\cdot8+\frac{1}{3}\cdot24+\frac{1}{6}\cdot(-12)=10 $$

# EXPECTIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2Fee58a6a214f847efb3d74abcac32e7eb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090063&Signature=SCxjmybqNkVXYg%2BcYXj%2BJHKDTsw%3D)

Children of each chance node are equally likely

# EXPECTIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2Fc9f25630c97e4b2ca900cae98aad0041.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090063&Signature=kNMYGUqjClvstQA50JHpnK64ND0%3D)

Left node is 8. The middle node's first child is 2: can we stop? No: an unseen child could be arbitrarily large.

Pruning needs bounds on the utilities: if all values lie in [0, 10], the middle node is at most  $ (2 + 10 + 10)/3 \approx 7.3 < 8 $, prune.

# DEPTH-LIMITED EXPECTIMAX

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F28478ae8cc5e4f7e8243deed121687de.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090063&Signature=el5R0M%2F152qFdE653mbq1gi08B4%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F4bba173f1a7e48af9051f062893947f3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090063&Signature=iq6wD4Umb1Z7w1Xt3QtbRaVKLR0%3D)

# PROBABILITIES

# PRIMER: PROBABILITIES

A random variable represents an event whose outcome is unknown.

A probability distribution is an assignment of weights to outcomes

Example: Traffic on freeway

• Random variable: T = whether there is traffic

• Outcomes:  $ T \in \{none, mild, heavy\} $

• Distribution:  $ P(T = \text{none}) = 0.25 $,  $ P(T = \text{mild}) = 0.50 $,  $ P(T = \text{heavy}) = 0.25 $

# PRIMER: PROBABILITIES

Some laws of probability (more later):

• Probabilities are always non-negative

• Probabilities over all possible outcomes sum to one

As we get more evidence, probabilities may change:

•  $ P(T = heavy) = 0.25, P(T = heavy \mid Hour = 8am) = 0.60 $

• We will talk about methods for reasoning and updating probabilities later

# PRIMER: EXPECTATIONS

The expected value of a function of a random variable is the average, weighted by the probability distribution over outcomes

Example: How long to get to the airport?

<table><tr><td></td><td>None</td><td>mild</td><td>heavy</td></tr><tr><td>Time:</td><td>20</td><td>30</td><td>60</td></tr><tr><td>Probability:</td><td>0.25</td><td>0.50</td><td>0.25</td></tr></table>

<table><tr><td></td><td>None</td><td>mild</td><td>heavy</td></tr><tr><td>Time:</td><td>20</td><td>30</td><td>60</td></tr><tr><td></td><td>✗</td><td>✗</td><td>✗</td></tr><tr><td>Probability:</td><td>0.25</td><td>0.50</td><td>0.25</td></tr></table>

# WHAT PROBABILITIES TO USE?

In expectimax search, we have a probabilistic model of how the opponent (or environment) will behave in any state

• Model could be a simple uniform distribution (roll a die)

• Model could be sophisticated and require a great deal of computation

• We have a chance node for any outcome out of our control: opponent or environment

• The model might say that adversarial actions are likely.

For now, assume each chance node magically comes along with probabilities that specify the distribution over its outcomes

# QUIZ: INFORMED PROBABILITIES

Let us say you know that your opponent is actually running a depth 2 minimax, using the result 80% of the time, and moving randomly otherwise.

Question: What tree search should you use?

Answer: Expectimax

• To figure out EACH chance node's probabilities, you have to run a simulation of your opponent

• This kind of thing gets very slow very quickly

• Even worse if you have to simulate your opponent simulating you

• Except for minimax, which has the nice property that it all collapses into one game tree

# MODELING ASSUMPTIONS

# THE DANGERS OF OPTIMISM AND PESSIMISM

Dangerous Optimism

Dangerous Pessimism

• Assuming chance when the • Assuming the worst case world is adversarial when it is not likely

# ASSUMPTIONS VS REALITY

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F264d2e779a33471fab8457f6cde7c68b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090063&Signature=z6YUvEi%2F1Sgd66TJTbglkw7MioE%3D)

Pacman used depth 4 search with an eval function that avoids trouble

Ghost used depth 2 search with an eval function that seeks Pacman

Adversarial Ghost Random Ghost

<table><tr><td></td><td>Adversarial Ghost</td><td>Random Ghost</td></tr><tr><td>Minimax Pacman</td><td>Won 5/5</td><td>Won 5/5</td></tr><tr><td></td><td>Avg. Score: 483</td><td>Avg. Score: 493</td></tr><tr><td>Expectimax Pacman</td><td>Won 1/5</td><td>Won 5/5</td></tr><tr><td></td><td>Avg. Score: -303</td><td>Avg. Score: 503</td></tr></table>

Avg. Score: -303  Avg. Score: 503

# MIXED AGENT GAMES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F319bd275eb3045a8845fb598061402c5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090063&Signature=bDGhFpywtMU6BEQGb8BB%2BWtxJro%3D)

E.g. Backgammon

# Expectiminimax

Environment is an extra "random agent" player that moves after each min/max agent

• Each node computes the appropriate combination of its children

# MIXED AGENT GAMES: BACKGAMMON

Dice rolls increase b: 21 possible

rolls with 2 dice

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F4c6945e01f6e47cf945409c6c846ee22.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090063&Signature=sZ0fnjNYT6h0akBKVrKUgZOTNHM%3D)

• ≈ 20 legal moves

• Four plies (two moves each): 20 × (21 × 20)³ ≈ 1.5 × 10⁹

As depth increases, probability of reaching a given search node shrinks

• So usefulness of search is diminished

• So limiting depth is less damaging

• But pruning is trickier

Historic AI: TD-Gammon (1992) uses depth-2 search + an evaluation function learned by reinforcement learning from self-play: world-class play

The first program to reach that level by learning; a preview of the RL lectures

# UTILITIES

# MAXIMUM EXPECTED UTILITY

Why should we average utilities? Why not minimax?

Principle of maximum expected utility:

• A rational agent should chose the action that maximizes its expected utility, given its knowledge

Questions:

• Where do utilities come from?

• How do we know such utilities even exist?

• How do we know that averaging even makes sense?

• What if our behavior (preferences) cannot be described by utilities?

# WHAT UTILITIES TO USE?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F0bd9b33e0226438f8f5744602099bcc8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090064&Signature=XBmhrghU3BfXuzhX0FkpjzKOweg%3D)

For worst-case minimax reasoning, terminal function scale

does not matter

• We just want better states to have higher evaluations (get the ordering right)

• We call this insensitivity to monotonic transformations.

For average-case expectimax reasoning, we need magnitudes to be meaningful

- Read the trees above with chance nodes: averages 20 vs 25 (go right) become 800 vs 650 after squaring (go left)

# UTILITIES

Utilities are functions from outcomes (states of the world) to real numbers that describe an agent's preferences

Where do utilities come from?

• In a game, may be simple  $ (+1/ - 1) $

• Utilities summarize the agent's goals

• Theorem (von Neumann and Morgenstern, 1944): any "rational" preferences can be summarized as a utility function

We hard-wire utilities and let behaviors emerge

• Why don't we let agents pick utilities?

• Why don't we prescribe behaviors?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F1baa02c8e9e64058ab7e9069669e7003.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090064&Signature=6k9dgwywz51kGAifMuDwffjd0z4%3D)





![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F57250bf5eba84a2093d71832dab1c28d%2Fmedia%2F9c2174d721e7461bb325d78ce1a803a2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090064&Signature=R80T4eBKL9L%2Ff%2F4%2FqqWu6ENnzDs%3D)
