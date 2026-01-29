class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        print(self.__age)
    def set_age(self, age):
        self.__age = age
        return self.__age

p1 = Person("Naga", 29)
print(p1.name)
# print(p1._Person__age)
p1.get_age()
p1.set_age(30)
p1.get_age()

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num,(int, float)):
            return False
        return True
    def add(self, num):
        if self.__validate(num):
            self.result += num
        return self.result
c1 = Calculator()
c1.add(10)
print(c1.result)
c1.add(20)
print(c1.result)
c1.add(30)
print(c1.result)

