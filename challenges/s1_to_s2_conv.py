s1 = list('arjun')
s2 = list('bindu')
s3 = set(s2)
print(s1, s2, s3)
cst = 0
for i in s3:
    if i in s1:
        if s2.count(i) > s1.count(i):
            cst += s2.count(i)
    else:
        cst += 1
print(cst)
