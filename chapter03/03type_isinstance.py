# 尽量用isinstance 而不用type

# 类变量和实例变量

class A:
    aa = 1

    # self这个类的实例
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
a.aa = 100  # 赋值只会赋给实例
print(a.x, a.y, a.aa)
print(A.aa)
# print(A.x)  # 会抛异常

# 修改了类的变量，所有的实例都会改变
