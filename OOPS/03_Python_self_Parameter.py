class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, Good Day {self.name}!'

    def welcome(self):
        message = self.greet()
        return message+'this is welcome method!'

p1 = Person("John", 25)
p2 = Person("Jane")
print(p1.name, p1.age, p1.greet(), p1.welcome())
print(p2.name, p2.age, p2.greet(), p2.welcome())

