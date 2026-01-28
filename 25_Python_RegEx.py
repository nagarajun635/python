import re


txt = 'The rain in Singapore'
x = re.search('^The.*Singapore$', txt)
print(x)
print("This is string: ", x.string)
print(x.group())
print(x.start())
print(x.end())
print(x.span())
if x:
    print('The string pattern found')
else:
    print('The string pattern not found')

y = re.findall(r'in', txt)
print(y)
y = re.findall(r'z', txt)
print(y)

z = re.split(r'\s', txt)
print(z)
z = re.split(r'\s', txt, 2)
print(z)

a = re.sub(r'\s', '-', txt)
print(a)
a = re.sub(r'\s', '-', txt, 1)
print(a)



