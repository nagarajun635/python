x = 3
y = 12
# l1 = set(x*i for i in range(1, (x*y)))
# print(l1)
# l2 = set(y*i for i in range(1, (x*y)))
# print(l2)
# print(sorted(l1 & l2)[0])


lcm = max(x, y)  # Optimized
while True:
    if lcm % x == 0 and lcm % y == 0:
        break
    lcm += 1
print(lcm)
