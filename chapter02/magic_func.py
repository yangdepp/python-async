# python的魔法函数
# 字符串相关
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 隐含调用，但是必须用print方法
    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return ','.join(self.employee)


company = Company(['yang', 'deng', 'hahaha'])
company

print(company.__repr__())


# 数值计算相关
class NumberXY(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = NumberXY(self.x + other.x, self.y + other.y)
        return result

    def __str__(self):
        return 'x:{x}, y:{y}'.format(x=self.x, y=self.y)


my_number = NumberXY(1, 2)
my_number1 = NumberXY(2, 3)
print(my_number + my_number1)
