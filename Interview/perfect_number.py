def func(n):
    l = list()
    for i in range(1, n+1//2):
        if n%i == 0:
            l.append(i)
    return sum(l)
for j in range(1, 10001):
    x = func(j)
    if j == x:
        print(j, x)