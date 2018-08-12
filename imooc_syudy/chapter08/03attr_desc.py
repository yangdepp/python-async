from datetime import date, datetime
import numbers


# 属性描述符有两类，第一类实现get和set是数据描述符
class IntField:
    # 这个类实现下面三个方法中任意一个，就是属性描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if value < 0:
            raise ValueError('positive value need')

        self.value = value

    def __delete__(self, instance):
        pass


# 第二类是只实现get方法的非数据描述符
class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    # age是IntField实例对象
    # age = IntField()
    age = NonDataIntField()


if __name__ == '__main__':
    user = User()
    # 对age赋值时，会进入IntField对象中
    user.age = 19
    print(user.age)

# 属性查找的顺序
# 如果user是某个类的实例，那么user.age等价于getattr(user, 'age')
# 首先调用_getattribute__。如果类定义了__getattr__方法，
# 那么在__getattribute__抛出AttributeError的时候就会调用到__getattr__
# 而对于描述符(__get__)的调用，则是发生在__getattribute__内部的

# 1、 如果'age'是出现在User或其基类的__dict__中，且age是data descriptor，那么调用里面的get方法
# 2、 如果'age'出现在user的__dict__中，那么直接返回obj.__dict__，对象中的值
# 3、 如果'age'出现在User或者基类的__dict__中，类中的值
# 3.1 、如果age是非数据描述符，那么调用非数据描述符其__get__方法，否则
# 3.2 、如果不是非数据描述符，在类中直接赋值的，直接去__dict__中取，
# 4、 如果User中有__getattr__方法，调用__getattr__方法，否则抛出AttributeError
