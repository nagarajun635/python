# n = x = 370
# length = len(str(n))
# arm = 0
# while n > 0:
#     dig = n % 10
#     arm += (dig**length)
#     n //= 10
# if x == arm:
#     print('yes')
# else:
#     print('no')
n = 153
a = list(map(int,str(n)))
print(a)
b = list(map(lambda x: x**3,a))
print(b)