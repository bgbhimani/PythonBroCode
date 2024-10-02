import datetime as dt

# date = dt.date(2025,1,2)
# today = dt.date.today()
# print("Today =",today)
# print(date)

time = dt.time(12,3,45) 
print(time)
now = dt.datetime.now()
print(now)

# String formation of time 
now = now.strftime("%H:%M:%S %d-%m-%y")
print(now)

# See if target datetime is passed the datetime or not
target_datetime = dt.datetime(2025,9,13,12,11,15)
current_datetime = dt.datetime.now()

if target_datetime < current_datetime:
    print("The targeted Date Passed")
else:
    print("Your Targeted Date is not Passed")
    