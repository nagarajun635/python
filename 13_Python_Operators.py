print(10 + 5)

a, b = 100, 150
sum1 = a + b
print(sum1)
sum2 = sum1 + 150
print(sum2)

# Arithmetic Operators
print('Arithmetic Operators')
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 5)
print(10 % 5)
print(10 ** 2)

# Assignment Operators
print('Assignment Operators')
x = 5
print(x)
x += x
print(x)
x -= x
print(x)
print(x := 5)
x /= 2
print(x)
x = 5
x //= 2
print(x)
x = 5
x *= x
print(x)
x = 5
x **= 5
print(x)
x = 5
x %= 5
print(x)

x = 1
x &= 1
print(x)
x = 1
x |= 2
print(x)
x = 1
x ^= 2
print(x)

x = 5
x >>= 1
print(x)
x = 5
x <<= 1
print(x)

# Comparison Operators
print('Comparison Operators')
x = 5
y = 3
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)
print(x > y)

# Logical Operators
print('Logical Operators')
print(x > 1 and x < 6)
print(x < 1 or x < 6)
print(not(x < 1 or x < 6))

# Identity Operators
print('Identity Operators')
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is y)
print(x is not y)
print(x is z)
print(x is not z)

# Membership Operators
print('Membership Operators')
txt = 'Hello'
print('H' in txt)
print('z' not in txt)

# Bitwise Operators
print('Bitwise Operators')
print(1 & 2)
print(1 | 2)
print(1 ^ 2)
print(~(1|2))
print(2>>2)
print(2<<2)

