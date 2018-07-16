from sqlite3 import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1990, 2, 1))
    # 双下划线的私有属性，是不能直接访问的，只能通过类里面的公共的方法访问
    # print(user.birthday)
    # print(user._User__birthday)   #可以通过这个来访问私有属性
    print(user.get_age())
