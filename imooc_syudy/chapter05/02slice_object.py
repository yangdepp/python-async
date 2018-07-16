# create by 'yang' in 2018/7/9
import numbers

__author__ = 'yang'


# 创建一个支持切片操作的object
class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    # 是支持可切片的关键
    def __getitem__(self, item):

        # 传递的item是一个slice切片对象
        # 直接这么返回，则返回的是一个list类型，想要返回一个Group类型的对象
        # return self.staffs[item]

        # --------------------------
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    # 实现if in
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ['yang', 'deng', 'yang1', 'deng1']
group = Group(company_name='immoc', group_name='user', staffs=staffs)
staffs_group = group[:2]  # 现在返回的是一个list了，想要还是返回一个Group类型的对象
print(staffs_group)
print('-' * 50)
staffs_group1 = group[3]
print(staffs_group1)

if 'yang' in group:
    print('我在的')

for user in group:
    print(user)

print('-'*50)
reversed(group)
for user in group:
    print(user)