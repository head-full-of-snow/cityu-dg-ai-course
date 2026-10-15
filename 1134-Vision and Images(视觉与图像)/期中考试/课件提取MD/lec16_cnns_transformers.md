# lec16_cnns_transformers

> PyMuPDF 文本层提取；公式为图形对象无法直接提取，
> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。

## Slide 1

CS5 8
s o
a d
age: Neu a
Network

## Slide 2

Outline
●Deep Learning
○
RNN
○
CNN
○
Attention
○
Transformer

## Slide 3

RNNs
Some slides borrowed from Fei-Fei Li & Justin
Johnson & Serena Yeung at Stanford.

## Slide 4

Vanilla Neural Networks
Input
Output
Hidden
Layers
Input
Output
Hidden
Layers
House Price Prediction

## Slide 5

How to model sequences?
●Text Classification: Input Sequence -> Output label
●Translation: Input Sequence -> Output Sequence
●Image Captioning: Input image -> Output Sequence

## Slide 6

RNN- Recurrent Neural Networks
Vanilla
Neural
Networks
e.g.- Image
Captioning
e.g.- Text
Classification
e.g.-
Translation
e.g.- POS
tagging

## Slide 7

RNN- Representation
Input Vector
Output Vector
Hidden state fed back
into the RNN cell

## Slide 8

RNN- Recurrence Relation
Input Vector
Output Vector
Hidden state fed back
into the RNN cell
The RNN cell consists of a hidden state that is updated
whenever a new input is received. At every time step,
this hidden state is fed back into the RNN cell.

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

RNN 循环关系【标准形式】：

$$h_t = \tanh\big(W_{hh}h_{t-1} + W_{xh}x_t\big), \qquad y_t = W_{hy}h_t$$

隐状态每步更新并反馈回 cell；所有时间步共享同一组权重 $W$。
## Slide 9

RNN- Rolled out representation

## Slide 10

RNN- Rolled out representation
Same Weight
matrix- W
Individual Losses Li

## Slide 11

RNN- Backpropagation Through Time
Forward pass through entire sequence to produce intermediate hidden states, output sequence and finally
the loss. Backward pass through the entire sequence to compute gradient.

## Slide 12

RNN- Backpropagation Through Time
Running Backpropagation through time for the entire text would be very slow. Switch to an approximation-
Truncated Backpropagation Through Time

## Slide 13

RNN- Truncated Backpropagation Through Time
Run forward and backward
through chunks of the
sequence instead of whole
sequence

## Slide 14

RNN- Truncated Backpropagation Through Time
Carry hidden states forward
in time forever, but only
backpropagate for some
smaller number of steps

## Slide 15

RNN- Types
The 3 most common types of Recurrent Neural Networks are-
1.
Vanilla RNN
2.
LSTM (Long Short-Term Memory)
3.
GRU (Gated Recurrent Units)
Some good resources-
Understanding LSTM Networks
An Empirical Exploration of Recurrent Network Architectures
Recurrent Neural Network Tutorial, Part 4 – Implementing a GRU/LSTM RNN with Python and Theano
Stanford CS231n: Lecture 10 | Recurrent Neural Networks

## Slide 16

CNNs
Some slides borrowed from Fei-Fei Li & Justin
Johnson & Serena Yeung at Stanford.

## Slide 17

Fully Connected Layer
Input
32x32x3 image
Flattened image
32*32*3 = 3072
Weight Matrix
Output

## Slide 18

Convolutional Layer
Input
32x32x3 image
Filter
5x5x3
Convolve the filter with the image i.e.
“slide over the image spatially,
computing dot products”
Filters always extend the full depth of
the input volume.

## Slide 19

Convolutional Layer
At each step during the
convolution, the filter acts on a
region in the input image and
results in a single number as
output.
This number is the result of the
dot product between the values
in the filter and the values in the
5x5x3 chunk in the image that
the filter acts on.
Combining these together for the
entire image results in the
activation map.

## Slide 20

Convolutional Layer
Filters can be stacked together.
Example- If we had 6 filters of
shape 5x5,
each would produce an
activation map of 28x28x1 and
our output would be a “new
image” of shape 28x28x6.

## Slide 21

Convolutional Layer
Visualizations borrowed from Irhum Shafkat’s blog.

## Slide 22

Convolutional Layer
Visualizations borrowed from vdumoulin’s github repo.
Standard
Convolution
Convolution
with Padding
Convolution
with strides

## Slide 23

Convolutional Layer
Output Size:
(N - F)/stride + 1
e.g. N = 7, F = 3, stride 1
=> (7 - 3)/1 + 1 = 5
e.g. N = 7, F = 3, stride 2
=> (7 - 3)/2 + 1 = 3

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

卷积层输出尺寸：

$$\text{Output} = \frac{N - F}{\text{stride}} + 1$$

例：$N=7, F=3$, stride 1 $\Rightarrow 5$；stride 2 $\Rightarrow 3$。
## Slide 24

Pooling Layer
●makes the
representations smaller
and more manageable
●operates over each
activation map
independently

## Slide 25

Max Pooling

## Slide 26

ConvNet Layer
Image credits- Saha’s blog.

## Slide 27

ConvNet Layer
Image credits- Saha’s blog.

## Slide 28

Attention
Some slides borrowed from Sarah Wiegreffe
at Georgia Tech.

## Slide 29

RNN

## Slide 30

RNN - Attention

## Slide 31

RNN - Attention

## Slide 32

RNN - Attention

## Slide 33

RNN - Attention

## Slide 34

RNN - Attention

## Slide 35

RNN - Attention

## Slide 36

RNN - Attention

## Slide 37

RNN - Attention

## Slide 38

RNN - Attention

## Slide 39

Attention

## Slide 40

（纯图片页，无文本层）

## Slide 41

Drawbacks of RNN

## Slide 42

Transformer
Some slides borrowed from Sarah Wiegreffe
at Georgia Tech.

## Slide 43

Transformer

## Slide 44

Self-Attention

> 【公式·人工补全】以下公式为幻灯片中的图形公式（PyMuPDF 文本层不可见），已对照幻灯片渲染图人工核对转录：

自注意力【标准公式，幻灯片为示意图】：

$$\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^{\mathsf T}}{\sqrt{d}}\right)V$$

（Q=query, K=key, V=value；多头 = 多组 QKV 并行再拼接。）
## Slide 45

Self-Attention

## Slide 46

Self-Attention

## Slide 47

Self-Attention

## Slide 48

Multi-Head Self-Attention

## Slide 49

Retaining Hidden State Size

## Slide 50

Details of Each Attention Sub-Layer of Transformer
Encoder

## Slide 51

Each Layer of Transformer Encoder

## Slide 52

Positional Encoding

## Slide 53

Each Layer of Transformer Decoder

## Slide 54

Transformer Decoder - Masked Multi-Head Attention
Problem of Encoder self-attention: we can’t see the future !

## Slide 55

Transformer
