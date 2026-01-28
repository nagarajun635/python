try:
    print(x)
except:
    print("NameError")

try:
    print(x)
except NameError:
    print("NameError")
except:
    print("NormalError")

try:
    print('Hello')
except:
    print("Something went wrong")
else:
    print("Else part executed")

def divide_hundred():
    try:
        # val = int(input("Enter a number: "))
        val = 10
        divide = 100 // val
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Can't divide with zero")
    else:
        print(f"The result is {divide}")
    finally:
        print("Operation completed")
divide_hundred()

try:
    f = open("test.txt",'r')
    try:
        f.writelines('Hello')
    except:
        print("While writing file error occured")
    finally:
        f.close()
except:
    print("Unable to open file")