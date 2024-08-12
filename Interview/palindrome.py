n0 = n1 = 1234
n2 = dig = 0
while n1 > 0:
    dig = n1 % 10
    n2 = (n2 * 10) + dig
    n1 = n1 // 10
print(n0, n1, n2)
if n0 == n2:
    print('yes')
else:
    print('no')
n0_str = str(n0)
n2_str = str(n2)
length = len(n0_str)
for i in range(length):
    if n0_str[i] == n2_str[length - 1 - i]:
        print(i, length - 1 - i)
        # print(f"Digit {i+1} of n0 ({n0_str[i]}) is equal to digit {length-i} of n2 ({n2_str[length-1-i]}).")
        print(n0_str[i], n2_str[length - 1 - i])
    else:
        print(f"Digit {i + 1} of n0 ({n0_str[i]}) is NOT equal to digit {length - i} of n2 ({n2_str[length - 1 - i]}).")
