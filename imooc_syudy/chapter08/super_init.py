class B(type):
    print('b')


class BaseMode(metaclass=B):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        print(self)
        return super().__init__()

    def save(self):
        print('i am save')
        pass


class User(BaseMode):
    name = 'yang'
    age = 20

    class Meta:
        db_table = 'user'

# metaclass是在类生成过程中调用，因此上述代码会打印出'b'
