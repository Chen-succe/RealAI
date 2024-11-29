import torch
import torch.nn as nn
import numpy as np
from torchvision.models import resnet34

# 四维数组生成one-hot，一般用在分割任务
# 假设最后是一个5*5的特征图，共4个类别, 0,1,2,3
class_num = 4

gt = np.random.randint(0, class_num, size=[5,5])
gt = torch.LongTensor(gt)
print(gt)

def get_one_hot(label, N):
    # print(type(label.size()))  # <class 'torch.Size'>
    size = list(label.size())
    label = label.view(-1)  # 25*1
    print('label after reisze :{}'.format(label))
    # print(size)  # [5, 5]
    ones = torch.eye(N)
    ones = ones.index_select(0, label)  # 25*4
    print(ones)
    size.append(N)
    # print(size)  # [5, 5, 4]
    ones = ones.view(*size)
    return ones

    

ones = get_one_hot(gt, class_num)
print(ones)

# model = resnet34()
# print(model)

a = torch.tensor([[0.1, 0.2], [-0.3, 0.5]])
pred = torch.sigmoid(a)
preds = (pred > 0.5).float()
print(preds)
label = torch.tensor([[0,1], [0,1]])
label = label.float()
print(label)
print(preds == label)
print((preds == label).float().sum())