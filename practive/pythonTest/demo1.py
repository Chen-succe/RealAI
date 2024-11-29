import numpy as np
import torch
import torch.nn.functional as F

a = np.ones((5, 2))
a = torch.tensor(a)
print(a)
b = a[:, :1]
c = a[:, 1:]
d1 = torch.mean(b, dim=1)
d2, _ = torch.max(c, dim=1)
d = torch.cat((d1, d2))
print(d)
prob = F.softmax(d)
print(prob)
