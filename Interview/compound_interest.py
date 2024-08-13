principal = 10000
rate = 18
time = 2
amount = principal * (pow((1 + rate / 100), time))
interest = amount - principal
print(f'{interest:.2f}')
