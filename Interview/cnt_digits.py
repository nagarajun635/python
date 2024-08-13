n = 1234567
cnt = 0
while n>0:
    dig = n%10
    cnt +=1
    n //= 10
print(cnt)