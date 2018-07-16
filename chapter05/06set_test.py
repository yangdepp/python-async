# create by 'yang' in 2018/7/10 
__author__ = 'yang'

s1 = set('abcde')
print(s1)

s2 = set(['a', 'b', 'c', 'd', 'e'])
print(s2)

s3 = {'a', 'b'}
s3.add('c')
print(s3)

# 不可变，可作为dict的值
s4 = frozenset('abcde')
print(s4)

s5 = set('def')
s6 = set('abc')
s6.update(s5)
print(s6)

# 有返回值，不改变s6的值
result = s6.difference(s4)
print(result)