import torch
import numpy as np

def IoU(SR, GT, threshold=0.5):
    print(SR)
    print(GT)
    SR = SR > threshold
    GT = GT == torch.max(GT)
    print(SR, GT)
    print((SR == 1) & (GT ==1))
    print(torch.sum((SR == 1) & (GT ==1)))
    TP = ((SR == 1) & (GT == 1))
    FP = ((SR == 1) & (GT == 0))
    FN = ((SR == 0) & (GT == 1))
    IOU = float(torch.sum(TP)) / (float(torch.sum(TP + FP + FN)) + 1e-6)

    return IOU

sr = torch.eye(3,3)
gr = torch.randint(0, 2, size=(3,3))
IoU(sr, gr)


    
    
 