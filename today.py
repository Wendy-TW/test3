
import datetime
today = datetime.date.today()
print(today)                 # 2021-10-19
print(today.year)            # 2021
print(today.month)           # 10
print(today.day)             # 19
print(today.weekday())       # 1    ( 因為是星期二，所以是 1 )
print(today.isoweekday())    # 2    ( 因為是星期二，所以是 2 )
print(today.isocalendar())   # (2021, 42, 2)  ( 第三個數字是星期二，所以是 2 )
print(today.isoformat())     # 2021-10-19
print(today.ctime())         # Tue Oct 19 00:00:00 2021
print(today.strftime('%Y.%m.%d'))    # 2021.10.19

newDay = today.replace(year=2020)
print(newDay)                # 2020-10-19

current_date=str(today.year)+str(today.month)+str(today.day)

print(current_date)
print(str(today))
