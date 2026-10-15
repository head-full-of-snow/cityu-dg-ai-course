# Tutorial 1 学习指南（双语） / Study Guide (Bilingual)

## 1. 作业主题 / Assignment Topic

**Tutorial 1: Text Document Classification with KNN and Naive Bayes**

**教程 1：使用 KNN 和朴素贝叶斯进行文本分类**

## 2. 学习目标 / Learning Objectives

通过这份作业，你需要掌握文本分类中的基础流程，包括数据加载、文本特征提取、模型训练、效果比较和结果分析。

Through this assignment, you are expected to understand the basic workflow of text classification, including data loading, text feature extraction, model training, performance comparison, and result analysis.

完成本作业后，你应当能够：

After finishing this assignment, you should be able to:

1. 理解 `20 Newsgroups` 数据集的基本结构。  
   Understand the basic structure of the `20 Newsgroups` dataset.
2. 使用词袋模型（Bag of Words）表示文本。  
   Represent text with the Bag-of-Words model.
3. 使用 `TF-IDF` 提升文本特征的区分能力。  
   Use `TF-IDF` to improve feature discrimination.
4. 训练并比较 `KNN`、`Bernoulli Naive Bayes` 和 `Multinomial Naive Bayes`。  
   Train and compare `KNN`, `Bernoulli Naive Bayes`, and `Multinomial Naive Bayes`.
5. 分析参数变化对分类准确率的影响。  
   Analyze how parameter changes affect classification accuracy.

## 3. 文件说明 / Files in This Assignment

当前目录中的主要文件如下：

The main files in the current directory are:

- `Tutorial1.ipynb`  
  已运行版本，包含结果输出和图表。  
  The executed version, including outputs and plots.

- `Tutorial1_bilingual.ipynb`  
  未运行的中英双语 notebook，适合重新运行或作为提交版本。  
  The unrun bilingual notebook, suitable for re-execution or submission.

- `20news-bydate_py3.pkz`  
  数据文件，必须与 notebook 放在同一目录，并且不要解压。  
  The dataset file. It must stay in the same folder as the notebook and should not be unzipped.

## 4. 建议学习顺序 / Recommended Study Order

建议按下面的顺序学习这份作业：

It is recommended to study this assignment in the following order:

1. 先阅读数据加载部分，确认分类任务和类别名称。  
   First read the data loading section and confirm the task and class names.
2. 再看文本表示部分，理解 `CountVectorizer` 和 `TF-IDF` 的区别。  
   Then review the text representation section and understand the difference between `CountVectorizer` and `TF-IDF`.
3. 接着看 KNN 模型结果，体会传统距离方法在高维文本上的局限。  
   Next, check the KNN results to see the limitation of distance-based methods on high-dimensional text data.
4. 然后比较两种朴素贝叶斯模型的表现和关键词。  
   Then compare the two Naive Bayes models and their informative words.
5. 最后查看 `alpha` 和 `vocabulary size` 两部分图像，理解参数敏感性。  
   Finally, examine the `alpha` and `vocabulary size` plots to understand parameter sensitivity.

## 5. 基础知识解读 / Foundational Concepts Explained

### 5.1 什么是文本分类 / What Is Text Classification

文本分类的目标是：给定一段文本，让模型自动判断它属于哪个类别。

The goal of text classification is: given a piece of text, let the model automatically decide which category it belongs to.

在这份作业中，输入是新闻组帖子文本，输出是 4 个类别之一：

In this assignment, the input is a newsgroup post and the output is one of four classes:

- `alt.atheism`
- `talk.religion.misc`
- `comp.graphics`
- `sci.space`

这属于**监督学习**，因为训练数据里已经给出了正确标签。

This is a form of **supervised learning**, because the correct labels are already provided in the training data.

### 5.2 训练集与测试集 / Training Set and Test Set

训练集用于让模型学习规律，测试集用于检验模型在“没见过的新数据”上的效果。

The training set is used to learn patterns, while the test set is used to evaluate performance on unseen data.

如果一个模型在训练集上很好、在测试集上很差，通常说明它可能**过拟合**了。

If a model performs very well on the training set but poorly on the test set, it often indicates **overfitting**.

### 5.3 为什么文本要先变成数字 / Why Text Must Be Converted into Numbers

大多数机器学习模型不能直接理解自然语言字符串，它们只能处理数值向量。

Most machine learning models cannot directly understand raw text strings; they can only work with numerical vectors.

因此，我们需要先把句子或文档转换成数字表示。

Therefore, we first need to convert a sentence or document into a numerical representation.

### 5.4 One-hot、词袋模型与 TF-IDF 的区别 / Differences Among One-hot, Bag of Words, and TF-IDF

**One-hot 编码**的特点是：每个词对应一个位置，出现哪个词，就把对应位置标为 1。

**One-hot encoding** works by assigning one position to each word; if a word appears, its position is marked as 1.

它适合帮助理解“如何把词变成向量”，但如果词汇表很大，向量会非常稀疏，也很难直接表达词频信息。

It is useful for understanding how words become vectors, but when the vocabulary is large, the vectors become extremely sparse and do not directly express word frequency well.

**词袋模型（Bag of Words）**进一步改进为：不只记录有没有出现，还记录每个词出现了多少次。

**Bag of Words** improves this by recording not only whether a word appears, but also how many times it appears.

它忽略词序，但保留了词频，因此在许多基础文本分类任务中非常实用。

It ignores word order but keeps word frequency, which makes it very practical for many basic text classification tasks.

**TF-IDF** 则是在词频基础上再加权：

**TF-IDF** adds weighting on top of raw term frequency:

- 如果一个词在某篇文档中出现很多次，它的 `TF` 较高。  
  If a word appears many times in one document, its `TF` is high.
- 如果一个词在几乎所有文档中都很常见，它的区分能力就不强，因此 `IDF` 会压低它的权重。  
  If a word is common in almost all documents, it is less discriminative, so `IDF` reduces its weight.

因此，TF-IDF 更强调“哪些词更能代表当前文档的类别特征”。

So TF-IDF emphasizes which words are more representative of the current document's category.

### 5.5 停用词是什么 / What Are Stop Words

停用词是指像 `the`、`is`、`and` 这类在很多文本里都频繁出现、但通常区分能力较弱的词。

Stop words are words like `the`, `is`, and `and`, which appear frequently in many texts but usually have weak discriminative power.

在本作业中使用 `stop_words='english'`，就是为了减少这类词对模型的干扰。

In this assignment, `stop_words='english'` is used to reduce the interference caused by such words.

### 5.6 KNN 的基础思想 / The Basic Idea of KNN

KNN 的核心思想很直观：一个新样本通常更像它附近的样本。

The core idea of KNN is intuitive: a new sample is usually similar to the samples near it.

做预测时，KNN 会：

When making a prediction, KNN:

1. 计算测试样本与训练样本之间的距离。  
   Computes the distance between the test sample and training samples.
2. 找出最近的 `K` 个邻居。  
   Finds the nearest `K` neighbors.
3. 用这些邻居中出现最多的类别作为预测结果。  
   Uses the majority class among those neighbors as the prediction.

但在文本任务里，向量维度通常很高，很多词又非常稀疏，因此“距离”不一定能很好地反映语义相似性。

However, in text tasks, vectors are usually high-dimensional and sparse, so distance does not always reflect semantic similarity well.

这也是为什么 KNN 往往不如朴素贝叶斯稳定。

This is one reason KNN is often less stable than Naive Bayes in this setting.

### 5.7 什么是交叉验证 / What Is Cross-Validation

交叉验证是一种更稳健的选参方法。

Cross-validation is a more robust method for hyperparameter selection.

它会把训练集再切成若干份，轮流用一部分做验证、其余部分做训练，最后综合多轮结果来判断哪个参数更好。

It splits the training set into several parts, repeatedly using one part for validation and the others for training, then combines the results to decide which parameter is better.

本作业里，交叉验证用于给 KNN 选择更合适的 `K`。

In this assignment, cross-validation is used to choose a better value of `K` for KNN.

### 5.8 朴素贝叶斯为什么适合文本 / Why Naive Bayes Works Well for Text

朴素贝叶斯本质上是在计算：

Naive Bayes essentially computes:

“在已知这篇文本中出现了这些词的情况下，它属于某个类别的概率有多大？”

"Given the words appearing in this document, how likely is it to belong to a certain class?"

它之所以叫“朴素”，是因为它做了一个简化假设：把各个词看作在给定类别下彼此独立。

It is called “naive” because it makes a simplifying assumption: given the class, the words are treated as independent from one another.

这个假设并不完全真实，但在文本分类里经常依然有效。

This assumption is not fully true, but it still works surprisingly well in many text classification tasks.

### 5.9 Bernoulli NB 与 Multinomial NB 的区别 / Difference Between Bernoulli NB and Multinomial NB

**Bernoulli Naive Bayes** 更关注“某个词有没有出现”。

**Bernoulli Naive Bayes** focuses more on whether a word appears or not.

所以它适合二值特征，也就是把词频转成 0/1。

So it is suitable for binary features, where counts are converted into 0/1 values.

**Multinomial Naive Bayes** 更关注“某个词出现了多少次”，因此通常更适合词频型文本特征。

**Multinomial Naive Bayes** focuses more on how many times a word appears, so it is usually more suitable for count-based text features.

当它和 TF-IDF 结合时，往往能在文本分类中取得更好的效果。

When combined with TF-IDF, it often achieves better performance in text classification.

### 5.10 平滑参数 alpha 是什么 / What the Smoothing Parameter Alpha Means

`alpha` 是朴素贝叶斯里的平滑参数。

`alpha` is the smoothing parameter in Naive Bayes.

如果没有平滑，某个词一旦在某个类别中从未出现，该词对应的概率就可能变成 0，这会让整篇文档的概率计算变得很脆弱。

Without smoothing, if a word never appears in a class, its probability may become 0, making the document probability calculation fragile.

加入平滑后，即使某个词没有出现过，也会给它一个很小的非零概率。

After smoothing is added, even unseen words are assigned a small non-zero probability.

这能提升模型的稳定性，但平滑太强也可能把真正有区分度的信息“抹平”。

This improves stability, but too much smoothing can also wash out truly discriminative information.

### 5.11 词汇表大小为什么重要 / Why Vocabulary Size Matters

词汇表太小，模型会丢掉很多有用词。

If the vocabulary is too small, the model loses many useful words.

词汇表太大，又可能引入很多噪声词、稀有词，甚至增加计算负担。

If the vocabulary is too large, it may introduce noisy or very rare words and increase computation.

因此，词汇表大小通常需要通过实验来调整，而不是越大越好。

So vocabulary size usually needs to be tuned experimentally; bigger is not always better.

### 5.12 准确率与“最有信息量的词”怎么看 / How to Interpret Accuracy and Informative Words

**准确率（accuracy）** 表示预测正确的样本数占总样本数的比例。

**Accuracy** is the proportion of correctly predicted samples among all samples.

它能帮助我们快速比较模型效果，但它不能告诉我们“模型为什么这样判断”。

It helps compare model performance quickly, but it does not explain why the model made its decisions.

而“**最有信息量的词**”可以帮助我们理解：

The “**most informative words**” help us understand:

- 某个类别最依赖哪些词  
  Which words are most associated with a class
- 模型抓住的是宽泛词还是更具体的主题词  
  Whether the model captures broad markers or more specific topical words

所以在这份作业里，准确率和关键词解释应该结合起来看。

So in this assignment, accuracy and informative-word analysis should be interpreted together.

## 6. 每一部分在学什么 / What Each Part Teaches

### 6.1 数据加载 / Data Loading

这一部分帮助你熟悉文本分类任务的数据输入形式，包括：

This part helps you understand the input format of a text classification task, including:

- 文本列表 `data`  
  The text list `data`
- 类别标签 `target`  
  The class labels `target`
- 类别名称 `target_names`  
  The class names `target_names`

### 6.2 词袋模型 / Bag of Words

这一部分的重点是：

The key idea in this part is:

- 把文本转换成数值向量  
  Convert text into numerical vectors
- 每个单词用出现次数表示  
  Represent each word by its occurrence count

### 6.3 TF-IDF

这一部分帮助你理解：

This part helps you understand:

- 为什么常见词不一定有区分度  
  Why frequent words are not always discriminative
- 为什么更有代表性的词应该有更高权重  
  Why more representative words should receive higher weights

### 6.4 KNN

KNN 部分主要帮助你观察：

The KNN section helps you observe:

- 文本特征维度很高时，KNN 往往不是最优选择  
  KNN is often not the best choice when text features are high-dimensional
- 交叉验证可以帮助选择较优参数  
  Cross-validation can help select better parameters

### 6.5 Bernoulli Naive Bayes

这一部分重点在于：

The focus of this part is:

- 使用“是否出现”来建模单词特征  
  Model word features based on presence or absence
- 观察它更偏向哪些高频类别标记词  
  Observe which broad category marker words it tends to emphasize

### 6.6 Multinomial Naive Bayes + TF-IDF

这一部分重点在于：

The focus of this part is:

- 使用更适合文本频率建模的方法  
  Use a method more suitable for text frequency modeling
- 理解为什么它通常比 KNN 更适合此类任务  
  Understand why it is usually better suited than KNN for this task

### 6.7 参数分析 / Parameter Analysis

这两部分图像分析帮助你理解：

These plotting sections help you understand:

- 平滑参数过大或过小都会影响模型表现  
  Smoothing values that are too large or too small can hurt performance
- 词汇表过小会丢失信息，过大也不一定继续提升效果  
  A vocabulary that is too small loses information, while a very large vocabulary does not always continue improving performance

## 7. 建议重点关注的结果 / Key Results to Focus On

建议你特别关注以下结论：

You should pay special attention to the following conclusions:

1. `KNN` 在这个任务上的效果明显弱于朴素贝叶斯模型。  
   `KNN` performs noticeably worse than the Naive Bayes models on this task.

2. `Bernoulli Naive Bayes` 的表现优于 KNN，但通常弱于 `Multinomial Naive Bayes + TF-IDF`。  
   `Bernoulli Naive Bayes` performs better than KNN, but is usually weaker than `Multinomial Naive Bayes + TF-IDF`.

3. `Multinomial Naive Bayes + TF-IDF` 往往给出本作业中最好的分类效果。  
   `Multinomial Naive Bayes + TF-IDF` usually gives the best performance in this assignment.

4. 最有信息量的词可以帮助你理解模型为什么会做出某类判断。  
   Informative words help explain why the model makes certain predictions.

## 8. 学习建议 / Study Tips

1. 不要只看准确率，也要看“最有信息量的词”。  
   Do not look only at accuracy; also examine the “most informative words.”

2. 学习时建议把 Bernoulli 和 Multinomial 的关键词结果放在一起比较。  
   When studying, compare the keywords from Bernoulli and Multinomial side by side.

3. 如果你对图像结果不敏感，可以把最佳参数和最佳准确率单独记下来。  
   If plots are not intuitive for you, write down the best parameters and best accuracy separately.

4. 如果需要写报告，可以从“特征表示不同”和“模型假设不同”这两个角度展开。  
   If you need to write a report, discuss it from two angles: different feature representations and different model assumptions.

## 9. 重新运行前的注意事项 / Notes Before Re-Running

1. 请确认 `20news-bydate_py3.pkz` 仍在当前目录。  
   Make sure `20news-bydate_py3.pkz` is still in the current folder.

2. 请不要解压该数据文件。  
   Do not unzip the dataset file.

3. 建议从上到下顺序执行 notebook。  
   Run the notebook from top to bottom in order.

4. 记得先填写 `Name / EID`。  
   Remember to fill in `Name / EID` first.

## 10. 提交前自查 / Self-Check Before Submission

- 是否已经填写姓名和学号？  
  Have you filled in your name and student ID?

- 是否确认提交的是老师要求的版本（已运行或未运行）？  
  Have you confirmed whether the required submission should be executed or unrun?

- 是否确认 notebook 可以正常打开？  
  Have you confirmed that the notebook opens correctly?

- 是否确认数据文件位置正确？  
  Have you confirmed that the dataset file is in the correct location?

- 是否理解了主要模型之间的区别？  
  Do you understand the main differences among the models?

## 11. 推荐使用方式 / Recommended Usage

如果你是学生：

If you are a student:

- 用 `Tutorial1_bilingual.ipynb` 作为主要阅读和提交版本。  
  Use `Tutorial1_bilingual.ipynb` as the main reading and submission version.

- 用 `Tutorial1.ipynb` 对照查看已经生成的结果。  
  Use `Tutorial1.ipynb` to check the already generated results.

如果你是老师或助教：

If you are an instructor or TA:

- 可以优先查看双语版 notebook 和本指南。  
  You may review the bilingual notebook and this guide first.

- 如需直接查看结果，可打开已运行版本。  
  If direct outputs are needed, open the executed version.
