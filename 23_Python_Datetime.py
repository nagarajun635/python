import datetime
from zoneinfo import ZoneInfo
print(datetime.datetime.now())
x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
print(x.isoweekday())
print(x.weekday())
print(x.strftime("%A"))

x = datetime.datetime(2026,1,25,18,15,15,151515,ZoneInfo('Asia/Kolkata'))
# weekday
print(x.strftime("%Y-%m-%d %H:%M:%S.%f"))
print(x.strftime("%a-%A-%w"))
# Day
print(x.strftime("%d"))
# Month
print(x.strftime("%b-%B-%w"))
# Year
print(x.strftime("%y-%Y"))
# Hour
print(x.strftime("%H-%I"))
# AM/PM
print(x.strftime("%p"))
# Timezone
print(x.strftime("%z-%Z"))
# Day number
print(x.strftime("%j"))
# Week number
print(x.strftime("%U-%W"))
# local version of time
print(x.strftime("%c->%x->%X"))
# Century
print(x.strftime("%C"))
# ISO 8601
print(x.strftime("%G-%u-%V"))

