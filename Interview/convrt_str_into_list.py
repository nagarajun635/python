n = '10 1 2 5 8 9 '
l = list(map(int, n.split(' ')))
print(l)
mn = min(l)
mx = max(l)
for i in range(mn, mx):
    if i not in l:
        print(i)
