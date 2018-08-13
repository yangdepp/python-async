class BaseMode:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        print('i am save')
        pass


class User(BaseMode):
    name = 'yang'
    age = 20

    class Meta:
        db_table = 'user'


if __name__ == '__main__':
    pass
    user = User(name='yang', age=20)
    user.save()