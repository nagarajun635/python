print('Hello')
print("It's alright")

x = "Hello!"
print(x)

x = """Hello"""
print(x)
x = 'Hello'
print(x)

a = "Hello"
print(a[1:5])

for x in a:
    print(x, end=' ')

print(len(a))

txt = "free bus is always free"
print('bus' in txt)
print('bus' not in txt)
if 'bus' in txt:
    print('I"m there.')
if '-' not in txt:
    print('I"m not there.')

txt = " Hello, World! "
print(txt[2:])
print(txt[:4])
print(txt[-4:-1])
print(txt[-5:])

print(len(txt.upper()))
print(len(txt.lower()))
print(len(txt.strip()))
print(txt.replace('H', 'C'))
print(txt.split(','))

a = 'Hello'
b = 'World'
c = a + b
print(c)
c = a + ' ' + b
print(c)

age = 29
print(f'My name is naga, and I am {age} years old.')

price = 59
print(f'The price is {price} dollars.')
print(f'The price is {price:.2f} dollars.')
print(f'The price is {10 * price:.2f} dollars.')

print("This is nagaraju")
print("This is \\nagaraju")
print("This is \'nagaraju")
print("This is \"nagaraju")
print("This is \'nagaraju")
print("This is \tnagaraju")
print("This is \rnagaraju")

stri = 'this \t is for string functions for {age}'
print(stri.capitalize())
print(stri.casefold())
print(stri.center(100))
print(stri.count('f'))
print(stri.endswith('for'))
print(stri.startswith('for'))
print(stri.expandtabs(10))


print(stri.find(' is'))
print(stri.rfind('is'))
try:
    if stri.index('b'):
        print('b is there')
except ValueError:
    print('the substring is not found')

print(stri.format(age=30))
txt = 'this is {name}, action is {action}'
data = {'name': 'nagaraju', 'action' :'coding'}
print(txt.format_map(data))

x = '123as'
y = '123'
z = 'as'
print(x.isalnum())
print(y.isdigit())
print(y.isdecimal())
print(y.isnumeric())
print(z.isalpha())
print(x.isascii())
print(z.isidentifier())
print(z.islower())
print(z.isupper())
print(z.isspace())
print(z.isprintable())
print(z.istitle())

x = ['apple', 'banana', 'cherry']
print('-'.join(x))

x = 'this is string'
print(x.ljust(1000), 'this ljust')
print('this rjust', x.rjust(1000))

x = ' this is lstrip and rstrip '
print(x.strip())
print(x.lstrip())
print(x.rstrip())

x = 'this is isis'
print(x.partition(' is '))
print(x.rpartition('is'))
print(x.title())
print(x.swapcase())
x = '50'
print(x.zfill(10))
txt = 'This is \na string \n contains new lines'
print(txt.splitlines())
print(stri.upper())
print(stri.lower())

print(stri.strip())
print(stri.lstrip())
print(stri.rstrip())
