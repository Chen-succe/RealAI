import os

path = r'F:\Datas\ages_data\ages.txt'
# print(type(path))
# print(path)
# print(os.path.exists(path))
with open(path, 'r') as f:
    cont = f.readlines()
    for i in cont:
        # print(i)
        pt = r'{}'.format(i).replace('/f/','F:\\').replace('/', '\\').strip()  # 不要哦忽略空格符。
        # print(pt)  # F:\Datas\ages_data\UTKface\part1\part1\20_1_0_20170103175636647.jpg
        # print(type(pt))
        # print(os.path.exists(pt))
        # exit()
        