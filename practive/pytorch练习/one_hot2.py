import torch
import torch.nn as nn
import numpy as np

# tensor.index_select 方法


class_num = 6 # 假设有6个类别
tens = torch.tensor([2,1,4,0,5])
# tens.index_select(dim, index, out=None)dim为0，以为这按照行来取tensor的向量。具体取哪一行呢，就是label中的值了
ones = torch.eye(class_num)
one_hot = ones.index_select(dim=0, index=tens)
print(ones)
print(one_hot)

print(one_hot.argmax(-1) == tens)
print(one_hot.argmax(1))