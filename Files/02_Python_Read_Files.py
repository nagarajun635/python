f = open("demo.txt","r")
print(f.read())
f.close()

with open("demo.txt","r") as f:
    print(f.read(5))
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readline())
    print(f.readline())
    f.seek(0)
    for x in f:
        print(x)
    f.close()
