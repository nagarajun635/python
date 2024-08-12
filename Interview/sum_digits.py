n = 7584
print(n)
rev = dig = 0
while n>0:
    dig = n%10
    print(n%10,n//10)
    rev = (rev * 10) + dig
    n=n//10
print(rev)
