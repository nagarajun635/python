class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname, "This is from parent")
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.age = 18

    # def printname(self):
    #     return f"{self.firstname} {self.lastname} {self.age} years old This is from Child function"

    def __str__(self):
        return f"{self.firstname}{self.lastname} {self.age} years old This is from Child"

x = Person("Nagaraju", 'N')
x.printname()

y = Student("Naga", 'Raju')
y.printname()
print(y)
