def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return 'user'

        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return 'company'

        return Company


def say(self):
    return 'I am user'
    # return self.name


class BaseClass:
    def answer(self):
        return "I am baseClass"


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


# 什么是元类，元类是创建类的类，type就是元类
# 定义类时，加上metaclass，可以控制User类实例化的过程
# 在类的实例化中，会首先寻找metaclass，通过metaclass去创建User类
class User(metaclass=MetaClass):
    pass


if __name__ == '__main__':
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)

    # User = type('User', (BaseClass,), {"name": "yang", "say": say})
    # my_obj = User()
    # print(my_obj.name)
    # print(my_obj.say())
    # print(my_obj.answer())

    user = User()
    print(user)