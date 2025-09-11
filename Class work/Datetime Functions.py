#date functions
from datetime import date,time,datetime,timedelta
today=date.today()
print(today)#2025-09-09
print(today.year)#2025
print(today.month)#9
print(today.day)#9
print(today.weekday)#<built-in method weekday of datetime.date object at 0x000001828AF91D70>
print(today.isoweekday())#2
print(date(2003,7,18))#2003-07-18

#time function
print(time(12,30,12))#12:30:12

#datetime function

now=datetime.now()
print(now)#2025-09-09 23:06:36.766573
print(now.year)#2025
print(now.month)#9
print(now.day)#9
print(now.hour)#23
print(now.minute)#6
print(now.second)#36


#strftime function
print(now.strftime('%y-%m-%d'))#25-09-09
print(now.strftime('%d/%m/%y'))#09/09/25
print(now.strftime('%d/%m/%y %H:%M:%S'))#09/09/25 23:06:36
print(now.strftime('%b %d, %y %H:%M:%S'))#Sep 09, 25 23:06:36
print(now.strftime('%B %d, %y %H:%M:%S'))#September 09, 25 23:06:36
print(now.strftime('%B %d, %Y %H:%M:%S %p'))#September 09, 2025 23:06:36 PM
print(now.strftime('%a, %B %d, %Y %H:%M:%S %p'))#Tue, September 09, 2025 23:06:36 PM
print(now.strftime('%A, %B %d, %Y %H:%M:%S %p'))#Tuesday, September 09, 2025 23:06:36 PM
print(now.strftime('%A, %B %d, %Y %I:%M:%S %p'))#Tuesday, September 09, 2025 11:06:36 PM

future=today-timedelta(weeks=10)
futureday=today-timedelta(days=10)


futuretime=now+timedelta(minutes=30)
futurehour=now+timedelta(hours=3)

print(future,futureday,futuretime,futurehour.strftime('%A, %B %d, %Y %I:%M:%S %p'))

#Output:
2025-07-01 2025-08-30 2025-09-09 23:36:36.766573 Wednesday, September 10, 2025 02:06:36 AM


