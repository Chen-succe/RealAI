import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

# 假设有四个样本，三个类别。
input = torch.tensor([[0.7, 0.3, 0.3], [0.2, 0.8, 0.4], [0.4, 0.5, 0.7], [0.1, 0.4, 0.9]], requires_grad=True)
# input_s = nn.Sigmoid()(input)
input_soft = nn.Softmax()(input)
print(input_soft)
input_s = input
print(input_s)
print(input_s.shape)
# 真实标签
true_labels = torch.tensor([[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
true_lable_c = torch.tensor([0, 0, 1, 2])

a1 = np.log(0.7) + np.log(1-0.3) + np.log(1-0.3)
a2 = np.log(0.2) + np.log(1-0.8) + np.log(1-0.4)
a3 = np.log(0.5) + np.log(1-0.4) + np.log(1-0.7)
a4 = np.log(0.9) + np.log(1-0.4) + np.log(1-0.1)
a = -(a1 + a2 + a3 +a4) / 12

b = -(np.log(0.4272) + np.log(0.2473) + np.log(0.3199) + np.log(0.4864)) / 4

#定义损失函数：
ce = nn.CrossEntropyLoss()
bce = nn.BCELoss()
bcew = nn.BCEWithLogitsLoss()

loss_ce = ce(input, true_lable_c)
loss_ce_c = ce(input, true_labels.float())
loss_bce = bce(input, true_labels.float())
loss_bcew = bcew(input, true_labels.float())




print('loss_ce:{}'.format(loss_ce))
print('loss_ce_c:{}'.format(loss_ce_c))
print(b)

print('loss_bce:{}'.format(loss_bce))
print('loss_bcew:{}'.format(loss_bcew.item()))
print(a)



'''
用到的知识点：
1. one-hot编码:分为两类。一类是对输出网络为二维的情况，一类是输出是思维特征图的情况。
2. BCE和CE损失使用时有些区别要注意。
3. BCELoss 期望模型输出已经经过 sigmoid 激活，而 BCEWithLogitsLoss 会在内部应用 sigmoid 激活。
详见笔记2024.11.25损失函数
'''