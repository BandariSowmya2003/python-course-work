#Control Statements

#1. For Loop Statements
seats={
    "U1":{'price':1029,'booking_status':True},
    "U2":{'price':1029,'booking_status':False},
    "U3":{'price':1029,'booking_status':True},
    "U4":{'price':1029,'booking_status':False},
    "L1":{'price':2029,'booking_status':True},
    "L2":{'price':2029,'booking_status':False},
    "L3":{'price':2029,'booking_status':True},
    "L4":{'price':2029,'booking_status':True},
    
    }
for i in seats:
    if seats[i]['booking_status']:
        print(f'{i}')
    else:
        print(f'{i}-{seats[i]["price"]}') #U1,U2-1029,U3,U4-1029,L1,L2-2029,L3,L4.
seatno=input("Enter the seat no: ").upper()
if seatno in seats:
    if seats[seatno]['booking_status']:
     print(f'{seatno} is already booked. Go for the other one!!') #U1=U1 is already booked. Go for the other one!!
    else:
        name=input('Enter the name: ').title()
        age=int(input('Enter your age: '))
        gender=input('Enter your gender(F or M): ').upper()
        if age<=5:
            print(f'Hello {name} your seat booked successfully with free of cost.')# L2=Madhubala,4,F=Hello Madhubala your seat booked successfully with free of cost.
        elif age<15:
            print(f'Hello {name} your seat booked successfully with 50% discount\nTotal Price={seats[seatno]["price"]*0.5}')#L2=Pooja,14,F=Hello Pooja your seat booked successfully with 50% discount
        else:
            print(f'Hello {name} your seat booked successfull. Pay the amount-{seats[i]["price"]}')#L2=Mahesh,21,M=Hello Mahesh your seat booked successfull. Pay the amount-2029
else:
    print('Enter the seat no properly') #L5=Enter the seat no properly

#2. Break Statements

n=int(input("Enter the number: "))
isprime=False
for i in range(2,n//2+1):
    if n%i==0:
        isprime=True
        break
if isprime:
    print("Not a prime number") #45=Not a prime number
else:
    print("prime number") #19=prime number


#count value
    
n=int(input("Enter the number: "))
c=0
for i in range(2,n//2+1):
    if n%i==0:
        c=1
        break
if isprime:
    print("Not a prime number") #6=Not a prime number
else:
    print("prime number") #5=prime number

#3. Continue Statements
# Print odd numbers only
for num in range(1,10):
    if num%2==0:
        continue
    print(num)#1,3,5,7,9