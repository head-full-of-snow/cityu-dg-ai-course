# Tutorial 2 中文翻译：逻辑回归与支持向量机

> 本文是 `Tutorial2.ipynb` 的完整中文翻译，包含题目说明、代码和已经填好的分析答案，方便对照理解。
>
> **姓名：** \_\_\_\_\_
>
> **EID：** \_\_\_\_\_

---

## 本次教程简介

在本次教程中，你将使用**逻辑回归（Logistic Regression）**、**支持向量机（Support Vector Machine）**、**朴素贝叶斯（Naive Bayes）** 和 **K 近邻（KNN）** 来预测一张人脸图像的性别是男性还是女性。

首先需要初始化 Python 环境，运行下面的代码单元格。

> **注意**：本教程推荐使用的 scikit-learn 版本是 **1.3**。如果使用其他版本，可能会出现 bug。

```python
%matplotlib inline
import IPython.core.display
# 设置输出图像格式（Chrome 浏览器显示效果最好）
IPython.core.display.set_matplotlib_formats("svg")
import matplotlib.pyplot as plt
import matplotlib
from numpy import *
from sklearn import *
import os
import zipfile
import fnmatch
random.seed(100)
```

---

## 1. 数据加载与预处理

我们首先需要加载图像。请下载 `photos-bw.zip`，并把它放在与本 ipynb 文件相同的目录下。**不要解压该文件。** 然后运行下面的单元格来加载图像。

```python
imgdata = []
genders = []

# 加载 zip 文件
filename = 'photos-bw.zip'
zfile = zipfile.ZipFile(filename, 'r')

for name in zfile.namelist():
    # 检查文件名是否匹配
    if fnmatch.fnmatch(name, "photos-bw/*.png"):
        print("loading", name)
        # 在内存中打开文件，并解析为图像
        myfile = zfile.open(name)
        img = matplotlib.image.imread(myfile)
        myfile.close()

        # 追加到数据中
        imgdata.append(img)
        genders.append( int(name[len("photos-bw/")] == 'm') )  # 0 表示女性，1 表示男性

zfile.close()
imgsize = img.shape
print("DONE: loaded {} images".format(len(imgdata)))
```

运行结果：共加载 **50** 张图像。

每张图像都是一个 45×40 的像素值数组。运行下面的代码显示一个示例：

```python
print(img.shape)
plt.imshow(img, cmap='gray', interpolation='nearest')
plt.show()
```

输出：`(45, 40)`

运行下面的代码可以显示全部图像（缩略图拼接）：

```python
# 用于生成图像拼贴（montage）的函数
def image_montage(X, imsize=None, maxw=10):
    """X 可以是图像列表，也可以是向量化后的图像矩阵。
      当 X 是矩阵时需要指定 imsize。"""
    tmp = []
    numimgs = len(X)

    # 创建图像列表（如有必要则 reshape）
    for i in range(0, numimgs):
        if imsize != None:
            tmp.append(X[i].reshape(imsize))
        else:
            tmp.append(X[i])

    # 补上空白图像，使拼贴整齐
    if (numimgs > maxw) and (mod(numimgs, maxw) > 0):
        leftover = maxw - mod(numimgs, maxw)
        meanimg = 0.5*(X[0].max()+X[0].min())
        for i in range(0, leftover):
            tmp.append(ones(tmp[0].shape)*meanimg)

    # 生成拼贴图
    tmp2 = []
    for i in range(0, len(tmp), maxw):
        tmp2.append( hstack(tmp[i:i+maxw]) )
    montimg = vstack(tmp2)
    return montimg

plt.figure(figsize=(9,9))
plt.imshow(image_montage(imgdata), cmap='gray', interpolation='nearest')
plt.show()
```

每张图像是一个二维数组，但分类算法需要的是一维向量。运行下面的代码，把所有图像展平（flatten）成一维向量。结果是一个矩阵，每一行是一张展平后的图像。

```python
X = empty((50, prod(imgdata[0].shape)))  # 创建空数组
for i, img in enumerate(imgdata):
    X[i, :] = ravel(img)                 # 把每张图像变成一个向量
Y = asarray(genders)                     # 把列表转换成 numpy 数组
print(X.shape)
print(Y.shape)
```

输出：

```
(50, 1800)
(50,)
```

接下来，我们把像素值整体平移，使灰色对应 0.0、黑色对应 -0.5、白色对应 0.5。

```python
print("Before: min={}, max={}".format(X.min(), X.max()))
X -= 0.5
print("After:  min={}, max={}".format(X.min(), X.max()))
```

输出：

```
Before: min=0.0, max=1.0
After:  min=-0.5, max=0.5
```

最后，把数据集划分为训练集和测试集。我们取 80% 用于训练，20% 用于测试。

```python
# 随机划分 80% 训练集和 20% 测试集
trainX, testX, trainY, testY = \
  model_selection.train_test_split(X, Y,
  train_size=0.80, test_size=0.20, random_state=4487)

print(trainX.shape)
print(testX.shape)
```

输出：

```
(40, 1800)
(10, 1800)
```

---

## 2. 逻辑回归（Logistic Regression）

训练一个逻辑回归分类器。使用交叉验证（cross-validation）来选择最优的 $C$ 参数。

```python
# 训练逻辑回归分类器
# LogisticRegressionCV 内部使用交叉验证选择最优的 C
logreg = linear_model.LogisticRegressionCV(cv=5, max_iter=5000)
logreg.fit(trainX, trainY)
print("best C =", logreg.C_[0])
```

运行结果：`best C = 0.0464`

用学到的模型分别对训练数据和测试数据预测性别。训练集上的准确率是多少？测试集上的准确率是多少？

```python
# 用模型进行预测
predYtrain = logreg.predict(trainX)
predYtest  = logreg.predict(testX)

# 计算准确率
acc = metrics.accuracy_score(trainY, predYtrain)
print("train accuracy =", acc)

acc = metrics.accuracy_score(testY, predYtest)
print("test accuracy  =", acc)
```

运行结果：

```
train accuracy = 0.95
test accuracy  = 0.8
```

### 2.1 分析分类器

运行下面的代码，把超平面参数 $\mathbf{w}$ 显示为一张图像。

```python
# logreg 是训练好的逻辑回归模型
wimg = logreg.coef_.reshape(imgsize)      # 取出 w 并 reshape 成图像
mycmap = matplotlib.colors.LinearSegmentedColormap.from_list('mycmap', ["#0000FF", "#FFFFFF", "#FF0000"])
mm = max(wimg.max(), -wimg.min())
plt.imshow(wimg, interpolation='nearest', cmap=mycmap, vmin=-mm, vmax=mm)
plt.colorbar()
plt.title("weight image")
plt.show()
```

回顾一下：分类器的预测基于函数 $f(\mathbf{x}) = \mathbf{w}^T\mathbf{x}+b = \sum_{i=1}^P w_ix_i + b$ 的符号。这里每个 $x_i$ 是人脸图像中的一个像素，$w_i$ 是对应的权重。因此，这个函数相当于把人脸图像与权重图像逐像素相乘，然后对所有像素求和。

为了让 $f(\mathbf{x})$ 为正，权重图像中的正值（红色区域）应当与人脸图像中的正值（白色像素）对应，权重图像中的负值（蓝色区域）应当与人脸图像中的负值（黑色像素）对应。

于是可以有如下的解释：

| 类别 | 红色区域（正权重） | 蓝色区域（负权重） | 白色区域（权重接近 0） |
|------|--------------------|--------------------|------------------------|
| +1 类（男性） | 人脸图像中的白色像素 | 人脸图像中的黑色像素 | 不重要的区域 |
| -1 类（女性） | 人脸图像中的黑色像素 | 人脸图像中的白色像素 | 不重要的区域 |

**观察权重图像，分类器在看人脸图像的哪些部分来判断性别？这样合理吗？**

### 答案

- 观察权重图像可以发现：权重绝对值最大的区域都在**头发区域**，而不在人脸内部（眼睛、鼻子、嘴巴附近基本都是白色，即权重接近 0）。

  - **图像顶部（额头 / 发际线一带）是蓝色**（负权重）：该处出现黑色像素会把预测推向男性（+1）。这对应男性较短的深色头发覆盖了这一片区域。
  - **人脸左下和右下两侧是红色**（正权重）：该处出现白色像素会把预测推向男性；反过来，黑色像素（垂在脸旁的长发）会把预测推向女性（-1）。

  也就是说，分类器主要利用**发型 / 头发轮廓**这一线索来判断性别，而不是五官特征。在这个数据集上这是合理的：男性都是短发，女性多为垂在脸两侧的长发，因此仅凭头发区域就足以很好地区分性别。

---

现在来看看测试集中被错误分类的人脸。运行下面的代码，显示分类错误和分类正确的人脸。

```python
# predYtest 是测试集上的类别预测结果。

# 找出被错误分类的测试图像
inds = where(predYtest != testY)  # 获取被错误分类的测试图像的索引
# 生成拼贴图
badimgs = image_montage(testX[inds], imsize=imgsize)

# 找出被正确分类的测试图像
inds = where(predYtest == testY)
goodimgs = image_montage(testX[inds], imsize=imgsize)

plt.figure(figsize=(8,4))
plt.subplot(2,1,1)
plt.imshow(badimgs, cmap='gray', interpolation='nearest')
plt.title('misclassified faces')
plt.subplot(2,1,2)
plt.imshow(goodimgs, cmap='gray', interpolation='nearest')
plt.title('correctly classified faces')
plt.show()
```

**为什么分类器会对这些被错误分类的人脸做出错误的预测？**

### 答案

- 分类器在测试集上一共错了 **2 张**，都是**被预测成男性的女性**。观察这两张脸可以发现：她们的头发被扎起或比较短，脸的两侧没有深色长发垂下来。由于分类器主要看的是头发区域（见上面的权重图像），这两张女性人脸在它看来是"男性样"的。也就是说，分类器依赖的是发型而不是五官，一旦女性是短发或把头发扎起来，就打破了它学到的规律，从而被误分类。

---

## 3. 支持向量机（Support Vector Machine）

现在在同一份训练数据和测试数据上训练一个支持向量机（SVM）。使用交叉验证选择最优的 $C$ 参数。

```python
# 搜索不同的 C 值
paramgrid = {'C': logspace(-4, 4, 20)}

# 用 5 折交叉验证选择最优的 C
# 使用线性核（linear kernel），这样才能把超平面 w 可视化出来
clf = model_selection.GridSearchCV(svm.SVC(kernel='linear'), paramgrid, cv=5)
clf.fit(trainX, trainY)
print("best C =", clf.best_params_['C'])
```

运行结果：`best C = 0.00483`

计算 SVM 分类器的训练集和测试集准确率。

```python
# 用模型进行预测
predYtrain = clf.predict(trainX)
predYtest  = clf.predict(testX)

# 计算准确率
acc = metrics.accuracy_score(trainY, predYtrain)
print("train accuracy =", acc)

acc = metrics.accuracy_score(testY, predYtest)
print("test accuracy  =", acc)
```

运行结果：

```
train accuracy = 0.9
test accuracy  = 0.8
```

与之前类似，把超平面参数 $w$ 画成图像，并查看被错误分类和被正确分类的测试图像。

```python
# clf 是训练好的 SVM 模型（使用交叉验证选出的最优估计器）
wimg = clf.best_estimator_.coef_.reshape(imgsize)   # 取出 w 并 reshape 成图像
mycmap = matplotlib.colors.LinearSegmentedColormap.from_list('mycmap', ["#0000FF", "#FFFFFF", "#FF0000"])
mm = max(wimg.max(), -wimg.min())
plt.imshow(wimg, interpolation='nearest', cmap=mycmap, vmin=-mm, vmax=mm)
plt.colorbar()
plt.title("SVM weight image")
plt.show()
```

再来看看测试集中被错误分类的人脸，像上面一样显示分类错误和分类正确的人脸。

```python
# 找出被错误分类的测试图像
inds = where(predYtest != testY)  # 获取被错误分类的测试图像的索引
# 生成拼贴图
badimgs = image_montage(testX[inds], imsize=imgsize)

# 找出被正确分类的测试图像
inds = where(predYtest == testY)
goodimgs = image_montage(testX[inds], imsize=imgsize)

plt.figure(figsize=(8,4))
plt.subplot(2,1,1)
plt.imshow(badimgs, cmap='gray', interpolation='nearest')
plt.title('misclassified faces')
plt.subplot(2,1,2)
plt.imshow(goodimgs, cmap='gray', interpolation='nearest')
plt.title('correctly classified faces')
plt.show()
```

**逻辑回归的 $w$ 和 SVM 的 $w$ 之间有什么不同吗？对这些不同点有没有什么解释？**

### 答案

- 两张权重图像的**整体图案非常相似**：两者都把较大的权重放在头发区域（顶部偏蓝、左右下侧偏红），而眼睛 / 鼻子 / 嘴巴附近的权重接近 0。这说明两个模型学到的判别特征是相同的（都是发型）。

  两者的差异主要体现在权重的**数值大小和分布**上：

  - 逻辑回归的权重数值更大（最大约 0.045，SVM 约 0.021）。这是因为交叉验证给逻辑回归选到的 $C$（约 0.046）比 SVM 的 $C$（约 0.0048）更大，也就是说 SVM 的正则化更强。
  - 逻辑回归最大化的是数据似然（likelihood），**每一张训练人脸**都对 $\mathbf{w}$ 有贡献；因此 $\mathbf{w}$ 看起来更像是男性、女性人脸的"平均差异"，比较平滑、分散。
  - 线性 SVM 最大化的是间隔（margin），$\mathbf{w}$ 只由**支持向量**（离决策边界最近的那几张脸）决定；因此权重图像更集中在真正区分两类的那些模糊/关键区域上。

---

## 4. 朴素贝叶斯（Naive Bayes）

接下来，我们在同一份训练数据和测试数据上训练一个朴素贝叶斯（NB）模型（上一节课讲过），然后显示训练集和测试集的准确率。

```python
# 训练高斯朴素贝叶斯分类器
nb = naive_bayes.GaussianNB()
nb.fit(trainX, trainY)

# 用模型进行预测
predYtrain = nb.predict(trainX)
predYtest  = nb.predict(testX)

# 计算准确率
acc = metrics.accuracy_score(trainY, predYtrain)
print("train accuracy =", acc)

acc = metrics.accuracy_score(testY, predYtest)
print("test accuracy  =", acc)
```

运行结果：

```
train accuracy = 0.975
test accuracy  = 0.9
```

再来看看测试集中被错误分类的人脸，像上面一样显示分类错误和分类正确的人脸。

```python
# predYtest 是测试集上的类别预测结果。

# 找出被错误分类的测试图像
inds = where(predYtest != testY)  # 获取被错误分类的测试图像的索引
# 生成拼贴图
badimgs = image_montage(testX[inds], imsize=imgsize)

# 找出被正确分类的测试图像
inds = where(predYtest == testY)
goodimgs = image_montage(testX[inds], imsize=imgsize)

plt.figure(figsize=(8,4))
plt.subplot(2,1,1)
plt.imshow(badimgs, cmap='gray', interpolation='nearest')
plt.title('misclassified faces')
plt.subplot(2,1,2)
plt.imshow(goodimgs, cmap='gray', interpolation='nearest')
plt.title('correctly classified faces')
plt.show()
```

（朴素贝叶斯在测试集上只错了 **1 张**，同样是把一名头发扎起的女性预测成了男性。）

---

## 5. K 近邻（K Nearest Neighbor）

另外，在同一份训练数据和测试数据上训练一个 K 近邻（KNN）模型（上一节课讲过）。使用交叉验证选择最优的 $K$ 参数，然后显示训练集和测试集的准确率。

```python
# 搜索不同的 K 值
paramgrid = {'n_neighbors': [3, 5, 10]}

# 用 5 折交叉验证选择最优的 K
clf = model_selection.GridSearchCV(neighbors.KNeighborsClassifier(), paramgrid, cv=5)
clf.fit(trainX, trainY)
print("best K =", clf.best_params_['n_neighbors'])

# 用模型进行预测
predYtrain = clf.predict(trainX)
predYtest  = clf.predict(testX)

# 计算准确率
acc = metrics.accuracy_score(trainY, predYtrain)
print("train accuracy =", acc)

acc = metrics.accuracy_score(testY, predYtest)
print("test accuracy  =", acc)
```

运行结果：

```
best K = 3
train accuracy = 0.875
test accuracy  = 0.8
```

（notebook 中还附带了一段验证用的代码，会重新拟合并输出相同的结果。）

```python
clf.fit(trainX, trainY)
# 用模型进行预测
predYtrain = clf.predict(trainX)
predYtest = clf.predict(testX)

# 计算准确率
acc      = metrics.accuracy_score(trainY, predYtrain)
print("train accuracy =", acc)

# 计算准确率
acc      = metrics.accuracy_score(testY, predYtest)
print("test accuracy  =", acc)
```

再来看看测试集中被错误分类的人脸，像上面一样显示分类错误和分类正确的人脸。

```python
# predYtest 是测试集上的类别预测结果。

# 找出被错误分类的测试图像
inds = where(predYtest != testY)  # 获取被错误分类的测试图像的索引
# 生成拼贴图
badimgs = image_montage(testX[inds], imsize=imgsize)

# 找出被正确分类的测试图像
inds = where(predYtest == testY)
goodimgs = image_montage(testX[inds], imsize=imgsize)

plt.figure(figsize=(8,4))
plt.subplot(2,1,1)
plt.imshow(badimgs, cmap='gray', interpolation='nearest')
plt.title('misclassified faces')
plt.subplot(2,1,2)
plt.imshow(goodimgs, cmap='gray', interpolation='nearest')
plt.title('correctly classified faces')
plt.show()
```

（KNN 在测试集上错了 **2 张**，同样是把头发扎起 / 短发的女性预测成了男性。）

---

## 结果汇总

| 模型 | 最优超参数 | 训练集准确率 | 测试集准确率 | 测试集错分数量 |
|------|------------|--------------|--------------|----------------|
| 逻辑回归（Logistic Regression） | C ≈ 0.046 | 0.95 | 0.80 | 2（女→男） |
| 线性 SVM（Linear SVM） | C ≈ 0.0048 | 0.90 | 0.80 | 2（女→男） |
| 高斯朴素贝叶斯（Gaussian NB） | — | 0.975 | **0.90** | 1（女→男） |
| K 近邻（KNN） | K = 3 | 0.875 | 0.80 | 2（女→男） |

**小结：**

1. 四个模型的测试集准确率都在 0.8 以上，其中朴素贝叶斯最高（0.90）。
2. 从逻辑回归和 SVM 的权重图像可以看出，模型主要依赖**头发 / 发型区域**（图像顶部和两侧）来判断性别，而不是五官——这与数据集中"男性短发、女性长发"的特点一致。
3. 所有模型的错误都是"短发或扎起头发的女性被误判为男性"，说明发型这一线索一旦失效，分类器就容易出错。这也提醒我们：模型学到的只是数据集中的相关性（发型与性别相关），不一定是我们真正想让它学到的东西（五官与性别相关）。
