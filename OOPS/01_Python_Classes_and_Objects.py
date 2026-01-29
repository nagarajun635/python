class MyClass:
    x = 5

print(MyClass)
print(MyClass.x)
p1 = MyClass()
p2 = MyClass()
print(p1.x)
print(p2.x)
del p1
print(p1.x)

