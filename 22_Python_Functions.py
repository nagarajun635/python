def myfunc():
    return print("Hello World myfunc")

myfunc()
myfunc()
myfunc()

def myFunc():
    return "Hello World myFunc"
print(myFunc())

def MyFunc():
    a = 1
    return a
print(MyFunc())

# Python Function Arguments
print('Python Function Arguments')

def myfunc(name):
    return f"Hello {name}"
print(myfunc("naga"))

def myfunc(fname, lname):
    return f"Hello {fname}, {lname}"

print(myfunc("naga", 'raju'))

def myfunc(country = 'india'):
    return f"Hello {country}"
print(myfunc('india'))
print(myfunc('paki'))

def myfunc(name, country):
    return f"Hello {name}, {country}"
print(myfunc(country='india', name='naga'))
print(myfunc('india', 'naga'))

def myfunc(name, age, country):
    return f"Hello {name}, {age}, {country}"
print(myfunc('naga', age=29, country='india'))

fruits = ["apple", "banana", "cherry"]
def myfunc(fun_fruits):
    for x in fruits:
        print(x)
myfunc(fruits)

def myfunc(x,y):
    return f"Hello {x}, {y}"
print(myfunc("apple", "banana"))

def myfunc():
    return "Hello World"
myfun = myfunc()
print(myfun[-1])

def myfunc(name, /):
    return f"Hello {name}"
print(myfunc("naga"))

def myfunc(*, name):
    return f"Hello {name}"
print(myfunc(name="naga"))

def myfunc(a, b, /, *, c, d):
    return f"Hello {a}, {b}, {c}, {d}"
print(myfunc(1,2,c=3, d=4))

# Python Arguments
print('Python Arguments')

def myfunc(*args):
    print(type(args))
    print(args[2])
    return f"Hello {args}"
print(myfunc('naga', 'raju', 'nagaraju'))

def myfunc(greet, *args):
    return [f'{greet}, {x}' for x in args]
print(myfunc('Hello', 'naga', 'raju', 'nagaraju'))

def myfunc(greet, *args, **kwargs):
    print(type(greet), type(args), type(kwargs))
    return f"Hello {greet}, {args}, {kwargs}"
print(myfunc('naga', 'raju', 'nagaraju', name='naga', age=29))

def myfunc(a, b, c):
    return a+b+c
data = [1,2,3]
print(myfunc(*data))

def myfunc(fname, lname):
    return f"Hello {fname}, {lname}"
dit = {'fname':'naga', 'lname':'raju'}
print(myfunc(**dit))

# Python Scope
print('Python Scope')
x = 'no func'
def myfunc(y):
    global x
    x = 'myfunc'
    print(x)
    def myfunc1():
        x = 'myfunc1'
        print(x)
        def myfunc2():
            print('before nonlocal')
            nonlocal x
            print('after nonlocal', x)
            x = 'myfunc2'
            print('after nonlocal assignment ', x)
            return x
        myfunc2()
        return x
    myfunc1()
    return x
print(myfunc(x))
print(x)

