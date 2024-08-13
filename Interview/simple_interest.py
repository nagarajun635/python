from pendulum import date
principle = 100000
interest = 18
days = (date(year=2024, day=1, month=1) - date(year=2022, day=1, month=10)).in_days()
time = 1
day_inst = ((principle*interest*time)//100)//(date(year=2024, day=1, month=1) - date(year=2023, day=1, month=1)).in_days()
print(day_inst)
print(day_inst*days, days, day_inst)
