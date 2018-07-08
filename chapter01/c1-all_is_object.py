def ask(name="yang"):
    print('hello', name)


class Person:
    def __init__(self):
        print('yang')


obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())

my_func = ask
my_func('yang')
