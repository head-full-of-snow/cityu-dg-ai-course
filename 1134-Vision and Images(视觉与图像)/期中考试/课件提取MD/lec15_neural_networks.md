# lec15_neural_networks

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

Neural networks
CS5187: Computer Vision

## Slide 2

• Input: an image
• Assume it is of fixed size, e.g. 128x128
pixels
• Output: the class label for that image
• Label is generally a discrete label from a
pre-defined set
• e.g. {cat, dog, cow, toaster, apple, tomato,
truck, … }
New problem: Image classification
def classifier(image):
//Do some stuff
return class_label;
“Toaster”
“Cat”
“Dog”

## Slide 3

Image classification demo
https://cloud.google.com/vision/docs/drag-and-drop
See also:
https://aws.amazon.com/rekognition/
https://www.clarifai.com/
https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/
…

## Slide 4

The Semantic Gap
What we see
What the computer sees

## Slide 5

• The same class of object
can appear very
differently in different
images
Variation Makes Recognition Hard
Viewpoint Variation
Lighting Variation
Deformation
Background Clutter
Occlusion

## Slide 6

• Distinct realities can produce the same
image…
• We generally can’t compute the “right”
answer, but we can compute the most
likely one…
• We need some kind of prior to condition
on. We can learn this prior from data:
The Problem is Under-constrained
I think there may be
a spy among us…

## Slide 7

• An image is just a bunch of numbers
• Let’s stack them up into a vector
• Our training data is just a bunch of
high-dimensional points now
Images As High-Dimensional Vectors
The Space of
All Images

## Slide 8

Toasters
Cats
• An image is just a bunch of numbers
• Let’s stack them up into a vector
• Our training data is just a bunch of
high-dimensional points now
• Divide space into different regions
for different classes
Images As High-Dimensional Vectors
The Space of
All Images

## Slide 9

Toasters
Cats
• An image is just a bunch of numbers
• Let’s stack them up into a vector
• Our training data is just a bunch of
high-dimensional points now
• Divide space into different regions
for different classes
Images As High-Dimensional Vectors
The Space of
All Images

## Slide 10

• Define a distribution over
space for each class
• An image is just a bunch of numbers
• Let’s stack them up into a vector
• Our training data is just a bunch of
high-dimensional points now
• Divide space into different regions
for different classes
Images As High-Dimensional Vectors
The Space of
All Images
Toasters
Cats

## Slide 11

• How high-dimensional is an image?
• Let’s consider an iPhone X photo:
• 4032 x 3024 pixels
• Every pixel has 3 colors
• 36,578,304 pixels (36.5 Mega pixels)
• In practice, images sit on a lower-
dimensional manifold
• Think of image features and
dimensionality reduction as ways to
represent images by their location on
such manifolds
Image Features and Dimensionality Reduction
The Space of
All Images

## Slide 12

Side Note:
This also lets us deal with images
of different sizes, crops, etc.
Image Features and Dimensionality Reduction
• How high-dimensional is an image?
• Let’s consider an iPhone X photo:
• 4032 x 3024 pixels
• Every pixel has 3 colors
• 36,578,304 pixels (36.5 Mega pixels)
• In practice, images sit on a lower-
dimensional manifold
• Think of image features and
dimensionality reduction as ways to
represent images by their location on
such manifolds

## Slide 13

• Collect a database of images with labels
• Use ML to train an image classifier
• Evaluate the classifier on test images
Training & Testing a Classifier
Slide from Andrej Karpathy and Fei-Fei Li   http://vision.stanford.edu/teaching/cs231n/

## Slide 14

Training & Testing a Classifier

## Slide 15

Training & Testing a Classifier

## Slide 16

• Nearest Neighbor
• kNN  (“k-Nearest Neighbors”)
• Linear Classifier
• Neural Network
• Deep Neural Network
• Transformers
• …
Classifiers

## Slide 17

• Nearest Neighbor
• kNN  (“k-Nearest Neighbors”)
• Linear Classifier
• Neural Network
• Deep Neural Network
• Transformers
• …
Classifiers

## Slide 18

Linear Classifiers

## Slide 19

• Linear Classifier
• Store hyperplanes that best
separate different classes
• We can compute continuous
class score by calculating (signed)
distance from hyperplane
Linear Classification vs. Nearest Neighbors
We can interpret this as a linear
"score function” for each class.

## Slide 20

Score functions
Slide adapted from Andrej Karpathy and Fei-Fei Li http://vision.stanford.edu/teaching/cs231n/

## Slide 21

Parametric Approach
Slide adapted from Andrej Karpathy and Fei-Fei Li http://vision.stanford.edu/teaching/cs231n/

## Slide 22

Parametric Approach: Linear Classifier
Slide adapted from Andrej Karpathy and Fei-Fei Li http://vision.stanford.edu/teaching/cs231n/

## Slide 23

Parametric Approach: Linear Classifier
Slide adapted from Andrej Karpathy and Fei-Fei Li http://vision.stanford.edu/teaching/cs231n/

## Slide 24

Linear Classifier
Slide adapted from Andrej Karpathy and Fei-Fei Li http://vision.stanford.edu/teaching/cs231n/

## Slide 25

Interpretation: Algebraic
Slide adapted from Andrej Karpathy and Fei-Fei Li http://vision.stanford.edu/teaching/cs231n/

## Slide 26

• Parameters define a hyperplane
for each class:
• We can think of each class score as
defining a distribution that is
proportional to distance from the
corresponding hyperplane
Interpretation: Geometric
The Space of
All Images

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

线性分类器几何观点：每类参数定义一张超平面，分数 = 到超平面的（带符号）距离：

$$f(x, W, b) = Wx + b$$
## Slide 27

Hard Cases for a Linear Classifier

## Slide 28

• We can think of the rows in         as templates for each class
Interpretation: Template matching
Rows of W in

## Slide 29

Linear Classifier: Three Viewpoints

## Slide 30

So far: Defined a (linear) score function f(x, W) = Wx + b

## Slide 31

Linear classification
Output scores

## Slide 32

Loss functions

## Slide 33

• Given ground truth labels (yi), scores f(xi, W)
• how unhappy are we with the scores?
• Loss function or objective/cost function measures unhappiness
• During training, want to find the parameters W that minimize the
loss function
Loss function, cost/objective function

## Slide 34

• Two classes (e.g., “cat” and “not cat”)
• AKA “positive” and “negative” classes
Simpler example: binary classification
cat
not cat

## Slide 35

0
:
negative
0
:
positive






b
b
i
i
i
i
w
x
x
w
x
x
Linear classifiers
Which hyperplane is best? We
need a loss function to decide
• Find linear function (hyperplane) to
separate positive and negative
examples

## Slide 36

• One possibility: Number of misclassified examples
• Problems: discrete, can’t break ties
• We want the loss to lead to good generalization
• We want the loss to work for more than 2 classes
What is a good loss function?
Loss: 2
Loss: 0
Loss: 0

## Slide 37

• Interpret Scores as
unnormalized log
probabilities of classes
Softmax classifier
Squashes values into probabilities
ranging from 0 to 1
(score function)
Example with three classes:

## Slide 38

Softmax classifier
0.06
0.82
0.12
Softmax
“probabilities”

## Slide 39

Cross-entropy loss
(score function)
We call Li cross-
entropy loss

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

Softmax 分类器：把分数解释为未归一化对数概率：

$$p_i = \frac{e^{s_i}}{\sum_j e^{s_j}}, \qquad P(y_i\mid x_i; W) = \frac{e^{s_{y_i}}}{\sum_j e^{s_j}}$$
## Slide 40

Cross-entropy loss
(score function)
We call Li cross-
entropy loss
fyi  : score of correct class

## Slide 41

Cross-entropy loss
(score function)
We call Li cross-
entropy loss

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

交叉熵损失：

$$L_i = -\log\!\left(\frac{e^{s_{y_i}}}{\sum_j e^{s_j}}\right) = -s_{y_i} + \log\sum_j e^{s_j}$$

（最小化负对数似然。）
## Slide 42

• Cross-entropy loss is just one possible loss function
• One nice property is that it reinterprets scores as probabilities, which have a natural
meaning
• SVM (max-margin) loss functions also used to be popular
• But currently, cross-entropy is the most common classification loss
Losses

## Slide 43

The story so far: linear classification
• What we have: a score function and loss function
– Score function maps an input data instance (e.g., an image) to a
vector of scores, one for each category
– Last time, our score function is based on linear classifier
• Find W and b that minimize a loss over labeled training data,
e.g. cross-entropy loss
f:  score function
x: input instance
W, b: parameters of a linear (actually affine) function

## Slide 44

Questions?

## Slide 45

Neural networks
Slide credit: Fei-Fei Li & Andrej Karpathy & Serena Leung

## Slide 46

Neural networks
Slide credit: Fei-Fei Li & Andrej Karpathy & Serena Leung

## Slide 47

Neural networks
(100 x 3072 matrix)
(10 x 100 matrix)
100D intermediate
vector
Slide credit: Fei-Fei Li & Andrej Karpathy & Serena Leung

## Slide 48

Neural networks
• Total number of weights to learn:
3,072 x 100 + 100 x 10 = 308,200
Adapted from Fei-Fei Li & Andrej Karpathy & Serena Leung

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

两层神经网络（隐层 100，输入 3072 维，输出 10 类）：

$$f = W_2\max(0, W_1 x)$$

权重总数 $= 3072\times100 + 100\times10 = 308{,}200$。
## Slide 49

Neural networks
also called “Multilayer
Perceptrons” (MLPs)
Adapted from Fei-Fei Li & Andrej Karpathy & Serena Leung

## Slide 50

Neural networks
• Very coarse generalization of neural networks:
– Linear functions chained together and separated by non-
linearities (activation functions), e.g. “max”
– Why separate linear functions with non-linear functions?
– Very roughly inspired by real neurons

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

深度网络 = 线性层与非线性激活交替串联：

$$f = W_3\max\big(0,\ W_2\max(0, W_1 x)\big)$$

（去掉非线性则整体退化为线性。）
## Slide 51

Neural network architecture
• Computation graph for a 2-layer neural
network
Neuron or unit
Adapted from Fei-Fei Li & Andrej Karpathy & Serena Leung

## Slide 52

• Deep networks typically have many layers and potentially
millions of parameters
Adapted from Fei-Fei Li & Andrej Karpathy & Serena Leung
Neural networks: architectures

## Slide 53

Deep neural network
• Inception network (Szegedy et al, 2015)
• 22 layers
Adapted from Fei-Fei Li & Andrej Karpathy & Serena Leung

## Slide 54

• Just like a linear classifer – but in this case, just one layer of
a larger network
Adapted from Fei-Fei Li & Andrej Karpathy & Serena Leung

## Slide 55

Summary so far
• A classic neural network arranges neurons into fully-
connected layers. This kind of neural network is also called a
Multi-Layer Perceptron
• The layer abstraction enables efficient implementations of
neural networks using vectorized operations like matrix
multiplication
Adapted from Fei-Fei Li & Andrej Karpathy & Serena Leung

## Slide 56

Optimizing parameters with gradient descent
• How do we find the best W and b parameters?
• In general: gradient descent
1.
Start with a guess of a good W and b (or randomly initialize them)
2.
Compute the loss function for this initial guess and the gradient of the
loss function
3.
Step some distance in the negative gradient direction (direction of
steepest descent)
4.
Repeat steps 2 & 3
•
Note: efficiently performing step 2 for deep networks is called
backpropagation

## Slide 57

Gradient descent: walk in the direction opposite gradient
•
Q: How far?
•
A: Step size: learning rate
•
Too big: will miss the minimum
•
Too small: slow convergence

## Slide 58

2D example of gradient descent
• In reality, in deep learning
we are optimizing a highly
complex loss function with
millions of variables (or
more)
• More on this later…
https://laptrinhx.com/gradient-descent-animation-2-multiple-linear-regression-3070246823/

## Slide 59

2D example: TensorFlow Playground
https://playground.tensorflow.org

## Slide 60

Questions?

## Slide 61

Multi-layer perceptrons: just the beginning
• MLPs can work well with simple image classification problems
(e.g., digit recognition)
• For more complex recognition problems (e.g., recognizing
1,000s of categories), we need more technology
(convolutional neural networks and transformers)
• MLPs have a surprising application: 3D reconstruction!
– See NeRFs (neural radiance fields) next time
