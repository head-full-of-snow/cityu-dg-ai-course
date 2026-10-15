# CityU CS5491 Linear Programming Tutorial

Feb 20 $ ^{th} $, 2025

# Objectives

After studying this tutorial material $ ^{1} $, you should:

• be able to formulate linear programming problems from contextual problems.

• be able to identify feasible regions for linear programming problems.

• be able to find solutions to linear programming problems using graphical means.

# 1 Introduction

The methods of linear programming were originally developed between 1945 and 1955 by American mathematicians to solve problems arising in industry and economics planning. Many such problems involve constraints on the size of the workforce, the quantities of raw materials available, the number of machines available, and so on. The problems that will be solved usually have two variables (i.e., unknowns) in them and can be solved graphically, but problems occurring in the industry have many more variables and have to be solved by computer algorithms. For example, in oil refineries, problems arise with hundreds of variables and tens of thousands of constraints.

Undoubtedly linear programming is one of the most widespread methods used to solve management and economic problems and has been applied in a wide variety of situations and contexts in the broad scope of AI.

# 2 Formulation

You are now in a position to use your knowledge of constraints from week 3's lecture on Constraint Satisfaction to illustrate linear programming with the following case study.

Suppose a manufacturer of printed circuits has a stock of

200 resistors, 120 transistors, and 150 capacitors

and is required to produce two types of circuits.

• Type A requires 20 resistors, 10 transistors, and 10 capacitors.

• Type B requires 10 resistors, 20 transistors, and 30 capacitors.

If the profit on Type A circuits is $5 and that on Type B circuits is $12, how many of each circuit should be produced in order to maximize the profit?

$ ^{1} $Credits to Center for Innovation in Mathematics Teaching.

You will not actually solve this problem yet, but show how it can be formulated as a linear programming problem. There are three vital stages in the formulation, namely

(a) What are the variables (i.e., unknowns)?

(b) What are the constraints?

(c) What is the profit/cost to be maximized/minimized?

For this problem,

**(a) What are the variables (i.e., unknowns)?**

Clearly the number of Type A and Type B circuits produced; so we define

$ x = \text{number of Type A circuits produced} $

y = number of Type B circuits produced

**(b) What are the constraints?**

There are constraints associated with the total number of resistors, transistors, and capacitors available.

Resistors Since each Type A requires 20 resistors, and each Type B requires 10 resistors, then  $ 20x + 10y \leq 200 $, as there is a total of 200 resistors available.

Transistors similarly

$$ 10x+20y\leq120, $$

Capacitors similarly

$ 10x + 30y \leq 150, $

Finally you must state the obvious (but nevertheless important) inequalities

$$ x\geq0,y\geq0\text{and}x,y\in\mathbb{Z} $$

In this particular example, you should be aware that x and y can only be integers since it is not sensible to consider fractions of a printed circuit, i.e.,  $ x, y \in Z $.

**(c) What is the profit/cost to be maximized/minimized?**

Since each Type A gives $5 profit and each Type B gives $12 profit, the total profit is $P, where

$$ P=5x+12y $$

You can now summarize the problem as:

<table><tr><td>maximize</td><td>$ P = 5x + 12y $</td></tr><tr><td>subject to</td><td>$ 20x + 10y ≤ 200 $</td></tr><tr><td></td><td>$ 10x + 20y ≤ 120 $</td></tr><tr><td></td><td>$ 10x + 30y ≤ 150 $</td></tr><tr><td></td><td>$ x ≥ 0, y ≥ 0 $ and  $ x, y \in \mathbb{Z} $</td></tr></table>

This is called a linear programming problem since both the objective function P and the constraints are all linear in variables x and y.

The key stage is the first one, namely that of identifying the unknowns (i.e., variables); so you must carefully read the problem through in order to identify the basic unknowns. Once you have done this successfully, it should be straightforward to express both the constraints and the profit function in terms of the unknowns.

Before proceeding with finding the actual solutions, you will concentrate further practice in formulating problems of this type.

**Example Exercise**

A small firm builds two types of garden sheds.

• Type A requires 2 hours of machine time and 5 hours of craftsman time.

• Type B requires 3 hours of machine time and 5 hours of craftsman time.

Each day there are 30 hours of machine time available and 60 hours of craftsman time. The profit on each Type A shed is $60 and on each Type B shed is $84.

Formulate the appropriate linear programming problem.

Solution

(a) Unknowns

(c) Profit

So, in summary, the linear programming problem is

# 3 Graphical Solution

In the previous section, you worked through problems that led to a linear programming problem in which a linear function of x and y is to be maximized (or minimized) subject to a number of linear inequalities to be satisfied.

Fortunately, as we have seen in the class, problems of this type with just two variables can easily be solved using a graphical method. The method will be first illustrated using the example from the previous section, namely

$$ \begin{array}{r l}{\mathrm{m a x i m i z e}}&{{}\qquad P=5x+12y}\end{array} $$

$$ \begin{array}{r l r}{\mathrm{s u b j e c t~t o~}}&{{}}&{20x+10y\leq200}\end{array} $$

$$ 10x+20y\leq120 $$

$$ 10x+30y\leq150 $$

$$ x\geq0,y\geq0\text{and}x,y\in\mathbb{Z} $$

You can illustrate the feasible (i.e., allowable) region by graphing all the inequalities and shading out the regions not allowed. This is illustrated in the figure below.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2297a8877fec4c7988f183c06564d81b%2Fmedia%2Faef5b655ec78438a98de78427539363b.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799742268&Signature=lIdM4Xn8obl1djbVPxblDWd4pPI%3D)

Magnifying the feasible region, you can look at the family of straight lines defined by

$$ C=5x+12y $$

where C takes various values.

The figure shows, for example, the lines defined by

$$ C=15,C=30,C=45. $$

Any point on each of these lines gives the same profit.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2297a8877fec4c7988f183c06564d81b%2Fmedia%2Fb06d32c6a93d4198985ff3ea3b9a44d0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799742268&Signature=kU3dwBZtjba1bNZv2K2OL3T0vxY%3D)

**Where is the point representing maximum profit?**

As the profit line moves to the top right corner, the profit increases and so the maximum profit corresponds to the last point touched as the profit line moves out of the feasible region. This is the point B, the intersection of

$$ 10x+30y=150\  and \ 10x+20y=120 $$

Solving these equations gives 10y = 30, i.e., y = 3 and x = 6. So maximum profit occurs at the point (6, 3) and the profit is given by

$$ P=5\times6+12\times3=66. $$

**Example Exercise**

A farmer has 20 hectares for growing barley and swedes. The farmer has to decide how much of each to grow. The cost per hectare for barley is $30 and for swedes is $20. The farmer has budgeted $480.

Barley requires 1 man-day per hectare and swedes require 2 man-days per hectare. There are 36 man-days available.

The profit on barley is $100 per hectare and on swedes is $120 per hectare.

Find the number of hectares of each crop the farmer should sow to maximize profit.

**Solution**

The problem is formulated as a linear programming problem:

(a) Unknowns

(b) Constraints

(c) Profit

So, in summary, the linear programming problem is

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F2297a8877fec4c7988f183c06564d81b%2Fmedia%2Ff05b5f93d71449368be2fe2964e1cd1f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799742268&Signature=pHTenL3Cex0PyPmlNysx24GL1G4%3D)
