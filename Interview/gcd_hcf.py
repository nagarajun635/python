# x = 10
# y = 20
# z = x if x > y else y
# for i in range(1,z):
#     if x%i == 0 and y%i == 0:
#         gcm = i
# print(gcm)
w = 4
x = 8
y = 16
z = x if x > y else y if y>w else w
for i in range(1,z):
    if x%i == 0 and y%i == 0 and w%i == 0:
        gcm = i
print(gcm)