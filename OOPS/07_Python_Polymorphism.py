class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self, action):
        return self.brand, self.model, action
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self, action):
        return self.brand, self.model, action

x1 = Car('BMW',"X5").move('Drive')
x2 = Boat('Lanchi', "aplha").move('Swim')

for y in (x1, x2):
    print(y)

