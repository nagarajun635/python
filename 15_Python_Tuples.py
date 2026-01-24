mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))

thistuple = ('naga',)
print(type(thistuple))
thistuple = ('naga')
print(type(thistuple))
thistuple = 'naga',
print(type(thistuple))

mytuple = tuple(['apple', 'banana', 'cherry'])
print(mytuple)
mytuple = tuple(('apple', 'banana', 'cherry'))
print(mytuple)

# Access Tuple Items
print('Access Tuple Items')
print(mytuple[0])
print(mytuple[-1])
print(mytuple[-3:-1])
if 'apple' in mytuple:
    print(mytuple.index('apple'))
    print(mytuple.count('apple'))
    print(mytuple)

red, yellow, green = mytuple
print(red)
print(yellow)
print(green)
(red, *other) = mytuple
print(red)
print(other)

