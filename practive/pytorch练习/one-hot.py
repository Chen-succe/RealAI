import torch
import numpy as np

# pytorch生成
x = torch.rand(2, 3, dtype=torch.float)
# print(x, type(x))

lable = torch.zeros(x.shape[:2])
# print(lable, lable.dtype, lable.type)

lable_long = torch.LongTensor(lable.numpy())
# torch.LongTensor 是 PyTorch 中的一个数据类型，
# 用于表示包含整数（整型数据）的张量（tensor）。它是一种特定的张量类型，其中的元素都为整数类型，
# 并且使用 64 位整数进行存储,不能传入一个tensor。


'''
tensor.scatter_(dim, index, src) 
dim : 指定了覆盖数据是从哪个轴作为依据。后面再详细解释。值的范围是从0到 sum(tensor.shape)-1
index ： 告诉函数要将src中对应的值放到tensor的哪个位置。index的shape要和src一致，或者src可以通过广播机制实现shape一致。
src : 保存了想用来覆盖tensor的值

'''
one_hot = torch.zeros(3,5).scatter_(0, torch.LongTensor([[0,1], [1,1]]), x)  
# 由于x中是两行三列，所以，torch.Longtensor中最多有两行，每行中列的索引是新生成tensor的对应位置。
# 在新生成的tensor中，应该有torch.LonngTensor种元素数量相同的元素数，除非有覆盖情况。
# 解释[0,1], [1,1]。[0,1]表示从x的第一行去取数，取到的数放在新生成tensor中对应位置，
# 比如[0,1]就表示，0是从x中第一行中取第一个数，放到新生成的tensor中第一列的第0行，1表示从x中第一行中取第二个数，
# 放到新生成tensor中第二列的第1行。如果不是[0,1]是个[0,2]。则2表示从x的第一行中第二个数字，放到新生成的tensor的第二列的第3行。
# 从x中取数是按照索引取，放到新生成的tensor中是将取到的数字再当成索引放到新生成tenor中对应位置。
print(one_hot)

lable = torch.tensor([1,0,3,4,2]) # 比如有这样一个类别索引，想转为one-hot，如何做
print(lable.unsqueeze(0).numpy())
one_hot = torch.zeros(5, 5).scatter_(0, torch.LongTensor(lable.unsqueeze(0).numpy()), 1)
print(one_hot)

# 一般是按照batch_size，比如batch_size为5， 类别数为6 .上面的lable应该改为lable.unsqueeze(1).numpy()
lable = lable.unsqueeze(1).numpy()
class_num = 6
print(lable.shape)
one_hot = torch.zeros(lable.shape[0], class_num).scatter_(1, torch.LongTensor(lable), 1)
print(one_hot)

# 每一行都是一个label的one-hot标签