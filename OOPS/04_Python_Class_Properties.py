class Person:

    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 29)
print(p1.species, p1.name, p1.age)
p1.age = 26
print(p1.name, p1.age)
# del p1.age
print(p1.name, p1.age)
Person.species = "Human!"
Person.color = "Black"
p2 = Person("Naga", 29)
print(p2.species, p2.name, p2.age, p2.color)

