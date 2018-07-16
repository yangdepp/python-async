# create by 'yang' in 2018/7/10
from datetime import date, datetime

__author__ = 'yang'


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('yang', date(year=1999, month=12, day=12))
    print(user.get_age())
    print(user.age)
    user.age = 10
    print(user._age)
    print(user.age)
