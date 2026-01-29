class Outer:
    def __init__(self):
        self.name = 'Outer'

    class Inner:
        def __init__(self):
            self.name = 'Inner'

        def display(self):
            print("This is from Display")
outer = Outer()
print(outer.name)

inner = outer.Inner()
inner.display()

class Outer:
    def __init__(self):
        self.name = 'Outer'

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f"This is from Display from Inner Accessing Outer: {self.outer.name}")
outer = Outer()
inner = outer.Inner(outer)
inner.display()

class Computer:
    def __init__(self):
        self.ram = self.RAM()
        self.cpu = self.CPU()

    class RAM:
        def store(self):
            print("storing data...")

    class CPU:
        def process(self):
            print("Processing data...")
comp = Computer()
comp.cpu.process()
comp.ram.store()


