import torch
import numpy as np

# a = torch.randint(0,3,(4,10))
# print('1', a)
# a_sig = torch.sigmoid(a)
# print('2', a_sig)
# print(a_sig.shape)
# a = a_sig.argmax(-1)
# print('3', a)
# b = torch.randint(0,3, (4, 1)).squeeze()
# print('b', b)
# diff = torch.abs(b-a)
# print(diff)
# acc_le = torch.mean(diff.le(5).float()).item()
# print(acc_le)

# img1 = torch.randn(3,2, 2).unsqueeze(0)
# img2 = torch.randn(3,2,2).unsqueeze(0)
# img_cat = torch.cat([img1, img2], dim=0)
# print(img1)
# print(img2)
# print(img_cat)
n = 0

a = torch.randn(1,3)
b = torch.randn(1,3)
c = []
c.append(a)
c.append(b)
print(c)
d = torch.cat(c)
print(d)
cnt = 0
for i in range(0, 10, 4):
    for j in range(i, 10, 4):
        cnt += 1
        batch_i = i, i + 4
        batch_j = j, j + 4
        # print(batch_i)
        # print(batch_j)
        # print(i, j)
# print(cnt)

father = np.arange(10, dtype=np.int32)
print(father)


for i in range(0, 43, 10):
    print(i)
    