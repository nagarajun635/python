# l = []
# for i in range(20):
#     if i <= 1:
#         l.append(i)
#     else:
#         l.append(l[i-1]+l[i-2])
# print(l)

# def my_fib(n):
#     l = []
#     for i in range(n):
#         if i <= 1:
#             l.append(i)
#         else:
#             l.append(l[i-1]+l[i-2])
#     return l
# print(my_fib(20))

def my_fib(n):
  if n<=1:
    return n
  else:
    return(my_fib(n-1)+my_fib(n-2))
n=20
for i in range(n):
  print(my_fib(i))