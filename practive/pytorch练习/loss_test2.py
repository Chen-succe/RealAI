import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

input = torch.tensor([[5], [3], [5], [6]])
labels = torch.tensor([2, 2, 2, 2])

mse = nn.MSELoss()

mse_loss = mse(input.float(), labels.float())
print('mes_loss:{}'.format(mse_loss))

mes_cal = np.mean((input.squeeze().numpy() - labels.numpy()) ** 2)
print(mes_cal)