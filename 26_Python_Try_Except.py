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

# x = -1
# if x < 0:
#     raise Exception("Numbers not less than 0")

# x = 'hello'
# print(x, type(x), not type(x), type(x) is str, not type(x) is int)
# if not type(x) is int:
#     raise TypeError("Invalid Type")
# try:
#     f = open("test.txt",'rt')
#     try:
#         f.write('Hello')
#     except:
#         print("While writing file, error occured")
#     finally:
#         f.close()
# except:
#     print("Unable to open file")