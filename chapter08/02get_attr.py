# create by 'yang' in 2018/7/10 
__author__ = 'yang'

# __getattr__ -在查找不到属性的时候使用


from datetime import date


class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    # 查找不到的时候用这个魔法函数
    def __getattr__(self, item):
        return self.info[item]


if __name__ == '__main__':
    user = User('yang', date(year=1999, month=12, day=12), info={'company_name': 'imooc'})
    print(user.company_name)
