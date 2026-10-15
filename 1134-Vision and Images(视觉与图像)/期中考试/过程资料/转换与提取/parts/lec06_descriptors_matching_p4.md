# Feature matching

Given a feature in  $ I_{1} $, how to find the best match in  $ I_{2} $?

1. Define distance function that compares two descriptors

2. Test all the features in  $ I_{2} $, find the one with min distance (can be accelerated with a nearest neighbors search data structure, like a kd-tree)

# Feature distance

How to define the difference between two features  $ f_{1}, f_{2} $?

– Simple approach:  $ L_{2} $ distance,  $ \parallel f_{1}-f_{2}\parallel $

— can give small distances for ambiguous (incorrect) matches

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F92348dcba45c43f8ada8d96e299a1d0d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256298&Signature=ddhsSbXZArWJDfvg6A6a9XNk3w8%3D)

$ I_{1} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2Ff8111082a868406f8c53c116ebe476d4.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=oUnT5ROXaXQxd9o646m9BQE849Q%3D)

$ I_{2} $

# Feature distance

How to define the difference between two features  $ f_{1}, f_{2} $?

• Better approach: ratio distance =  $ \left\| f_1 - f_2 \right\| / \left\| f_1 - f_2' \right\| $

•  $ f_{2} $ is the best SSD match to  $ f_{1} $ in  $ I_{2} $

•  $ f_{2}^{\prime} $ is the  $ 2^{nd} $ best SSD match to  $ f_{1} $ in  $ I_{2} $

• gives large values for ambiguous matches

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F86aaadc80ae0413f96d43c9aa08c2de1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=NyqJoGjc%2BiOWLN7icPbdeZI5wxk%3D)

$ I_{1} $

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F7523c2cca2cf499aa54aa9ae41b24ead.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=Uv94lhiGhPHoaE3BrVTEmmBNH9U%3D)

$ I_{2} $

# Feature distance

• Does the SSD vs "ratio distance" change the best match to a given feature in image 1?

• No, but it changes the distance, and it can change the ordering of matches from good to bad

• After we compute a set of matches, we threshold by distance (that is, throw out matches with distance > threshold)

# Feature matching example

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2Faa17d4332d9b4b3793be8797c006135d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=gwo0bcmaVPAa3gFv2LYG53ZZ4eU%3D)

58 matches (thresholded by ratio score)

# Feature matching example

We'll deal with outliers later

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F5e0a915bed574c2aaf0027a92661eb4a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=sA8x7fKUsoG4OGhCTASFBXgVlTQ%3D)

51 matches (thresholded by ratio score)

# Evaluating the results

How can we measure the performance of a feature點選擇?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F934f845156ef4cfa966e9af58f5dd6fb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=K4YJXNrxp0iZJMHCQDsV6SF7e9c%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F5f6d8832f2d6452a874371334e9bc18c.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=hM%2FW7AODLnoL4geT3hn9fmISQng%3D)

feature distance

# True/false positives

How can we measure the performance of a feature點選擇?

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F0ea524040ee24ff0b1aaffd0673f773f%2Fmedia%2F7715dbe704984c06b919a34c9fbfd378.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256299&Signature=6DfLlCTv5EqbLKYS5q6oyGl2ZCo%3D)

feature distance

The distance threshold affects performance

– True positives = # of detected matches that survive the threshold that are correct

– False positives = # of detected matches that survive the threshold that are incorrect
