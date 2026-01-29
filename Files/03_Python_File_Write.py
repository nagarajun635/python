with open("demo.txt", "a") as file:
    file.write("Hello World")
    file.close()
with open("demo.txt", "r") as file:
    print(file.read())
    file.close()

with open("demo.txt", "w") as file:
    file.write("Oops I have deleted content!")
    file.close()
with open("demo.txt", "r") as file:
    print(file.read())
    file.close()
with open("demo.txt", "w") as file:
    file.write("")
    file.close()