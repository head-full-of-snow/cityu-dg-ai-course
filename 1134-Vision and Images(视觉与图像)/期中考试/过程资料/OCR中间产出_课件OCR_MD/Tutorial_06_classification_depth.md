Zhu Zhiyu

Tutorial 04: Classification and depth estimation

# (1) Classification

What we will cover today:

Introduction to the CIFAR-10 dataset.

Building a custom Convolutional Neural Network (CNN) from scratch.

Adapting a state-of-the-art Vision Transformer (ViT) for a custom task.

Understanding the differences in data processing for CNNs vs. ViTs.

Writing a standard PyTorch training loop.

# (1) Classification

What are we trying to classify?

The Dataset: 60,000 color images (50,000 for training, 10,000 for testing).

The Classes: 10 distinct categories (airplanes, cars, birds, cats, deer, dogs, frogs, horses, ships, trucks).

The Challenge: The images are incredibly small—only 32x32 pixels.

Why it matters: The low resolution forces our neural networks to learn highly efficient feature representations to tell a dog apart from a cat.

# (1) Classification

**CNN**

•How it works: Uses sliding windows (filters/kernels) to detect local patterns like edges, corners, and textures.

•Architecture: Layers of Convolutions $\rightarrow$ Pooling (downsizing) $\rightarrow$ Fully Connected (Classification) Layers.

• Why it fits CIFAR-10: CNNs are naturally suited for 32x32 images. They are computationally lightweight and train quickly from scratch on smaller datasets.

# (1) Classification

**The Modern State-of-the-Art**

How it works: Inspired by Natural Language Processing. It treats an image like a sentence.

Patching: The image is chopped into a grid of smaller "patches" (usually 16×16 pixels).

Attention: Instead of local filters, ViTs use "Self-Attention" to look at the entire image at once and see how every patch relates to every other patch.

(1) Classification

Refer to the supplemented code

# (2)

Neural Network Depth Estimation

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F88040511e2364eccbe19cbd3dcf980d5%2Fmedia%2F5b837c802b8c47bc9fe3e0b9ef8baad6.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253961&Signature=EMSZaMkh5%2Fv9tlz0nTgliMc1U9g%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F88040511e2364eccbe19cbd3dcf980d5%2Fmedia%2F7bf126f2b1834d2a9ffbf55ccb9cf9d7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253961&Signature=dO9zhs2JJsexxLXkcFaWkz3tXAE%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F88040511e2364eccbe19cbd3dcf980d5%2Fmedia%2Fbd4555ea0d2c49dabc96680c1f283e4c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253961&Signature=F7%2BLgAIYB8BaQ%2FQahql1UPDmWhA%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F88040511e2364eccbe19cbd3dcf980d5%2Fmedia%2F9f0bce8cd6a64d8487b16b75c2782051.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253961&Signature=fT7uaXvuOJvfmfUPvpz5UYm5r0U%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F88040511e2364eccbe19cbd3dcf980d5%2Fmedia%2F372a23060f3b4edfa8ea4ca11c45bb73.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253961&Signature=2kho2kFHLWS1f8QN7s4b21hVAFs%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F88040511e2364eccbe19cbd3dcf980d5%2Fmedia%2F1cdf6df6a9664a95a9efe8287cbc89bd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799253962&Signature=%2FrRIVJ8mFY7bUYyhrJzqTTZrX10%3D)

(2) Neural Network Depth Estimation

Refer to the supplemented code
