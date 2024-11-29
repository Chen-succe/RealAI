import os
a = u'中文'
print(a)
print(type(a))
print(type('中文'))
print(u'中文' == '中文')
print(b'zhongwen')
print(b'zhongwen'.decode('ascii'))  # ascii 包含在utf-8中。
print(b'zhongwen'.decode('utf-8'))

