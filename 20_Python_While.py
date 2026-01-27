i = 0
while i < 6:
    print(i)
    if i == 2:
        i += 1
        # continue
    if i == 5:
        i += 1
        # break
    i += 1
else:
    print('execution done')