#Simple If statement
num = 12
if num % 2 == 0:
    print("The number is even.")#The number is even.

#If-Else statement
balance = 5000
withdraw = 2000

if withdraw <= balance:
    print("Transaction Successful!")
else:
    print("Insufficient Balance!")#Transaction Successful!

#If-Elif-Else statement
temperature = 30

if temperature > 35:
    print("It's too hot! Stay hydrated.")
elif temperature >= 20:
    print("Weather is pleasant.")
elif temperature >= 10:
    print("It's cool, wear a jacket.")
else:
    print("Freezing! Stay indoors.")#Weather is pleasant.

#Nested-if statement
hr,mins=list(map(int,input('enter the HH:MM :').split(':')))
if hr>=0 and hr<=24 and mins>=0 and mins<=60:
    if hr>=0 and hr<4:
        print('Its high time.Time to sleep')
    if hr>=4 and hr<12:
        print('Good morning.Have a nice day')
    if hr>=12 and hr<16:
        print('Good afternoon.Have a great lunch')
    if hr>=16 and hr<20:
        print('Good evening.Have some snacks')
    if hr>=20 and hr<24:
        print('Good night.Sweet dreams')
else:
    print('Enter the proper input,Your input is invalid')#enter the HH:MM :21:38 Good night.Sweet dreams

