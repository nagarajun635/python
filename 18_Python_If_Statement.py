a, b = 10, 20
if a<b:
 print("a is greater than b")

 is_logged_in = True
 if is_logged_in:
     print("logged in")
if 5:
    print("5 is greater than 5")
if False:
    print("False is greater than 5")
if "False":
    print("False is greater than 5")
a = b = 3
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
score = 65
if score >= 90:
    print("score is greater than 90")
elif score >= 80:
    print("score is less than 80")
elif score >= 70:
    print("score is greater than 70")
elif score >= 60:
    print("score is less than 60")
a, b = 33, 200
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")

if a < b: print("short hand if")

print('short hand ifelse') if a > b else print('short hand elseif')

a, b = 20, 20
bigger = a if a>b else b
print(bigger)

print('A') if a>b else print('=') if a==b else print('B')