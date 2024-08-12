import sys

print(sys.version)

name = 'raju'
age = 27
print('nama is {0} age is {1}'.format('naga', 27))
print('nama is %s age is %d' % ('naga', 27))
print(f'name is {name} age is {age}')

i = 1234.2345
print('{:.8f}'.format(i))
print(f'{i:.7f}')
print('%.6f'%i)

print(36 % 4)
print(36 // 4)
