fruits = ["apple", "banana", "cherry"]
colors = ["red", "green", "blue"]
for x in fruits:
    if x == "apple":
        continue
    print(x)
for x in fruits:
    for y in colors:
        if y == "blue":
            break
        if y == "red":
            continue
        print(x, y)

for x in 'banana':
    print(x)

for i in range(0,100,10):
    print(i)
else:
    print("else")

for i in range(0,100,10):
    pass