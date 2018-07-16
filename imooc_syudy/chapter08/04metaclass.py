# create by 'yang' in 2018/7/11 
__author__ = 'yang'


# 一般情况下，先定义类，就可以根据这个类创建出实例，所以，先定义类，再实例创建
# 我们想创建出类，就必须根据metaclass创建出类。先定义metaclass,然后创建类


# 下面的例子可以给自定义的MyList增加一个add方法

# metaclass是类的模板，必须从'type'派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
# 传入关键字参数metaclass时，魔术就生效了，它指示python解释器在创建MyList时，通过ListMetaclass.__new__创建

class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
L.add(2)
L.reverse()
print(type(L))
print(L)
