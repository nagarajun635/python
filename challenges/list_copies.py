l1 = ['naga', 'raju', 'bindu', 'madhavi']
l2 = l1
l3 = l1[:]
print(l1, l2, l3)
sums = 0
l2[0] = 'nag'
l3[1] = 'madhu'
print(l1, l2, l3)
for i in (l1,l2,l3):
    if i[0] == 'nag':
        sums += 1
    if i[1] == 'madhu':
        sums += 10
print(sums)