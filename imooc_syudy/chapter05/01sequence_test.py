# create by 'yang' in 2018/7/9 
__author__ = 'yang'

from collections import abc

a = [1, 2]
c = a + [3, 4]

print(c)
a1 = [1, 2]
a1 += [3, 4]
print(a1)

a2 = [1, 2]
a2 += (3, 4)
print(a2)

# +=调用了一个魔法函数 __iadd__
a3 = [1, 2]
a3.extend(range(3))  # 直接在a3上做修改，没有返回值
print(a3)

a4 = [1, 2]
a4.append([3, 4])
print(a4)
