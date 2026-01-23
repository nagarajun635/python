print(13>9)
print(13 == 9)
print(13<9)

a,b  = 100, 200
if a > b:
    print('a > b')
else:
    print('a < b')

print(bool('Hello'))
print(bool(23))
print(bool(a))
print(bool(b))

print(bool(None))
print(bool([]))
print(bool({}))
print(bool(''))

class MyClass:
    def myfunc(self):
        return 0
myobj = MyClass()
print(bool(myobj))

def myfunc2():
    return 0
print(myfunc2())

def myfunc3():
    return 1
print(myfunc3())

def myfunc4():
    return False
print(myfunc4())

def myfunc5():
    return True
print(myfunc5())

def myfunc6():
    return None
print(myfunc6())

def myFunction():
    return False
if myFunction():
    print('Success')
else:
    print('Fail')

print(isinstance('20',str))