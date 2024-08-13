# def func(dig):
#     y = 1
#     x = [i for i in range(1, dig+1)]
#     for j in x:
#         y *= j
#     return y
#
#
# n = x = 145
# stng = 0
# while n > 0:
#     dig = n % 10
#     stng = stng + func(dig)
#     n //= 10
# print(f'stng: {stng}, x is {x}')

def func(dig):
    y = 1
    x = [i for i in range(1, dig+1)]
    for j in x:
        y *= j
    return y
for j in range(100001):
    i = x = j
    stng = 0
    while i > 0:
        dig = i % 10
        stng = stng + func(dig)
        i //= 10
    if stng == x:
        print(f'stng: {stng}, x is {x}')