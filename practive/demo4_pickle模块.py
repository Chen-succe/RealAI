import pickle

a = pickle.dumps(1, 2)
b = pickle.dumps((1,2))

with open('a.txt', 'wb') as af:
    af.write(a)

with open('b.txt', 'wb') as bf:
    bf.write(b)
    
with open('a.txt', 'rb') as af:
    a_ = af.read()
a_ = pickle.loads(a_)

with open('b.txt', 'rb') as bf:
    b_ = bf.read()
b_ = pickle.loads(b_)
# a_ = pickle.load(a, open('a.txt', 'wb'))
# b_ = pickle.load(b, open('b.txt', 'wb'))
# print(a.decode())
# print(b.decode())
print(a_)

print(b_)