# create by 'yang' in 2018/7/9 
__author__ = 'yang'

# bisect用来处理已排序的序列的查找模块
# 用来维持已排序的序列，升序
# 二分查找

import bisect

inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)

print(bisect.bisect(inter_list, 3))  # 返回应该插入的位置index 3,默认是bisect_right
print(bisect.bisect_left(inter_list, 3))  # 返回应该插入的位置的左边index 2

print(inter_list)  # 返回一个已排序的序列[1, 2, 3, 5, 6]
