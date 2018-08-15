class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)

        return super().__new__(cls, name, bases, attrs)


class List(list, metaclass=ListMetaclass):
    pass


if __name__ == '__main__':
    list = List()
    list.add(1)
    print(list)
