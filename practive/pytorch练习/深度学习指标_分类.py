import numpy as np

def get_per_metric():
    # 真实值
    T = input('请输入正样本数量:')
    F = input('请输入负样本数量:')
    
    TP = int(input('实际为正样本，预测为正样本数量（TP）：'))
    TN = int(input('实际为负样本，预测为负样本数量（TN）：'))
    FP = int(input('实际为负样本，预测为正样本数量（FP）：'))
    FN = int(input('实际为正样本，预测为负样本数量（FN）：'))

    # 预测值
    P = TP + FP
    N = TN + FN 
    
    Acc = (TP + TN) / (FP + FN + TP + TN)
    precision = TP / (TP + FP)  # 预测值为正样本占所有预测值中正样本的比例，体现在预测值中正样本的预测情况
    recall = Sensitive = TPR = TP / (TP + FN)  # 预测值为正样本占真实样本中正样本的比例，体现正样本的召回率。
    F1_socre = 2*TP / (FP + 2*TP + FN)
    Specifity = TN / (TN + FP)
    
    FPR = 1 - Specifity
    
    print('准确率:{}'.format(Acc))
    print('精确度:{}'.format(precision))
    print('召回率：{}'.format(recall))
    print('F1-score:{}'.format(F1_socre))
    print('Sensitive：{}'.format(Sensitive))
    print('Specifity：{}'.format(Specifity))
    print('真正例：{}'.format(TPR))
    print('假正例：{}'.format(FPR))
    
    
if __name__ == '__main__':
    get_per_metric()