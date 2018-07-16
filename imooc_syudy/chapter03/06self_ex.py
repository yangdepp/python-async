class Person:
    name = 'user'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student('慕课网')

    # 通过__dict__查询属性
    # {'school_name': '慕课网'}
    print(user.__dict__)
    user.__dict__['school_addr'] = '北京市'
    print(user.school_addr)

    print(Person.__dict__)

    print('-' * 50)
    print(dir(user))
    # dir函数只有key，没有value
