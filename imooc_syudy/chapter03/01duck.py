class Cat(object):
    def say(self):
        print('I am a cat')


class Dog(object):
    def say(self):
        print('I am a dog')

    def __getitem__(self, item):
        return 'dog'


class Duck(object):
    def say(self):
        print('I am a duck')


animal = Cat
animal().say()
print('-' * 50)

# 多态
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

print('-' * 60)

dog = Dog()
a = ['1', '2']
b = ['3', '4']
a.extend(dog)  # 必须传入一个可迭代对象
print(a)
