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

# Python Decorators
print('Python Decorators')

def changecase(x):
    def myinner(y):
        return x(y).upper()
    return myinner
@changecase
def myfunctio(x):
    return x
@changecase
def myfunctio2(x):
    return x
print(myfunctio2('naga'))
print(myfunctio('naga'))

import functools
def addit(func):
    @functools.wraps(func)
    def myinner(x):
        return len(func(x)) + 5
    return myinner
def subit(func):
    def myinner(x):
        return func(x)-1
    return myinner
@subit
@addit
def myplan(x):
    return 'Hello'
print(myplan('hel'))

# Python Lambda
print('Python Lambda')

x = lambda a: a*10
print(x(10))

def myfun(n,a):
    return (lambda n,a : n * a)(a,n)
print(myfun(n=5,a=5))

numbers = [1,2,3,4,5,6,7,8,9]
thribled = list(map(lambda x: x*3, numbers))
print(thribled)
odd_filter = list(filter(lambda x: x % 2 !=0, numbers))
print(odd_filter)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key = lambda x: len(x[0]))
print(sorted_students)

# Python Recursion
print('Python Recursion')

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

def countdown(n):
    if n<0:
        print('Done')
    else:
        print(n)
        countdown(n-1)

countdown(3)

def val():
    yield 1
    yield 2
    yield 3
for value in val():
    print(value)


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count+=1
for i in count_up_to(1):
    print(i)

def large_seq(n):
    for i in range(0,n):
        yield i
gen = large_seq(10000)
print(next(gen))
print(next(gen))
print(next(gen))

gen_exp = (x*x for x in range(8,10))
print(next(gen_exp))
gen_exp = sum(x*x for x in range(8,10))
print(gen_exp)

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

gen = fibonacci()
for _ in range(10):
    print(next(gen))


def genetr():
    while True:
        x = yield
        print(x)
gen = genetr()
next(gen)
gen.send('this is 1')
gen.send('this is 2')
gen.close()
gen.send(12)
