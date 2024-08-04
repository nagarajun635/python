ls = [2, 8, 6, 4, 5, 9, 7, 3, 1,0]
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i]>=ls[j]:
            ls[i], ls[j] = ls[j],ls[i]
print(ls)
