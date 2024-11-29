import torch
import numpy as np
import torch.nn.functional as F
a = torch.tensor(np.ones((5, 5, 5)))
print(a)
a = F.avg_pool1d(a, kernel_size=3)
print(a)
print(a.shape)

for i in range(4):
    for j in range(5):
        if j == 2:
            continue
        print('i:', i)
        print('j:', j)