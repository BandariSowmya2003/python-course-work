#Input formatting

#String input
name=input('enter your name: ')
print(name)

#Integer input
quantity=int(input('enter the number of items: '))
print(quantity)

#Float input
price=float(input('enter the product price: '))
print(price)

#Input as List(space-seperated)
names=input('enter employee names(space-seperated):').split()
print(names)

#Input as List(comma-seperated)
tags=input('enter tags(comma-seperated):').split(',')
print(tags)

#List of integers
marks=list(map(int,input('enter marks: ').split()))
print(marks)

#List of Floats
weights=list(map(float,input('enter weights: ').split()))
print(weights)

#Tuple input
dimensions=tuple(map(int,input('enter length,width,height: ').split()))
print(dimensions)

#Set input
selected_ids=set(map(int,input('enter selected image IDs: ').split()))
print(selected_ids)

#Dictionary input using eval()
profile=eval(input('enter user profile as a dictionary: '))
print(profile)

#Multiple inputs with unpacking
username, password=input('enter username and password: ').split()
print('username:', username)
print('password:', password)
