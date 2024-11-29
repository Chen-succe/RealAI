import os
from collections import defaultdict, namedtuple

Item = namedtuple('Item', ['path', 'label', 'fea'])

a = defaultdict(list)
print(a)
print(Item)
a[int(3)].append(Item('/ma/df', 4, 0.33))
print(a)