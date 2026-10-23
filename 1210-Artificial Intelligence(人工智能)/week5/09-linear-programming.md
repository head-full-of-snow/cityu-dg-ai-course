Linear Programming

CS5491: Artificial Intelligence

ZHICHAO LU

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

# ANNOUNCEMENTS

Project proposal: 15 October 2026, 23:59 (BJT)

Submit through Canvas. The group project is worth 30% of the course grade.

# Midterm: 22 October 2026

Worth 20% of the course grade. Check Canvas for preparation materials.

# WHAT TO EAT?

We want to meet the given nutrition targets at minimum cost.

We can choose the amount of stir-fry (ounces) and boba (fluid ounces).

<table><tr><td>Nutrition targets</td><td>Food</td><td>Cost (units)</td><td>Calories</td><td>Sugar (g)</td><td>Calcium (mg)</td></tr><tr><td rowspan="2">$2000 \leq \text{Calories} \leq 2500$</td><td>stir-fry (per oz)</td><td>1</td><td>100</td><td>3</td><td>20</td></tr><tr><td>Boba (per fl oz)</td><td>0.4</td><td>50</td><td>4</td><td>70</td></tr><tr><td>$\text{Sugar} \leq 100\backslash, \text{text} \leq 100\backslash$</td><td>$ \text{Calcium} \leq 700\backslash, \text{text} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash$</td></tr></table>

What is the cheapest way to meet these targets with this menu?

How much stir-fry (ounces) and boba (fluid ounces) should we buy?

# CAN SEARCH ALGORITHMS HELP?

Essence of search algorithms:

- explore candidate states until a goal is reached

use additional information to avoid unnecessary search

Can we adopt a similar strategy here?

# OPTIMIZATION

Problem Description

Optimization Representation

$$\begin{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

# Graphical Representation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2F1b9a73f39b254666808dc5ba1a9c42c8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090138&Signature=cOvn30cA1Ka973TFHlQuikhroTA%3D)

# WHAT TO EAT?: CONSTRAINTS

We want to meet the given nutrition targets at minimum cost.

We can choose the amount of stir-fry (ounces) and boba (fluid ounces).

<table><tr><td>Nutrition targets</td><td>Food</td><td>Cost (units)</td><td>Calories</td><td>Sugar (g)</td><td>Calcium (mg)</td></tr><tr><td rowspan="2">$2000 \leq \text{Calories} \leq 2500$</td><td>stir-fry (per oz)</td><td>1</td><td>100</td><td>3</td><td>20</td></tr><tr><td>Boba (per fl oz)</td><td>0.4</td><td>50</td><td>4</td><td>70</td></tr><tr><td>$\text{Sugar} \leq 100\backslash, \text{text} \leq 100\backslash$</td><td>$ \text{Calcium} \leq 700\backslash, \text{text} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash$</td></tr></table>

What is the cheapest way to meet these targets with this menu?

How much stir-fry (ounces) and boba (fluid ounces) should we buy?

# CONSTRAINT SATISFACTION PROBLEMS

# Map Coloring $$ \begin{aligned} Any\\ & \text{begin{aligned} Any\\ & \text{begin{aligned} Any\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text{begin{aligned} Any}\\ & \text

# WHAT TO EAT?: COSTS

We want to meet the given nutrition targets at minimum cost.

We can choose the amount of stir-fry (ounces) and boba (fluid ounces).

<table><tr><td>Nutrition targets</td><td>Food</td><td>Cost (units)</td><td>Calories</td><td>Sugar (g)</td><td>Calcium (mg)</td></tr><tr><td rowspan="2">$2000 \leq \text{Calories} \leq 2500$</td><td>stir-fry (per oz)</td><td>1</td><td>100</td><td>3</td><td>20</td></tr><tr><td>Boba (per fl oz)</td><td>0.4</td><td>50</td><td>4</td><td>70</td></tr><tr><td>$\text{Sugar} \leq 100\backslash, \text{text} \leq 100\backslash$</td><td>$ \text{Calcium} \leq 700\backslash, \text{text} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash, \text{text} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash, \text{text} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash, \text{text} \leq 700\backslash$</td><td>$ \text{Calcium} \leq 700\backslash, \text{text} \leq 700\backslash$</td></tr></table>

What is the cheapest way to meet these targets with this menu?

How much stir-fry (ounces) and boba (fluid ounces) should we buy?

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

Nutrition targets

$2000 \leq

\text{Calories} \leq

2500$

$\text{Sugar} \leq 100\$, \text{g}$

<table><tr><td>Food</td><td>Cost (units)</td><td>Calories</td><td>Sugar (g)</td><td>Calcium (mg)</td></tr><tr><td>stir-fry (per oz)</td><td>1</td><td>100</td><td>3</td><td>20</td></tr><tr><td>Boba (per fl oz)</td><td>0.4</td><td>50</td><td>4</td><td>70</td></tr></table>

$\text{Calcium}

\geq 700\backslash,\backslash\text{mg}$

$\{\mathbf{x}\}$

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

Nutrition targets

$2000 \leq

\text{Calories} \leq

2500$

$\text{Sugar} \leq 100\$, \text{g}$

<table><tr><td>Food</td><td>Cost (units)</td><td>Calories</td><td>Sugar (g)</td><td>Calcium (mg)</td></tr><tr><td>stir-fry (per oz)</td><td>1</td><td>100</td><td>3</td><td>20</td></tr><tr><td>Boba (per fl oz)</td><td>0.4</td><td>50</td><td>4</td><td>70</td></tr></table>

$\text{Calcium}

\geq 700\backslash,\backslash\text{mg}$

Diet Problem $\begin{aligned}

\begin{aligned}

aligned \\

aligned

\end{aligned}

\end{aligned}

\min_{\mathrm{x}}~&\sim\mathrm{cost(\mathrm{x})} \\\

s.t.~\&~calories( $ mathbf{x} $) \leq 2500 \

~&~calories(\mathbf{x}) \geq 2000 \

~&~sugar(\mathbf{x}) \leq 100 \

~&~calcium( $ \mathrm{mathbf{x}} $) \geq 700

\end{aligned} $$

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

$2000 \leq

\text{Calories} \leq

2500$

$\text{Sugar} \leq 100\$, \text{g}$

<table><tr><td>Food</td><td>Cost (units)</td><td>Calories</td><td>Sugar (g)</td><td>Calcium (mg)</td></tr><tr><td>stir-fry (per oz)</td><td>1</td><td>100</td><td>3</td><td>20</td></tr><tr><td>Boba (per fl oz)</td><td>0.4</td><td>50</td><td>4</td><td>70</td></tr></table>

$\text{Calcium}

\geq 700\backslash,\backslash\text{mg}$

Diet Problem $\begin{aligned}aligned$

\min_{\mathrm{x}} && 1x_1 + 0.4x_2 \ s.t. &&

100x_1 + 50x_2 \geq 2000 \& 100x_1 +

50x_2 \leq 2500 \& 3x_1 + 4x_2 \leq 100 \

&& 20x_1 + 70x_2 \geq 700 \end{aligned} $$

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

Diet Problem $$ \begin{aligned}

\min_{\{\mathbf{mathbf\{x\}} \& \& c\_1x\_1 + c\_2x\_2}

\s.t. \& \& a_{\{1,1\}x\_1 + a_{\{1,2\}x\_2} \geq q

b\_1 \& \& a_{\{2,1\}x\_1 + a_{\{2,2\}x\_2} \geq q

b\_2 \& \& a_{\{3,1\}x\_1 + a_{\{3,2\}x\_2} \geq q

b\_3 \& \& a_{\{4,1\}x\_1 + a_{\{4,2\}x\_2} \geq q

b\_4 \end{aligned}

$$A=\begin{cases} bmatrix} 100 & 50 \\ 100 & 50 \\ 3 & 4 \\ 20 & 70 \\ end\begin{cases}

\end{cases}

\sim

\begin{cases}

bmatrix \\

2000 & 2500 \\ 100 & 700 \\ end\begin{cases}

bmatrix \\

\end{cases}

\end{cases}

\begin{cases}

\sim

\end{cases}

\sim

\begin{cases}

bmatrix \\

\end{cases}

\begin{cases}

1 & 1 \\

\end{cases}

\begin{cases}

0.4 & \end{cases}

\begin{cases}

bmatrix \\

\end{cases}

\begin{cases}

$$

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

Diet Problem $$ \begin{aligned}

\min_{\text{mathbf{x}}} \&

\mathbf{c}^T\mathbf{x} \\\text{s.t. } \&

a_{\text{1,1}}x_1 + a_{\text{1,2}}x_2 \geq \text{b}_1 \geq \text{b}_2 \geq \text{b}_3 \geq \text{b}_4 \geq \text{b}_5 \geq \text{b}_6 \geq \text{b}_7 \geq \text{b}_8 \geq \text{b}_9 \geq \text{b}_{10} \geq \text{b}_{11} \geq \text{b}_{12} \geq \text{b}_{13} \geq \text{b}_{14} \geq \text{b}_{15} \geq \text{b}_{16} \geq \text{b}_{17} \geq \text{b}_{18} \geq \text{b}_{19} \geq \text{b}_{20} \geq \text{b}_{21} \geq \text{b}_{22} \geq \text{b}_{23} \geq \text{b}_{24} \geq \text{b}_{25} \geq \text{b}_{26} \geq \text{b}_{27} \geq \text{b}_{28} \geq \text{b}_{29} \geq \text{b}_{30} \geq \text{b}_{31} \geq \text{b}_{32} \geq \text{b}_{33} \geq \text{b}_{34} \geq \text{b}_{35} \geq \text{b}_{36} \geq \text{b}_{37} \geq \text{b}_{38} \geq \text{b}_{39} \geq \text{b}_{40} \geq \text{b}_{41} \geq \text{b}_{42} \geq \text{b}_{43} \geq \text{b}_{44} \geq \text{b}_{45} \geq \text{b}_{46} \geq \text{b}_{47} \geq \text{b}_{48} \geq \text{b}_{49} \geq \text{b}_{50} \geq \text{b}_{51} \geq \text{b}_{52} \geq \text{b}_{53} \geq \text{b}_{54} \geq \text{b}_{55} \geq \text{b}_{56} \geq \text{b}_{57} \geq \text{b}_{58} \geq \text{b}_{59} \geq \text{b}_{60} \geq \text{b}_{61} \geq \text{b}_{62} \geq \text{b}_{63} \geq \text{b}_{64} \geq \text{b}_{65} \geq \text{b}_{66} \geq \text{b}_{67} \geq \text{b}_{68} \geq \text{b}_{69} \geq \text{b}_{70} \geq \text{b}_{71} \geq \text{b}_{72} \geq \text{b}_{73} \geq \text{b}_{74} \geq \text{b}_{75} \geq \text{b}_{76} \geq \text{b}_{77} \geq \text{b}_{78} \geq \text{b}_{79} \geq \text{b}_{80} \geq \text{b}_{81} \geq \text{b}_{82} \geq \text{b}_{83} \geq \text{b}_{84} \geq \text{b}_{85} \geq \text{b}_{86} \geq \text{b}_{87} \geq \text{b}_{88} \geq \text{b}_{89} \geq \text{b}_{90} \geq \text{b}_{91} \geq \text{b}_{92} \geq \text{b}_{93} \geq \text{b}_{94} \geq \text{b}_{95} \geq \text{b}_{96} \geq \text{b}_{97} \geq \text{b}_{98} \geq \text{b}_{99} \geq \text{b}_{100} \geq \text{b}_{101} \geq \text{b}_{102} \geq \text{b}_{103} \geq \text{b}_{104} \geq \text{b}_{105} \geq \text{b}_{106} \geq \text{b}_{107} \geq \text{b}_{108} \geq \text{b}_{109} \geq \text{b}_{110} \geq \text{b}_{111} \geq \text{b}_{112} \geq \text{b}_{113} \geq \text{b}_{114} \geq \text{b}_{115} \geq \text{b}_{116} \geq \text{b}_{117} \geq \text{b}_{118} \geq \text{b}_{119} \geq \text{b}_{120} \geq \text{b}_{121} \geq \text{b}_{122} \geq \text{b}_{123} \geq \text{b}_{124} \geq \text{b}_{125} \geq \text{b}_{126} \geq \text{b}_{127} \geq \text{b}_{128} \geq \text{b}_{129} \geq \text{b}_{130} \geq \text{b}_{131} \geq \text{b}_{132} \geq \text{b}_{133} \geq \text{b}_{134} \geq \text{b}_{135} \geq \text{b}_{136} \geq \text{b}_{137} \geq \text{b}_{138} \geq \text{b}_{139} \geq \text{b}_{140} \geq \text{b}_{141} \geq \text{b}_{142} \geq \text{b}_{143} \geq \text{b}_{144} \geq \text{b}_{145} \geq \text{b}_{146} \geq \text{b}_{147} \geq \text{b}_{148} \geq \text{b}_{149} \geq \text{b}_{150} \geq \text{b}_{151} \geq \text{b}_{152} \geq \text{b}_{153} \geq \text{b}_{154} \geq \text{b}_{155} \geq \text{b}_{156} \geq \text{b}_{157} \geq \text{b}_{158} \geq \text{b}_{159} \geq \text{b}_{160} \geq \text{b}_{161} \geq \text{b}_{162} \geq \text{b}_{163} \geq \text{b}_{164} \geq \text{b}_{165} \geq \text{b}_{166} \geq \text{b}_{167} \geq \text{b}_{168} \geq \text{b}_{169} \geq \text{b}_{170} \geq \text{b}_{171} \geq \text{b}_{172} \geq \text{b}_{173} \geq \text{b}_{174} \geq \text{b}_{175} \geq \text{b}_{176} \geq \text{b}_{177} \geq \text{b}_{178} \geq \text{b}_{179} \geq \text{b}_{180} \geq \text{b}_{181} \geq \text{b}_{182} \geq \text{b}_{183} \geq \text{b}_{184} \geq \text{b}_{185} \geq \text{b}_{186} \geq \text{b}_{187} \geq \text{b}_{188} \geq \text{b}_{189} \geq \text{b}_{190} \geq \text{b}_{191} \geq \text{b}_{192} \geq \text{b}_{193} \geq \text{b}_{194} \geq \text{b}_{195} \geq \text{b}_{196} \geq \text{b}_{197} \geq \text{b}_{198} \geq \text{b}_{199} \geq \text{b}_{200} \geq \text{b}_{201} \geq \text{b}_{202} \geq \text{b}_{203} \geq \text{b}_{204} \geq \text{b}_{205} \geq \text{b}_{206} \geq \text{b}_{207} \geq \text{b}_{208} \geq \text{b}_{209} \geq \text{b}_{210} \geq \text{b}_{211} \geq \text{b}_{212} \geq \text{b}_{213} \geq \text{b}_{214} \geq \text{b}_{215} \geq \text{b}_{216} \geq \text{b}_{217} \geq \text{b}_{218} \geq \text{b}_{219} \geq \text{b}_{220} \geq \text{b}_{221} \geq \text{b}_{222} \geq \text{b}_{223} \geq \text{b}_{224} \geq \text{b}_{225} \geq \text{b}_{226} \geq \text{b}_{227} \geq \text{b}_{228} \geq \text{b}_{229} \geq \text{b}_{230} \geq \text{b}_{231} \geq \text{b}_{232} \geq \text{b}_{233} \geq \text{b}_{234} \geq \text{b}_{235} \geq \text{b}_{236} \geq \text{b}_{237} \geq \text{b}_{238} \geq \text{b}_{239} \geq \text{b}_{240} \geq \text{b}_{241} \geq \text{b}_{242} \geq \text{b}_{243} \geq \text{b}_{244} \geq \text{b}_{245} \geq \text{b}_{246} \geq \text{b}_{247} \geq \text{b}_{248} \geq \text{b}_{249} \geq \text{b}_{250} \geq \text{b}_{251} \geq \text{b}_{252} \geq \text{b}_{253} \geq \text{b}_{254} \geq \text{b}_{255} \geq \text{b}_{256} \geq \text{b}_{257} \geq \text{b}_{258} \geq \text{b}_{259} \geq \text{b}_{260} \geq \text{b}_{261} \geq \text{b}_{262} \geq \text{b}_{263} \geq \text{b}_{264} \geq \text{b}_{265} \geq \text{b}_{266} \geq \text{b}_{267} \geq \text{b}_{268} \geq \text{b}_{269} \geq \text{b}_{270} \geq \text{b}_{271} \geq \text{b}_{272} \geq \text{b}_{273} \geq \text{b}_{274} \geq \text{b}_{275} \geq \text{b}_{276} \geq \text{b}_{277} \geq \text{b}_{278} \geq \text{b}_{279} \geq \text{b}_{280} \geq \text{b}_{281} \geq \text{b}_{282} \geq \text{b}_{283} \geq \text{b}_{284} \geq \text{b}_{285} \geq \text{b}_{286} \geq \text{b}_{287} \geq \text{b}_{288} \geq \text{b}_{289} \geq \text{b}_{290} \geq \text{b}_{291} \geq \text{b}_{292} \geq \text{b}_{293} \geq \text{b}_{294} \geq \text{b}_{295} \geq \text{b}_{296} \geq \text{b}_{297} \geq \text{b}_{298} \geq \text{b}_{299} \geq \text{b}_{300} \geq \text{b}_{301} \geq \text{b}_{302} \geq \text{b}_{303} \geq \text{b}_{304} \geq \text{b}_{305} \geq \text{b}_{306} \geq \text{b}_{307} \geq \text{b}_{308} \geq \text{b}_{309} \geq \text{b}_{310} \geq \text{b}_{311} \geq \text{b}_{312} \geq \text{b}_{313} \geq \text{b}_{314} \geq \text{b}_{315} \geq \text{b}_{316} \geq \text{b}_{317} \geq \text{b}_{318} \geq \text{b}_{319} \geq \text{b}_{320} \geq \text{b}_{321} \geq \text{b}_{322} \geq \text{b}_{323} \geq \text{b}_{324} \geq \text{b}_{325} \geq \text{b}_{326} \geq \text{b}_{327} \geq \text{b}_{328} \geq \text{b}_{329} \geq \text{b}_{330} \geq \text{b}_{331} \geq \text{b}_{332} \geq \text{b}_{333} \geq \text{b}_{334} \geq \text{b}_{335} \geq \text{b}_{336} \geq \text{b}_{337} \geq \text{b}_{338} \geq \text{b}_{339} \geq \text{b}_{340} \geq \text{b}_{341} \geq \text{b}_{342} \geq \text{b}_{343} \geq \text{b}_{344} \geq \text{b}_{345} \geq \text{b}_{346} \geq \text{b}_{347} \geq \text{b}_{348} \geq \text{b}_{349} \geq \text{b}_{350} \geq \text{b}_{351} \geq \text{b}_{352} \geq \text{b}_{353} \geq \text{b}_{354} \geq \text{b}_{355} \geq \text{b}_{356} \geq \text{b}_{357} \geq \text{b}_{358} \geq \text{b}_{359} \geq \text{b}_{360} \geq \text{b}_{361} \geq \text{b}_{362} \geq \text{b}_{363} \geq \text{b}_{364} \geq \text{b}_{365} \geq \text{b}_{366} \geq \text{b}_{367} \geq \text{b}_{368} \geq \text{b}_{369} \geq \text{b}_{370} \geq \text{b}_{371} \geq \text{b}_{372} \geq \text{b}_{373} \geq \text{b}_{374} \geq \text{b}_{375} \geq \text{b}_{376} \geq \text{

$$A=\begin{cases} bmatrix \\ 100 & 50 & 100 & 50 & 3 & 4 & 20 & 70\end{cases}

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

Diet Problem $$ \begin{aligned}

\min_{\text{}\begin{aligned}

\text{x}}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

\end{aligned}

\begin{aligned}

\text{x}

$$A=\begin{cases} 100 & 50 \\\end{cases}

4 \\\begin{cases}

\end{cases}

b=\begin{cases}

2000 & 2500 \\\end{cases}

700\end{cases}

{\begin{cases}

\end{cases}

0.4\end{cases}

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

Diet Problem $$ \begin{aligned}

\min_{\text{mathbf{x}}} \&

\mathbf{c}^T\mathbf{x} \\\text{s.t. } \&

a_{\text{1,1}}x_1 + a_{\text{1,2}}x_2 \

a_{\text{2,1}}x_1 + a_{\text{2,2}}x_2 \

a_{\text{3,1}}x_1 + a_{\text{3,2}}x_2 \

a_{\text{4,1}}x_1 + a_{\text{4,2}}x_2 \

\end{aligned}

\begin{cases} bmatrix \\ -2000 & 2500 \\ 100 & \end{cases}

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

\mathbf{q} \

$$A=\begin{cases}bmatrix}-100 & -50 \\ 100 & 50\end{cases}3 & 4

\\ -20 & -70\end{bmatrix} ~~

b=\begin{bmatrix}-2000 \ \ 2500 \ \ 100 \ \

-700\end{bmatrix}

{\rm{\sim and~}}~c=\begin{bmatrix}1\ \\\end{bmatrix}

0.4\end{bmatrix}$

# LINEAR PROGRAMMING

Linear objective with linear constraints

$$ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \text{aligned} \left\{ \begin{aligned} \text{aligned} \text{aligned} \text{

As opposed to general optimization

$$ \begin{aligned} \text{aligned} \left\{ \begin{array}{l} \text{aligned} \left\{ \begin{array}{l} \text{aligned} \left\{ \begin

g_i(\mathbf{x}) \leq 0, i=1,\dots,M \&

h_i(\mathrm{mathbf{x}})=0, i=1,\mathrm{dots,P}

\end{aligned} $$

# LINEAR PROGRAMMING

Different formulations

Inequality Form

$$ \begin{aligned} \text{aligned} \\ \text{aligned

General Form

\begin{aligned}

Standard Form (here)

\begin{aligned}

# OPTIMIZATION

Problem Description

Optimization Representation

$$\begin{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

# Graphical Representation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2Fd9641eac350740969518f536caea72c4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=w0I5cabwFRObJ65KgYBKSk3Vf38%3D)

GRAPHICAL REPRESENTATION

What shape does this inequality represent?

$$ a_{1x}1 + a_{2x}2 \backslash \text{eq b}_1$$

# COST CONTOURS

Illustration: $\mathrm{b}{c}=[1,1]^T$.

Each line has constant cost:

$$\mathrm{b}{c}^T\mathrm{mathbf}{x}=x_{1+x_{2}}=k.$$

$$k\mathrm{in}\{-2,-1,0,1,2\}$$

The contours are parallel. The vector $\mathrm{b}{c}$ is perpendicular to them and points toward increasing cost.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2F77bf1766c80b4ced884a51c75c6b40f3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=huFhUXtwwxhCgllY6qRqW24aG%2BY%3D)

# LP GRAPHICAL REPRESENTATION

Inequality Form

# $$ \begin{aligned} \text{aligned} \left\{ \begin{array}{l} \text{aligned} \left\{ \begin{array}{l} \text{aligned} \left\{ \begin

Start with no constraints

Add one constraint at a time

# OPTIMIZATION

Problem Description

Optimization Representation

$$\begin{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

\text{aligned}

\begin{aligned}

# Graphical Representation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2F67ac5eb4f2834de384c02a296ef1907a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=r2eDNWYsyzYIa8rFCHARMN3XYDQ%3D)

# OPTIMIZATION FORMULATION

$x_1$: stir-fry (oz); $x_2$: boba (fl oz).

$\mathrm{x}\backslash\mathrm{in}\backslash\mathrm{mathbb}\{R\}_{\mathrm{\{}geq0}}\mathrm{\wedge2}$

Diet Problem $$\begin{aligned}

\min_{\{\mathbf{x}\}} \& \&

\mathbf{c}^{\wedge} \mathbf{T} \mathbf{x} \\\mathbf{A} \mathbf{x} \mathbf{A} \mathbf{x} \

\mathbf{b} \\\mathbf{b} \\\mathbf{q} \

\mathbf{x} \\\mathbf{q} \

\mathbf{q} \

\mathbf{0}

\end{aligned}

\end{aligned}

$$A=\begin{cases}bmatrix}-100 & -50 \\ 100 & 50\end{cases}3 & 4

\\ -20 & -70\end{bmatrix} ~~

b=\begin{bmatrix}-2000 \ \ 2500 \ \ 100 \ \

-700\end{bmatrix}

{\rm{\sim and~}}~c=\begin{bmatrix}1\ \\\end{bmatrix}

0.4\end{bmatrix}$

# SOLVING AN LP

For a nonempty, bounded feasible polyhedron, at least one optimal solution is a vertex.

For this diet model, the optimal vertex is unique.

In two dimensions, a vertex is a feasible intersection of independent constraint boundaries.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2F4b07c7a6b50645f6a26297e1c1b51f6e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=cpfOPQHA9jW4NYqXwx9trup%2BIDo%3D)

# DIET PROBLEM: OPTIMAL SOLUTION

The calorie lower bound and sugar upper bound are binding:

$$\begin{aligned}

100x_{1}+50x_{2}+2000,\backslash 3x_{1}+4x_{2}+100.\\

\end{aligned}

end{aligned}$

Unique optimum: $(x_{1}, x_{2})=(12, 16)$

12 oz stir-fry and 16 fl oz boba.

Minimum cost: 18.4 units

$12+0.4(16)=18.4$.

The vertices cost $19.5$, $24$, and $24\frac{frac}{2}$

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2Fc2f1910be8444f23a0b757410a5cab44.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=HS7JYIRrIWSQA6X%2BMpuW%2FOCtZE0%3D)

POSSIBLE LP OUTCOMES

<table><tr><td>Outcome</td><td>Example</td><td>Meaning</td></tr><tr><td>Finite optimum</td><td>$\min x$ subject to $x\geq0$</td><td>Optimal value $0$ at $x=0$</td></tr><tr><td>Infeasible</td><td>$\min x$ subject to $x\geq0$</td><td>No point satisfies all constraints</td></tr><tr><td>Unbounded objective</td><td>$\min -x$ subject to $x\geq0$</td><td>The objective can decrease without limit</td></tr></table>

An unbounded feasible region can still have a finite optimum, as in the first example.

# ALGORITHMS AND INTEGER DECISIONS

Simplex: moves between adjacent feasible vertices, seeking a better objective value.

Interior-point methods: approach an optimum through the interior.

Requiring integer decisions gives an integer program. Rounding an LP solution may be infeasible or suboptimal.

Branch and bound: uses LP relaxations to bound and prune a search tree.

Open graphical LP and integer-programming demonstrations →

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

WHY IS THERE PHEMOUS

WHY ARE THERE SO MANY CROWS IN ROCHESTER, MIN

WHY ARE MY EARS RINGING

WHY DO CHILDREN GET CANCER

WHY DO POSEIDON ANGRY WITH ODYSSEUS

WHY IS THERE ICE IN SPACE

WHY ARE THERE MUSTACHS ON CLOTHES WHY ARE THERE MUSTACHS ON CARS WHY ARE THERE MUSTACHS EVERYWHERE WHY ARE THERE SO MANY BIRDS IN OHIO WHY IS THERE SO MUCH RAIN IN OHIO WHY IS OHIO WEATHER SO WEIRD WHY IS EARTH TILTED WHY IS SPACE BLACK WHY IS OUTER SPACE SO COLD WHY ARE THERE PYRAMIDS ON THE MOON WHY IS NASA SHUTTING DOWN

WHY ARE THERE MALE AND FEMALE BIKES ☎ WHY ARE THERE BRIDESMIPIDS WHY ARE THERE TINY SPIDERS IN MY HOUSE WHY ARE NOT THERE VARDOSE ARIDRES WHY ARE OLD RUNSIONS DIFFERENT

WHY ARE THERE

SQUIRRELS

WHY ARE THERE HUGE SPIDERS IN MY HOUSE

WHY ARE THERE LOTS OF SPIDERS IN MY HOUSE

WHY ARE THERE SPIDERS IN MY ROOM

WHY ARE THERE SO MANY SPIDERS IN MY ROOM

WHY DO SPIDER BITES ITCH

WHY IS DYING SO SCARY

WHY IS PROGRAMMING SO HARD WHY AREN'T THERE E GRADES WHY THERE A O CHM REGARD WHY DO AMERICANS HATE SOCDER WHY DO BOYS LIKE ME WHY DO TREES DIE WHY DON'T BOYS LIKE ME WHY IS THERE NO SOUND ON ON WHY IS THERE, ALWAYS A JAMA UPDATE WHY AREN'T POKEMON REAL WHY ARE THERE RED DOTS ON MY THIGHS WHY AREN'T BULLETS SHARP WHY IS LYING GOOD WHY IS SEX SO IMPORTANT

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2Fc9b5eb0e4d364eab8e3467b56137d385.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=9eW4kd%2B%2F9escFL3D3aSxMyQNKqE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2F48582622f30e4ba6bb9de709f3ca9ff0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=QiorC7D2FXMvHa4DszxvwGN7Zw4%3D)

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

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2Fbb81e57b03494bdfba44c5d7a2f4290d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=Wwe36TP59n4hu5gMXqdeLy6OU28%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2Fca4a7ab096f94120b93cb486542b501c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090139&Signature=RQwwrl7r3M86WylgZwOKst00zpI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F90b26bb9e7574a7babf3f3eac4c74fe4%2Fmedia%2Fcd01209b0940451884ed0ded2f6927ba.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800090140&Signature=HK%2FdwnDuG6lASC6VH1AMwdjXiF4%3D)
