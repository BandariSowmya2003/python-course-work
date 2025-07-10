#5.Membership Operators
Name='Sowmya' #String
print('S' in Name)#True
print('z' not in Name)#True
print('x' in Name)#False

l=['Jyothsna','Madhavi','Kusuma','Nagashilpa']#List
print('Madhavi' in l)#True
print('Akhila' not in l)#True
print('Bhargavi' in l)#False

t=(1,2,3,4,5,6,7,8)#Tuple
print(3 in t)#True
print(10 in t)#False
print(9 not in t)#True

s={'book','car','mobile','laptop'}#Set
print('book' in s)#True
print('pen' not in s)#True
print('mobile' not in s)#False

data={'Name':'Sowmya','batch':'pfs','age':'21'}#Dictionary
print('Name' in data)#True
print('dob' in data)#False
print('year' not in data)#True