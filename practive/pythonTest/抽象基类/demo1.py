from abc import abstractmethod, ABC


class a(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #@abstractmethod
    def eat(self):
        print(self.name + 'can eat')


class b(a):
    def run(self):
        print('I can run')


bb = b('bob', 13)
bb.run()
