day = 1
month = 0
match day:
    case 1|2|3|4|5 if month == 1:
        print('jan weekday')
    case 6|7 if month == 1:
        print('jan weekend')
    case _:
        print('bad day')

