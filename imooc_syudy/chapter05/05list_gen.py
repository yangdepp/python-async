
# create by 'yang' in 2018/7/9
__author__ = 'yang'

odd_list = []
for i in range(21):
    if i % 2 == 1:
        odd_list.append(i)

print(odd_list)

print('-' * 50)
odd_list1 = [i for i in range(21) if i % 2 == 0]
print(odd_list1)
print(type(odd_list1))

print('-' * 50)


# 逻辑复杂的情况
def handle_item(item):
    return item * item


odd_list2 = [handle_item(item) for item in range(21) if item % 2 == 0]
print(odd_list2)

# 列表生成式性能高于列表操作

# ------------------------------------------------------------------
print('#' * 50)
# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 == 0)
print(type(odd_gen))  # <class 'generator'>
# generator可以通过for循环的方式打印出来
for item in odd_gen:
    print(item)
print('-' * 50)
# 可以通过list改造成一个list
odd_gen1 = (i for i in range(21) if i % 2 == 0)
odd_list3 = list(odd_gen1)
print(odd_list3)

# ------------------------------------------------------------------
# 字典推导式
print('#' * 50)
my_dict = {'yang': 25, 'deng': 24, 'imooc': 'good'}
# 将key和value换位
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)

# ------------------------------------------------------------------
# 集合推导式
print('#' * 50)
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)

my_set1 = set(my_dict.keys())
print(my_set1)