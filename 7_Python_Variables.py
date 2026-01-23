x = 5
y = 'Nagaram'
print(x)
print(y)

x = 5
x = 'Nagaram'
print(x)

x, y, z = int(1), float(1), str(1)
print(x, y, z)
print(type(x), type(y), type(z))

x = 'Nagaram'
print(type(x))
x = "Nagaram"
print(type(x))

a = 5
A = 'Nagaram'
print(a, A)

# 2mayvar = 'nagaram'
# my var = 'nagaram'
# my-var = 'nagaram'

# this is camel case
thisIsVariable = "camel"
print(thisIsVariable)

# this is pascal case
ThisIsVariable = "pascal"
print(ThisIsVariable)

# this is snake case
this_is_snake = "snake"
print(this_is_snake)

fruits = ['apple', 'banana', 'orange']
x, y, z = fruits
print(x, y, z)

x = y = z = 'fruits'
print(x, y, z)

x = 'naga'
def mine():
    # global x
    x = 'raju'
    print(x)
mine()
print(x)