import random
x = 1
y = 2.8
z = 1j
print(type(x), type(y), type(z))

print(complex(x), complex(y), complex(z))
print(type(complex(x)), type(complex(y)), type(complex(z)))

print(int(x), int(y)) # , int(z))
print(type(int(x)), type(int(y))) # , type(int(z)))

print(float(x), float(y)) #, float(z))
print(type(float(x)), type(float(y))) #, type(float(z)))

print(random.randrange(1,100))