n = '2,6,4,0,1,5'
l = list(map(int, n.split(',')))
print(l)
for i in l:
    if i % 2 == 0:
        print(i)