# Adversarial Search

CS5491: Artificial Intelligence

ZHICHAO LU

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

# TODAY

Part 1: Deterministic Games

Adversarial games, minimax search

•  $ \alpha-\beta $ pruning, depth-limited search

Part 2: Games with Chance

• Expectimax, utilities

Reading

• Today's Lecture: RN Chapter 5.1-5.3, 5.5, 16.1-16.3

• Next Lecture (Oct 8): Linear and Integer Programming

COMPLETE MAP OF OPTIMAL TIC-TAC-TOE MOVES

YOUR MOVE IS GIVEN BY THE POSITION OF THE LARGEST RED SYMBOL ON THE GRID. WHEN YOUR OPPONENT PICKS A MOVE, ZOOM IN ON THE REGION OF THE GRID WHERE THEY WENT. REPEAT.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Ffd4855e208fe4fe793948df0a87cb9fc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090388&Signature=GzrOW67osp2p%2BCD8yjyBy3jkkQE%3D)

MAP FOR O:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F396717fe654a477e9e36aa418590ca76.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090388&Signature=zHcVkKEgHLOtqPgyBhckcRQ550s%3D)

# AGENTS INTERACTING WITH AGENTS

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F09d6bfc208b24e39bc5a5b7750abb3af.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090388&Signature=TJWXlT007sFsv08FDZQf9TJOLNc%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F58e20f6690974eadac8c1f101db0ab0f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090389&Signature=ATgBmZe6LztmVubbUcq40z26y1M%3D)

Other agents act in the same world, with goals of their own: some cooperate, some compete. Games are the fully specified version of this.

# GAME PLAYING STATE-OF-THE-ART

Checkers: 1950: first computer player. 1994: Chinook ends the 40-year reign of human champion Marion Tinsley, using a complete 8-piece endgame database. 2007: checkers solved: perfect play is a draw.

# GAME PLAYING STATE-OF-THE-ART

Checkers: 1950: first computer player. 1994: Chinook ends the 40-year reign of human champion Marion Tinsley, using a complete 8-piece endgame database. 2007: checkers solved: perfect play is a draw.

Chess: 1997: Deep Blue defeats world champion Garry Kasparov in a six-game match: 200M positions per second, deep  $ \alpha $- $ \beta $ search, a hand-tuned evaluation. Today's engines (Stockfish, Leela) add neural-network evaluation and are far beyond any human.

# GAME PLAYING STATE-OF-THE-ART

Checkers: 1950: first computer player. 1994: Chinook ends the 40-year reign of human champion Marion Tinsley, using a complete 8-piece endgame database. 2007: checkers solved: perfect play is a draw.

Chess: 1997: Deep Blue defeats world champion Garry Kasparov in a six-game match: 200M positions per second, deep  $ \alpha $- $ \beta $ search, a hand-tuned evaluation. Today's engines (Stockfish, Leela) add neural-network evaluation and are far beyond any human.

Go: b > 300: brute-force search fails, and no hand-written evaluation works. 2016: AlphaGo defeats Lee Sedol with Monte Carlo tree search plus learned policy and value networks. 2017: AlphaGo Zero and AlphaZero learn Go, chess and shogi from self-play alone.

# GAME PLAYING STATE-OF-THE-ART

Checkers: 1950: first computer player. 1994: Chinook ends the 40-year reign of human champion Marion Tinsley, using a complete 8-piece endgame database. 2007: checkers solved: perfect play is a draw.

Chess: 1997: Deep Blue defeats world champion Garry Kasparov in a six-game match: 200M positions per second, deep  $ \alpha $- $ \beta $ search, a hand-tuned evaluation. Today's engines (Stockfish, Leela) add neural-network evaluation and are far beyond any human.

Go: b > 300: brute-force search fails, and no hand-written evaluation works. 2016: AlphaGo defeats Lee Sedol with Monte Carlo tree search plus learned policy and value networks. 2017: AlphaGo Zero and AlphaZero learn Go, chess and shogi from self-play alone.

Imperfect information: 2017 and 2019: Libratus and Pluribus beat top professionals at no-limit poker. 2022: Cicero plays Diplomacy at human level, negotiating with a language model.

# ADVERSARIAL GAMES

# TYPES OF GAMES

Many different kinds of games.

Axes:

• Deterministic or stochastic?

• One, two, or more players?

Zero sum?

- Perfect information (can you see the state)?

# TYPES OF GAMES

Many different kinds of games.

Axes:

• Deterministic or stochastic?

• One, two, or more players?

Zero sum?

• Perfect information (can you see the state)?

Want algorithms for calculating a strategy (policy) which recommends a move from each state.

# DETERMINISTIC GAMES

Many possible formalizations, one is:

# DETERMINISTIC GAMES

Many possible formalizations, one is:

• States S (start at  $ s_{0} $)

# DETERMINISTIC GAMES

Many possible formalizations, one is:

• States S (start at  $ s_{0} $)

Players  $ P = \{1, \ldots, N\} $ (usually take turns)

# DETERMINISTIC GAMES

Many possible formalizations, one is:

• States $S$ (start at $s_{0}$)

• Players  $ P = \{1, \ldots, N\} $ (usually take turns)

• Actions A (may depend on player / state)

# DETERMINISTIC GAMES

Many possible formalizations, one is:

• States S (start at  $ s_{0} $)

• Players  $ P = \{1, \ldots, N\} $ (usually take turns)

• Actions A (may depend on player / state)

• Transition Function  $ S \times A \rightarrow S $

# DETERMINISTIC GAMES

Many possible formalizations, one is:

• States S (start at  $ s_{0} $)

• Players  $ P = \{1, \ldots, N\} $ (usually take turns)

• Actions A (may depend on player / state)

• Transition Function  $ S \times A \rightarrow S $

• Terminal Test  $ S \rightarrow \{t, f\} $

# DETERMINISTIC GAMES

Many possible formalizations, one is:

• States S (start at  $ s_{0} $)

• Players  $ P = \{1, \ldots, N\} $ (usually take turns)

• Actions A (may depend on player / state)

• Transition Function  $ S \times A \rightarrow S $

• Terminal Test  $ S \rightarrow \{t, f\} $

• Terminal Utilities  $ S \times P \rightarrow R $

# DETERMINISTIC GAMES

Many possible formalizations, one is:

• States $S$ (start at $s_{0}$)

• Players  $ P = \{1, \ldots, N\} $ (usually take turns)

• Actions A (may depend on player / state)

• Transition Function  $ S \times A \rightarrow S $

• Terminal Test  $ S \rightarrow \{t, f\} $

• Terminal Utilities  $ S \times P \rightarrow R $

Solution for a player is a policy:  $ S \rightarrow A $

# GAME THEORY

# Zero-Sum Games

General Games

# GAME THEORY

Zero-Sum Games

• Agents have opposite utilities (values on outcomes)

Let's us think of a single value that one maximizes and the other minimizes

Adversarial, pure competition

General Games

# GAME THEORY

Zero-Sum Games

• Agents have opposite utilities (values on outcomes)

Let's us think of a single value that one maximizes and the other minimizes

Adversarial, pure competition

General Games

• Agents have independent utilities (values on outcomes)

• Cooperation, indifference, competition, and more are all possible

# ADVERSARIAL SEARCH



# SINGLE-AGENT TREES



# SINGLE-AGENT TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F496cca4419314c9fa45ec70fa639aeed.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090389&Signature=q7F%2BHW%2BYFdRxf1dLp0Q%2FCKuD%2Fz0%3D)

# SINGLE-AGENT TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F094e62a855774b2eb972502cf723eeb1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090389&Signature=NBTRMIABRXcw5ZuURjsJCBE5ox4%3D)

# SINGLE-AGENT TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Fecb0928cc5bc474fb9585cddd3438df5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090389&Signature=Tm4a10LN0fFW%2BZUYnpAyv9bxkCU%3D)

Value of State: The best achievable outcome (utility) from that state

# SINGLE-AGENT TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F9bee00f6053d4339b08548bd971a258a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090389&Signature=rfjvUqHJCDuNbjNxTQbKCgcSbuE%3D)

# SINGLE-AGENT TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Fc0e94e786bb445dcb0617e42758b7579.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090389&Signature=3MBqMu3tW%2FRVsEa5JaDYxu4wUwA%3D)

Value of State: The best achievable outcome (utility) from that state

Terminal States:  $ V(s) $ known

Non-Terminal States:  $ V(s) = \max_{s' \in children(s)} V(s') $

# ADVERSARIAL GAME TREES

# ADVERSARIAL GAME TREES

# ADVERSARIAL GAME TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F6761f2800f3b428faf2bb2cd9c3fc50c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090389&Signature=TGSUMy7Z7hO3GqQEZ23gfNgSJzY%3D)

# ADVERSARIAL GAME TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F683744dffd8c4007a48e541b765f058c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090389&Signature=V7jx%2FwILETDvLfH%2B3mOwVVxEY4c%3D)

# ADVERSARIAL GAME TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F218b9bdc92e44108a5b5f8c026b700e1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=%2BQf16xgVcWdPLNChclYSL2wQtN4%3D)

# ADVERSARIAL GAME TREES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Fd6b9632f5fee4456b82e82aa186f42e2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=hWmW7fLu806inhpWTI2ijzCvMTg%3D)

# MINIMAX VALUES

# MINIMAX VALUES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Fd61ca28c848b4921bbb8c2e67bb44184.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=n2ipcrMzEFt8xsCmFt0UlKBK05U%3D)

$$  States Under Agent^{\prime}s Control:V(s)=\max_{s^{\prime}\in successors(s)}V(s^{\prime}) $$

States Under Opponent's Control:  $ V(s) = \min_{s' \in successors(s)} V(s') $

Terminal States:  $ V(s) $ known

# MINIMAX VALUES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F99d9cee1576d4d22b17c75d229b1cae3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=IOJG5WB0BPM2oOCE6EQ6UYA%2Fhig%3D)

$$  States Under Agent^{\prime}s Control:V(s)=\max_{s^{\prime}\in successors(s)}V(s^{\prime}) $$

States Under Opponent's Control:  $ V(s) = \min_{s' \in successors(s)} V(s') $

Terminal States:  $ V(s) $ known

# MINIMAX VALUES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Fa179f1d020e34248a0d2e381fe96a496.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=R4iqRCAib%2Fb6sV3wPOZVjE1pFl4%3D)

-10

+8

States Under Agent's Control:  $ V(s) = \max_{s' \in successors(s)} V(s') $

States Under Opponent's Control:  $ V(s) = \min_{s' \in successors(s)} V(s') $

Terminal States:  $ V(s) $ known

# TIC-TAC-TOE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F20e336abff2f41628236f2c5eb2e1eb2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=OEc2TRaVqVZMCt%2FoA4r%2F8n94Iso%3D)

# ADVERSARIAL SEARCH (MINIMAX)

Deterministic, zero-sum games:

Tic-tac-toe, chess, checkers

• One player maximizes result

• The other minimizes result

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Fb8355b385441413e8a3698896d49c550.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=DTKlxAO8yJZxxM6hU%2BVIIRbxNkk%3D)

# ADVERSARIAL SEARCH (MINIMAX)

Deterministic, zero-sum games:

Tic-tac-toe, chess, checkers

• One player maximizes result

• The other minimizes result

Minimax Search:

• A state-space search tree

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F8f0fa4e1b56345039b8fd514a9544752.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=hja78btIKoeicVxm%2FNBtY2IsKBk%3D)

• Players alternate turns

• Compute each node's minimax value: the best achievable utility against a rational (optimal) adversary

# MINIMAX IMPLEMENTATION

function max-value(state)

v ← -∞ ;

for each successor of state do

v ← max(v, min - value(successor));

return v;

end

# MIN Agent:

function min-value(state)

v ← +∞ ;

for each successor of state do

v ← min(v, max - value(successor));

return v;

end

# MINIMAX IMPLEMENTATION (DISPATCH)

# Dispatch:

nction value(state)

if state is a terminal state then

| return the state's utility

end

if next agent is MAX then

| return max-value(state)

end

if next agent is MIN then

| return min-value(state)

end

# MAX Agent:

unction max-value(state)

v ← -∞ ;

for each successor of state do

v ← max(v, min − value(successor));

return v;

end

# MIN Agent:

function min-value(state)

v ← +∞ ;

for each successor of state do

v ← min(v, max − value(successor));

return v;

end

# MINIMAX EXAMPLE

# MINIMAX EXAMPLE

# MINIMAX EXAMPLE

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F91b44381ebf145688d71176256d1e5da.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090390&Signature=Oaerv5HsUCLMpq6YwQlNKtc63uQ%3D)

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F0ef63d915c65499ba0bd7155a18d86d3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090391&Signature=6FMmAD0FrZGHCROqL3JGZPJXT6k%3D)

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Facfbf78d19fe420aac7a754b38cae42b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090391&Signature=wjYSvwNU9q6VIZVVwUhjvK0fsvE%3D)

# MINIMAX EXAMPLE

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Fea5912d9011c491987af08346a22f2bd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090391&Signature=%2FXau2tSvI73TZ1CPeS10U1wEmw0%3D)

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2Fa13e68e2b5aa438f819d9578cbe972da.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090391&Signature=egVtUat4N%2FTdd7X0OCk2f7%2FJYpU%3D)

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F746d09ab428c4013af2f6b1f44b88c52.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090391&Signature=VUUUVVFCnR5e55vOqAJ%2BMf1%2F1Xs%3D)

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2Fa4b0583e0dd34322b62d27e911d47b48%2Fmedia%2F80abfa7873bd4105aabb311007f4c5cd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090391&Signature=mX4GCckNU%2FKhwvDZXR3l4XhNeow%3D)

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F2e56152927e54742beee0e598c48bc6f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090428&Signature=POI7rL1Fqso2N3X5qxxTgrmZ%2FGA%3D)

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F093569b360d8408dbe307d032e2fc5cc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090428&Signature=A6BqRWUimQDNNFbjlQc7KXWplsU%3D)

# MINIMAX EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F7681a6d248c54902bf112132006b7a4a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090428&Signature=bnA30EbltCS1tJhUJxASxeO2p4g%3D)

# MINIMAX PROPERTIES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fec05c20d53cf4f59834fec9542e84c06.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090428&Signature=QK6AtcKEYN9%2F%2BfeHpRuUms%2FFtJM%3D)

Optimal against a perfect player. Otherwise?

# MINIMAX PROPERTIES

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fb1c369f1458e40b9908547a5bde25dc3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=DlK6%2BtoTR9w3B5UBnFBmJCEgnHo%3D)

Optimal against a perfect player. Otherwise?

Minimax value 10, move left. The 100 on the right is bait: it needs the opponent to blunder, and the price of guessing wrong is 9.

# MINIMAX EFFICIENCY

How efficient is minimax?

# MINIMAX EFFICIENCY

How efficient is minimax?

• Just like (exhaustive) DFS

• Time:  $ \mathcal{O}(b^{m}) $

• Space: O(bm)

# MINIMAX EFFICIENCY

How efficient is minimax?

• Just like (exhaustive) DFS

• Time:  $ \mathcal{O}(b^{m}) $

• Space: O(bm)

Example: For chess,  $ b \approx 35 $,  $ m \approx 100 $

# MINIMAX EFFICIENCY

How efficient is minimax?

• Just like (exhaustive) DFS

• Time:  $ O(b^{m}) $

• Space: O(bm)

Example: For chess,  $ b \approx 35 $,  $ m \approx 100 $

• Exact solution is completely infeasible

• But, do we need to explore the whole tree?

# GAME TREE PRUNING

# MINIMAX PRUNING

# MINIMAX PRUNING

# MINIMAX PRUNING

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F8dd81c455c1443ba93636cf69f068244.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=sQ0D1Sdy2DnXWhwnZgRNFDnFubc%3D)

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fc75a96f8d07e44b0bb2594d4749d219f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=ohCaR0vurEJD1jMBZ0%2FfOF4l%2BSE%3D)

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fc03a002329ee47609c3092c996152c07.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=1DoFd%2FOl7JpjUhQzbzmHooncWH4%3D)

# MINIMAX PRUNING

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fbc1198050c874970b7376fb810991492.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=Dk3QNT3olVSNWD4E01aXIWu5g%2BQ%3D)

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fd6802e2689c94036997e1f8622306173.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=O%2F%2FYrirZzYTv7nK3TFLP%2FTHXFuw%3D)

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F8057eefb81364ef4aefda48e7e48687f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=9OHkAwTdnLzRUB7rrLWX5AhZ0QE%3D)

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fd61909ab7be944549e7abdaa5ec4a035.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=WOYQ6FfAwg7rV5dhKo5DQrM6it0%3D)

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F4bd8f6f0186a4e2796de9a5cc796c2bc.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090429&Signature=aaeNfLZX4FsGq7NbM4Amk9022ls%3D)

# MINIMAX PRUNING

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F78e175b5a5ac47438c4bc5107209a3d9.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=R7Llfy7XymEqQOLdKY8LxhdAqFk%3D)

pruned: at most 2 here, root already has 3

# A-B PRUNING: THE IDEA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F244a11a2b56b4f4c9eddcf60ca640838.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=Sspjwa%2FMe8%2FiRSkJYZH9ReAf%2Flw%3D)

α = 3: MAX already has 3 here.

It will never accept less on this path.

β = 8: MIN can already hold MAX to 8. It will never allow more on this path.

Only values in $(\alpha, \beta) = (3, 8)$ can still change the decision at the root.

At n: first child is 2, so  $ v \leq 2 \leq a $.

MAX above will never choose n:

stop, skip the other children.

While searching, carry two numbers for the current path from the root:

# A-B PRUNING: THE IDEA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F25a4ddaa923b4b15aeb6ef9d658b37a8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=rjbsY%2BnPlvqmYz7D7RC4sb5wpJA%3D)

α = 3: MAX already has 3 here. It will never accept less on this path.

β = 8: MIN can already hold MAX to 8. It will never allow more on this path.

Only values in $(\alpha, \beta) = (3, 8)$ can still change the decision at the root.

At n: first child is 2, so  $ v \leq 2 \leq a $.

MAX above will never choose n:

stop, skip the other children.

While searching, carry two numbers for the current path from the root:

•  $ \alpha $: the best value MAX is already guaranteed at a choice point above: a floor

# A-B PRUNING: THE IDEA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F97ebf1e5d92743c09c8b4365fdc0d198.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=T3Ctq4hFSaD15Pi%2B41PAEdFgEvI%3D)

α = 3: MAX already has 3 here. It will never accept less on this path.

β = 8: MIN can already hold MAX to 8. It will never allow more on this path.

Only values in $(\alpha, \beta) = (3, 8)$ can still change the decision at the root.

At n: first child is 2, so  $ v \leq 2 \leq a $.

MAX above will never choose n:

stop, skip the other children.

While searching, carry two numbers for the current path from the root:

•  $ \alpha $: the best value MAX is already guaranteed at a choice point above: a floor

•  $ \beta $: the best value MIN is already guaranteed above: a ceiling

# A-B PRUNING: THE IDEA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fba11cf36c9f64355857c3c32c40931b8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=UpPfek6Niy5h5EasfB6C3TDlO4Q%3D)

α = 3: MAX already has 3 here. It will never accept less on this path.

β = 8: MIN can already hold MAX to 8. It will never allow more on this path.

Only values in $(\alpha, \beta) = (3, 8)$ can still change the decision at the root.

At n: first child is 2, so  $ v \leq 2 \leq \alpha $.

MAX above will never choose n:

stop, skip the other children.

While searching, carry two numbers for the current path from the root:

•  $ \alpha $: the best value MAX is already guaranteed at a choice point above: a floor

•  $ \beta $: the best value MIN is already guaranteed above: a ceiling

Only values strictly between α and β can still change the decision at the root

# A-B PRUNING: THE IDEA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Faf6f35bd06514ed991ba00dc4ff9037c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=GoQPsux0B%2FGsyknQmD8N1rjjD%2Fo%3D)

α = 3: MAX already has 3 here. It will never accept less on this path.

β = 8: MIN can already hold MAX to 8. It will never allow more on this path.

Only values in $(\alpha, \beta) = (3, 8)$ can still change the decision at the root.

At n: first child is 2, so  $ v \leq 2 \leq a $.

MAX above will never choose n:

stop, skip the other children.

While searching, carry two numbers for the current path from the root:

•  $ \alpha $: the best value MAX is already guaranteed at a choice point above: a floor

•  $ \beta $: the best value MIN is already guaranteed above: a ceiling

Only values strictly between α and β can still change the decision at the root

At a MIN node n, v only goes down. Once  $ v \leq \alpha $, MAX above will never choose n: stop expanding n

# A-B PRUNING: THE IDEA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F5ca8afff6e4f42dbbbc9e1ee99c2ff65.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=ZWjB4KUt%2FK4iU8UXRLodUQX4V7s%3D)

α = 3: MAX already has 3 here. It will never accept less on this path.

β = 8: MIN can already hold MAX to 8. It will never allow more on this path.

Only values in $(\alpha, \beta) = (3, 8)$ can still change the decision at the root.

At n: first child is 2, so  $ v \leq 2 \leq \alpha $.

MAX above will never choose n:

stop, skip the other children.

While searching, carry two numbers for the current path from the root:

•  $ \alpha $: the best value MAX is already guaranteed at a choice point above: a floor

•  $ \beta $: the best value MIN is already guaranteed above: a ceiling

Only values strictly between α and β can still change the decision at the root

At a MIN node n, v only goes down. Once  $ v \leq \alpha $, MAX above will never choose n: stop expanding n

At a MAX node, v only goes up. Once v ≥ β, MIN above will never allow it: stop

# A-B IMPLEMENTATION

# Dispatch:

α: MAX's best option on path to root

$ \beta $: MIN's best option on path to root

# MAX Agent:

def max-value(state,  $ \alpha $,  $ \beta $):

initialize v = - $ \infty $

for each successor of state:

$ v = \max(v, \text{value}(\text{successor}, \alpha, \beta)) $

if  $ v \geq \beta $ return v

$ \alpha = max(\alpha, v) $

return v

def min-value(state,  $ \alpha $,  $ \beta $):

# MIN Agent:

initialize v = +\infty

for each successor of state:

$ v = \min(v, \text{value}(\text{successor}, \alpha, \beta)) $

if  $ v \leq \alpha $ return v

$ \beta = min(\beta, v) $

return v

# A-B IMPLEMENTATION

# Dispatch:

α: MAX's best option on path to root

$ \beta $: MIN's best option on path to root

# MAX Agent:

def max-value(state,  $ \alpha $,  $ \beta $):

initialize v = - $ \infty $

for each successor of state:

$ v = \max(v, \text{value}(\text{successor}, \alpha, \beta)) $

if  $ v \geq \beta $ return v

$ \alpha = max(\alpha, v) $

return v

# MIN Agent:

def min-value(state,  $ \alpha $,  $ \beta $):

initialize v = + $ \infty $

for each successor of state:

$ v = \min(v, \text{value}(\text{successor}, \alpha, \beta)) $

if  $ v \leq \alpha $ return v

$ \beta = min(\beta, v) $

return v

Pass down: the root calls max-value(state, -∞, +∞): no floor, no ceiling yet; every recursive call hands its current (α, β) to its children

# A-B IMPLEMENTATION

# Dispatch:

α: MAX's best option on path to root

$ \beta $: MIN's best option on path to root

# MAX Agent:

def max-value(state,  $ \alpha $,  $ \beta $):

initialize v = - $ \infty $

for each successor of state:

$ v = \max(v, \text{value}(\text{successor}, \alpha, \beta)) $

if  $ v \geq \beta $ return v

$ \alpha = max(\alpha, v) $

return v

# MIN Agent:

def min-value(state,  $ \alpha $,  $ \beta $):

initialize v = + $ \infty $

for each successor of state:

$ v = \min(v, \text{value}(\text{successor}, \alpha, \beta)) $

if  $ v \leq \alpha $ return v

$ \beta = min(\beta, v) $

return v

Pass down: the root calls max-value(state, -∞, +∞): no floor, no ceiling yet; every recursive call hands its current (α, β) to its children

Test, then update: MAX: after each child, if  $ v \geq \beta $ return  $ v $ (MIN above will not allow it), else  $ \alpha \leftarrow \max(\alpha, v) $. MIN: if  $ v \leq \alpha $ return  $ v $, else  $ \beta \leftarrow \min(\beta, v) $

# A-B ON THE EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F61ab012b32b440c8b7bce305b86f0c6b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=Cp99FRrmKYMeum4ntkd09JCfuxA%3D)

<table><tr><td>Call</td><td>$ (\alpha,\beta) $ received</td><td>Children seen</td><td>Returns</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# A-B ON THE EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F3b92d09f343e4f8883af4e454e9f5e01.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=oIwGmhkZyzfxyr%2FXjf%2B%2BaBo1Rdw%3D)

<table><tr><td>Call</td><td>$ (\alpha,\beta) $ received</td><td>Children seen</td><td>Returns</td></tr><tr><td>root, MAX</td><td>$ (-\infty,+\infty) $</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# A-B ON THE EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Fef069cc509e847c8a2fe2cb84ce69f18.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090430&Signature=YsSsN4kKSkiPhUMEwWsYUvX7Rlo%3D)

<table><tr><td>Call</td><td>$ (\alpha, \beta) $ received</td><td>Children seen</td><td>Returns</td></tr><tr><td>root, MAX</td><td>$ (-\infty, +\infty) $</td><td></td><td></td></tr><tr><td>left MIN</td><td>$ (-\infty, +\infty) $</td><td>3, 12, 8:  $ v = 3 $, never ≤  $ \alpha $</td><td>3; root sets  $ \alpha = 3 $</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# A-B ON THE EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2Ff36429c50c914cebbf226e390b2b883e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090431&Signature=6sZ%2B6WRAajaDiICYDMU4%2BME5MFQ%3D)

<table><tr><td>Call</td><td>$ (\alpha, \beta) $ received</td><td>Children seen</td><td>Returns</td></tr><tr><td>root, MAX</td><td>$ (-\infty, +\infty) $</td><td></td><td></td></tr><tr><td>left MIN</td><td>$ (-\infty, +\infty) $</td><td>3, 12, 8:  $ v = 3 $, never ≤  $ \alpha $</td><td>3; root sets  $ \alpha = 3 $</td></tr><tr><td>middle MIN</td><td>$ (3, +\infty) $</td><td>2:  $ v = 2 ≤ \alpha $</td><td>2 at once: the other two children are never generated</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# A-B ON THE EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F7613bbd2e6a044e180599ac5533fea12.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090431&Signature=FvUYwp%2BB9CWbIi4NVvlcVsgpc3c%3D)

<table><tr><td>Call</td><td>$ (\alpha, \beta) $ received</td><td>Children seen</td><td>Returns</td></tr><tr><td>root, MAX</td><td>$ (-\infty, +\infty) $</td><td></td><td></td></tr><tr><td>left MIN</td><td>$ (-\infty, +\infty) $</td><td>3, 12, 8:  $ v = 3 $, never ≤  $ \alpha $</td><td>3; root sets  $ \alpha = 3 $</td></tr><tr><td>middle MIN</td><td>$ (3, +\infty) $</td><td>2:  $ v = 2 ≤ \alpha $</td><td>2 at once: the other two children are never generated</td></tr><tr><td>right MIN</td><td>$ (3, +\infty) $</td><td>14, 5, 2:  $ v $ stays above 3 until the last child</td><td>2; nothing to prune</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# A-B ON THE EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F96c3d2a842e041d2a697d428790be783.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090431&Signature=8l77qK7Zcb35zuCjNUWHz5XMjuM%3D)

<table><tr><td>Call</td><td>$ (\alpha, \beta) $ received</td><td>Children seen</td><td>Returns</td></tr><tr><td>root, MAX</td><td>$ (-\infty, +\infty) $</td><td></td><td></td></tr><tr><td>left MIN</td><td>$ (-\infty, +\infty) $</td><td>3, 12, 8:  $ v = 3 $, never ≤  $ \alpha $</td><td>3; root sets  $ \alpha = 3 $</td></tr><tr><td>middle MIN</td><td>$ (3, +\infty) $</td><td>2:  $ v = 2 ≤ \alpha $</td><td>2 at once: the other two children are never generated</td></tr><tr><td>right MIN</td><td>$ (3, +\infty) $</td><td>14, 5, 2:  $ v $ stays above 3 until the last child</td><td>2; nothing to prune</td></tr><tr><td>root</td><td></td><td>max(3, 2, 2)</td><td>3: move left</td></tr></table>

# A-B ON THE EXAMPLE

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F95d900af8dcc49f080381aa5a910432c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090431&Signature=pTmc399Q3c7ByJbOe5rVA3y160Q%3D)

<table><tr><td>Call</td><td>$ (\alpha, \beta) $ received</td><td>Children seen</td><td>Returns</td></tr><tr><td>root, MAX</td><td>$ (-\infty, +\infty) $</td><td></td><td></td></tr><tr><td>left MIN</td><td>$ (-\infty, +\infty) $</td><td>3, 12, 8:  $ v = 3 $, never ≤  $ \alpha $</td><td>3; root sets  $ \alpha = 3 $</td></tr><tr><td>middle MIN</td><td>$ (3, +\infty) $</td><td>2:  $ v = 2 ≤ \alpha $</td><td>2 at once: the other two children are never generated</td></tr><tr><td>right MIN</td><td>$ (3, +\infty) $</td><td>14, 5, 2:  $ v $ stays above 3 until the last child</td><td>2; nothing to prune</td></tr><tr><td>root</td><td></td><td>max(3, 2, 2)</td><td>3: move left</td></tr></table>

Had the middle leaves come as 6, 4, 2, all three would have been seen: pruning depends on the order.

# A-B PRUNING PROPERTIES

# A-B PRUNING PROPERTIES

This pruning has no effect on minimax value computed for the root.

# A-B PRUNING PROPERTIES

This pruning has no effect on minimax value computed for the root. Values of intermediate nodes might be wrong

• Important: children of the root may have the wrong value

• So the most naïve version won’t let you do action selection

# A-B PRUNING PROPERTIES

This pruning has no effect on minimax value computed for the root.

Values of intermediate nodes might be wrong

• Important: children of the root may have the wrong value

• So the most naïve version won’t let you do action selection

Good child ordering improves effectiveness of pruning

# A-B PRUNING PROPERTIES

This pruning has no effect on minimax value computed for the root. Values of intermediate nodes might be wrong

• Important: children of the root may have the wrong value

• So the most naive version won't let you do action selection

Good child ordering improves effectiveness of pruning

With "perfect ordering":

• Time complexity drops to  $ \mathcal{O}(b^{\frac{m}{2}}) $

- Doubles solvable depth

• Full search of, e.g. chess, is still hopeless . . .

# A-B PRUNING PROPERTIES

This pruning has no effect on minimax value computed for the root. Values of intermediate nodes might be wrong

• Important: children of the root may have the wrong value

• So the most naive version won't let you do action selection

Good child ordering improves effectiveness of pruning

With "perfect ordering":

• Time complexity drops to  $ \mathcal{O}(b^{\frac{m}{2}}) $

- Doubles solvable depth

• Full search of, e.g. chess, is still hopeless . . .

This is a simple example of metareasoning (computing about what to compute)

# CONSTRAINTED RESOURCES

Problem: In realistic games, cannot search to leaves.

# CONSTRAINTED RESOURCES

Problem: In realistic games, cannot search to leaves.

Solution: Depth-limited search

• Instead, search only to a limited depth in the tree

• Replace terminal utilities with an evaluation function for non-terminal positions

# CONSTRAINTED RESOURCES

Problem: In realistic games, cannot search to leaves.

Solution: Depth-limited search

• Instead, search only to a limited depth in the tree

• Replace terminal utilities with an evaluation function for non-terminal positions

Example:

• Suppose we have 100 seconds, can explore 10K nodes / sec

• So can check 1M nodes per move

• α-β reaches about depth 8 – decent chess program

# CONSTRAINTED RESOURCES

Problem: In realistic games, cannot search to leaves.

Solution: Depth-limited search

• Instead, search only to a limited depth in the tree

• Replace terminal utilities with an evaluation function for non-terminal positions

Example:

• Suppose we have 100 seconds, can explore 10K nodes / sec

• So can check 1M nodes per move

α-β reaches about depth 8 – decent chess program

Guarantee of optimal play is gone

More depth makes a BIG difference

Use iterative deepening for an anytime algorithm

# SUMMARY: ADVERSARIAL SEARCH

<table><tr><td></td><td>Minimax</td><td>$ \alpha-\beta $ pruning</td><td>Depth-limited + evaluation</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# SUMMARY: ADVERSARIAL SEARCH

<table><tr><td></td><td>Minimax</td><td>$ \alpha-\beta $ pruning</td><td>Depth-limited + evaluation</td></tr><tr><td>Answer</td><td>Exact minimax value and move</td><td>Same value, same move</td><td>Approximate; as good as the evaluation function</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# SUMMARY: ADVERSARIAL SEARCH

<table><tr><td></td><td>Minimax</td><td>$ \alpha-\beta $ pruning</td><td>Depth-limited + evaluation</td></tr><tr><td>Answer</td><td>Exact minimax value and move</td><td>Same value, same move</td><td>Approximate; as good as the evaluation function</td></tr><tr><td>Optimal against a perfect opponent?</td><td>Yes</td><td>Yes</td><td>No guarantee</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# SUMMARY: ADVERSARIAL SEARCH

<table><tr><td></td><td>Minimax</td><td>$ \alpha-\beta $ pruning</td><td>Depth-limited + evaluation</td></tr><tr><td>Answer</td><td>Exact minimax value and move</td><td>Same value, same move</td><td>Approximate; as good as the evaluation function</td></tr><tr><td>Optimal against a perfect opponent?</td><td>Yes</td><td>Yes</td><td>No guarantee</td></tr><tr><td>Time</td><td>$ \mathcal{O}(b^{m}) $</td><td>$ \mathcal{O}(b^{m/2}) $ with perfect move ordering</td><td>$ \mathcal{O}(b^{d}) $, choose  $ d $ to fit the clock</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# SUMMARY: ADVERSARIAL SEARCH

<table><tr><td></td><td>Minimax</td><td>$ \alpha-\beta $ pruning</td><td>Depth-limited + evaluation</td></tr><tr><td>Answer</td><td>Exact minimax value and move</td><td>Same value, same move</td><td>Approximate; as good as the evaluation function</td></tr><tr><td>Optimal against a perfect opponent?</td><td>Yes</td><td>Yes</td><td>No guarantee</td></tr><tr><td>Time</td><td>$ \mathcal{O}(b^{m}) $</td><td>$ \mathcal{O}(b^{m/2}) $ with perfect move ordering</td><td>$ \mathcal{O}(b^{d}) $, choose  $ d $ to fit the clock</td></tr><tr><td>Space</td><td>$ \mathcal{O}(bm) $</td><td>$ \mathcal{O}(bm) $</td><td>$ \mathcal{O}(bd) $</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

# SUMMARY: ADVERSARIAL SEARCH

<table><tr><td></td><td>Minimax</td><td>$ \alpha-\beta $ pruning</td><td>Depth-limited + evaluation</td></tr><tr><td>Answer</td><td>Exact minimax value and move</td><td>Same value, same move</td><td>Approximate; as good as the evaluation function</td></tr><tr><td>Optimal against a perfect opponent?</td><td>Yes</td><td>Yes</td><td>No guarantee</td></tr><tr><td>Time</td><td>$ \mathcal{O}(b^{m}) $</td><td>$ \mathcal{O}(b^{m/2}) $ with perfect move ordering</td><td>$ \mathcal{O}(b^{d}) $, choose  $ d $ to fit the clock</td></tr><tr><td>Space</td><td>$ \mathcal{O}(bm) $</td><td>$ \mathcal{O}(bm) $</td><td>$ \mathcal{O}(bd) $</td></tr><tr><td>What you give up</td><td>Feasible only for tiny games</td><td>Nothing; the gain depends on move ordering</td><td>Optimality; horizon effects</td></tr></table>

# SUMMARY: ADVERSARIAL SEARCH

<table><tr><td></td><td>Minimax</td><td>$ \alpha-\beta $ pruning</td><td>Depth-limited + evaluation</td></tr><tr><td>Answer</td><td>Exact minimax value and move</td><td>Same value, same move</td><td>Approximate; as good as the evaluation function</td></tr><tr><td>Optimal against a perfect opponent?</td><td>Yes</td><td>Yes</td><td>No guarantee</td></tr><tr><td>Time</td><td>$ \mathcal{O}(b^{m}) $</td><td>$ \mathcal{O}(b^{m/2}) $ with perfect move ordering</td><td>$ \mathcal{O}(b^{d}) $, choose  $ d $ to fit the clock</td></tr><tr><td>Space</td><td>$ \mathcal{O}(bm) $</td><td>$ \mathcal{O}(bm) $</td><td>$ \mathcal{O}(bd) $</td></tr><tr><td>What you give up</td><td>Feasible only for tiny games</td><td>Nothing; the gain depends on move ordering</td><td>Optimality; horizon effects</td></tr></table>

Chess:  $ b \approx 35 $,  $ m \approx 100 $. A million nodes per move buys depth 8 with  $ \alpha $- $ \beta $; iterative deepening makes it anytime.

# Q & A

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F60f1c28a2dfa4812ac453c91d7341f30%2Fmedia%2F323c61793394447eb157783751aded77.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090431&Signature=Skay8yl0nYZZaAR1kBWuEmbdmPg%3D)
