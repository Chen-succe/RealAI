import torch
import torch.nn.functional as F


a = torch.tensor([[0.1, 0.2, 0.4, 0.5], [-0.3, 0.5, 0.4, 0.8]])
label = torch.tensor([1, 1])

real = a[:, :1]
fake = a[:, 1:]
print(real)
print(fake)

mean_real = torch.mean(real, dim=1, keepdim=True)
max_fake, _ = torch.max(fake, dim=1, keepdim=True)  # 注意，max函数返回两个值

print(mean_real)
print(max_fake)

dist = torch.cat((mean_real, max_fake), dim=1)
print('dist', dist)

prob = F.softmax(dist.detach().clone(), dim=1)
print(prob)
loss = F.cross_entropy(dist, label , torch.tensor([4,1]).to(dist)) # .to(dist)表示转化为跟dist一样的格式。
                                              #这里也可以torch.tensor([4,1]).float(),需要的是一个float类型，而不是long类型
print(loss)

a = torch.softmax(torch.tensor([0.4061, 0.5939]),dim=0, dtype=torch.float)
print(a) 


d1 = torch.tensor(3)
d2 = torch.tensor(6)
diff = torch.abs(d1-d2)
print(diff)
print(diff.le(5))
print(diff.le(5).float())