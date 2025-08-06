#1.Functions

data={'current_balance':5000,'history':[]}

def Menu():
    print('\n[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transaction History')
    print('[E]xit\n')


def Welcome():
    print('Welcome to ATM'.center(40,'*'))

def Check_Balance():
    print(f'Current_balance:${data["current_balance"]}')
    
def Withdraw():
    amount=int(input("Enter the amount to withdraw: "))
    if amount<=data['current_balance']:
        data['current_balance']-=amount
        data['history'].append(f'Withdraw: ${amount}')
        print(f'${amount} is successfully Withdraw!!!')
    else:
        print('Insufficient Balance')
        
def Deposit():
    amount=int(input("Enter the amount to Deposit: "))
    data['current_balance']+=amount
    data['history'].append(f'Deposited: ${amount}')
    print(f'${amount} is successfully Deposited!!!')
    
def View_History():
    if data['history']:
        print('Transaction History'.center(40,'-'))
        for i in data['history']:
            print(i)
        else:
            print("No Transactions")

def Flow_Check(ch):
    if ch=="C":
        Check_Balance()
    elif ch=="D":
        Deposit()
    elif ch=="W":
        Withdraw()
    elif ch=="V":
        View_History()


Welcome()
while True:
    Menu()
    ch=input("Enter the char[CDWVE]: ").upper()
    Flow_Check(ch)
    if ch=='E':
        print("Thank you".center(40,'.'))
        break
        
#Functional arguments:

#1.Positional Arguments:
def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")

student_details(name,rollno,marks,grade,student_course)
student_details("xyz",65,100,'A','Java')

#2.Keyword Arguments:
def function_name(agr1,agr2,agr3):
    #block of code
    function_name(agr1='val1',agr2='val2',agr3='val3')
    function_name(agr2='val1',agr1='val2',agr3='val3')

def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")

student_details(name=name,rollno=rollno,marks=marks,grade=grade,course=student_course)

student_details(rollno=rollno,name=name,grade=grade,course=student_course,marks=marks)

student_details(rollno=56,name='ramya',grade='A',course='Mysql',marks=99)



#3.Default Arguments:
def function_name(agr1,agr2,agr3='val3'):
    #block of code
    function_name(val1,val2)
    function_name(val3,val1)
    function_name(agr1,agr2,agr3)


def student_details(name,rollno,marks=0,grade="F",course='Python'):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
course=input("Course: ")

student_details(name,rollno)

student_details(name,rollno,marks)

student_details(name,rollno,marks,grade)

student_details(name,rollno,marks,grade,course)



#4.Variable Length:
def function_name(*agr):
    #block of code =>(tuple)
    function_name(val1,val2,val3,val4)
    function_name(val3,val1)
    function_name(agr1,agr2,agr3)
    function_name(agr1)


def names(*stdnames):
    print("\nName of students")
    for i in stdnames:
        print(f"**{i.upper()}**")

names('kalyan','Adarsh','saikumar')
names('kalyan','Adarsh','saikumar','nihitha','keethana','leorah')
names('kalyan','nihitha','keethana','leorah')
names('Ramya','nihitha','keethana','leorah')
names('Ramya','nihitha','keethana','Sunitha','maheswari')

def function_name(**agr):
    #block of code =>(dict)
    function_name(agr1='val1')
    function_name(agr2='val1',agr1='val2',agr3='val3')
    function_name(agr1='val2',agr3='val3')
    function_name(agr2='val1',agr1='val2',agr3='val3',agr4='val4')



def display_products(**product):
    print("\nProducts and Prices: ")
    for i in product:
        print(f'{i}: ${product[i]}')

display_products(laptop=60000,phone=35000,watch=15000,fridge=200000)
display_products(fashwash=600,perfume=2000,eyeliner=1500,powder=2500)
display_products(carrot=25,tomato=30,beetroot=40,apple=50)

#*************Welcome to ATM*************

#[C]heck Balance
#[D]eposit
#[W]ithdraw
#[V]iew Transaction History
#[E]xit

#Enter the char[CDWVE]: c
#Current_balance:$5000

#[C]heck Balance
#[D]eposit
#[W]ithdraw
#[V]iew Transaction History
#[E]xit

#Enter the char[CDWVE]: d   
#Enter the amount to Deposit: 5000
#$5000 is successfully Deposited!!!

#[C]heck Balance
#[D]eposit
#[W]ithdraw
#[V]iew Transaction History
#[E]xit

#Enter the char[CDWVE]: d 
#Enter the amount to Deposit: 4000
#$4000 is successfully Deposited!!!

#[C]heck Balance
#[D]eposit
#[W]ithdraw
#[V]iew Transaction History
#[E]xit

#Enter the char[CDWVE]: w
#Enter the amount to withdraw: 9900
#$9900 is successfully Withdraw!!!

#[C]heck Balance
#[D]eposit
#[W]ithdraw
#[V]iew Transaction History
#[E]xit

#Enter the char[CDWVE]: c
#Current_balance:$4100

#[C]heck Balance
#[D]eposit
#[W]ithdraw
#[V]iew Transaction History
#[E]xit

#Enter the char[CDWVE]: d   
#Enter the amount to Deposit: 4000
#$4000 is successfully Deposited!!!

#[C]heck Balance
#[D]eposit
#[W]ithdraw
#[V]iew Transaction History
#[E]xit

#Enter the char[CDWVE]: v
#----------Transaction History-----------
#Deposited: $5000
#Deposited: $4000
#Withdraw: $9900
#Deposited: $4000
#No Transactions

#[C]heck Balance
#[D]eposit
#[W]ithdraw
#[V]iew Transaction History
#[E]xit

#Enter the char[CDWVE]: e
#...............Thank you................
#Name: sowmya
#Roll no: 1
#Marks: 100
#Grade: A
#Course: Python
#Name: sowmya
#Rollno: 1
#Marks: 100
#Grade: A
#Course: Python
#Name: xyz
#Rollno: 65
#Marks: 100
#Grade: A
#Course: Java
#Name: Ganavi
#Roll no: 3
#Marks: 99
#Grade: A
#Course: Python
#Name: Ganavi
#Rollno: 3
#Marks: 99
#Grade: A
#Course: Python
#Name: Ganavi
#Rollno: 3
#Marks: 99
#Grade: A
#Course: Python
#Name: ramya
#Rollno: 56
#Marks: 99
#Grade: A
#Course: Mysql
#Name: Anjali
#Roll no: 2
#Marks: 80
#Grade: B
#Course: MBA
#Name: Anjali
#Rollno: 2
#Marks: 0
#Grade: F
#Course: Python
#Name: Anjali
#Rollno: 2
#Marks: 80
#Grade: F
#Course: Python
#Name: Anjali
#Rollno: 2
#Marks: 80
#Grade: B
#Course: Python
#Name: Anjali
#Rollno: 2
#Marks: 80
#Grade: B
#Course: MBA

#Name of students
#**KALYAN**
#**ADARSH**
#**SAIKUMAR**

#Name of students
#**KALYAN**
#**ADARSH**
#**SAIKUMAR**
#**NIHITHA**
#**KEETHANA**
#**LEORAH**

#Name of students
#**KALYAN**
#**NIHITHA**
#**KEETHANA**
#**LEORAH**

#Name of students
#**RAMYA**
#**NIHITHA**
#**KEETHANA**
#**LEORAH**

#Name of students
#**RAMYA**
#**NIHITHA**
#**KEETHANA**
#**SUNITHA**
#**MAHESWARI**

#Products and Prices:
#laptop: $60000
#phone: $35000
#watch: $15000
#fridge: $200000

#Products and Prices:
#fashwash: $600
#perfume: $2000
#eyeliner: $1500
#powder: $2500

#Products and Prices:
#carrot: $25
#tomato: $30
#beetroot: $40
#apple: $50