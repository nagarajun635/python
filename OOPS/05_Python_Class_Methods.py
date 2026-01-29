class Person:
    def __init__(self, name):
        self.name = name
    def greet(self, name):
        return f"Hello {self.name} {name}"
p1 = Person("Naga")
print(p1.greet(''))
print(p1.greet("Raju"))

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self, num1, num2):
        self.num1 = self.num1 + num1
        self.num2 = self.num2 + num2
        return self.num1, self.num2
    def __str__(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"
c1 = Calculator(1, 2)
print(c1)
c1.add(num1=3, num2=4)
print(c1)
print(c1.num1, c1.num2)
print(c1.add(c1.num1, c1.num2))

class Playlist:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)
        return self.items

    def show_songs(self):
        for item in self.items:
            print(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item,'removed')
        else:
            print("Item not in the list")

p1 = Playlist("Favourite")
p1.add('Rooba')
p1.show_songs()
p1.remove('Rooba')
p1.show_songs()
del p1.show_songs
p1.remove('Rooba')
p1.show_songs()