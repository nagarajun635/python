n1 = [1,1,5,4,5,5,'i',3,4,2]
n = [i for i in n1 if isinstance(i, int)]
print(n)
dup = set()
for i in n:
    j = n.count(i)
    if j>1 and i not in dup:
        print(i, j)
        dup.add(i)