#Lambda Functions
def update(n):
    return n+10
print(update(10)) #20
update=lambda n:n+10
print(update(30)) #40

def square(n):
    return n**2
print(square(5)) #25
square=lambda n:n**2
print(square(7)) #49

evenorodd=lambda n:"Even" if n%2==0 else "Odd"
print(evenorodd(23)) #Odd
print(evenorodd(30)) #Even

#var=lambda para/argv : Exp
u=lambda n : n+10
print(u(10)) #20

cube=lambda n:n**3
print(cube(5)) #125


s= lambda s: s[0]
print(s("python")) #p
print(s("Lambda")) #L


add=lambda a,b: a+b
print(add(10,20)) #30
print(add(100,20)) #120


greater=lambda a,b: a if a>b else b
print(greater(10,20)) #20
print(greater(100,20)) #100


evenorodd= lambda n : "Even" if n%2==0 else "Odd"
print(evenorodd(15)) #Odd
print(evenorodd(130)) #Even

sumof3num= lambda a,b,c: a+b+c
print(sumof3num(30,40,20)) #90

#map,filter,reduce

s='python programming'
changestr= list(map(lambda i:i.upper(),s))
print(changestr)#['P', 'Y', 'T', 'H', 'O', 'N', ' ', 'P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']

asci=list(map(lambda i:ord(i),s))
print(asci)#[112, 121, 116, 104, 111, 110, 32, 112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]

vol='aeiouAEIOU'
frmt=list(map(lambda i:'*' if i in vol else '0',s))
print(frmt)#['0', '0', '0', '0', '*', '0', '0', '0', '0', '*', '0', '0', '*', '0', '0', '*', '0', '0']

ffmrt=list(filter(lambda i: i in vol ,s))
print("Filter:",ffmrt)#Filter: ['o', 'o', 'a', 'i']

cfmrt=list(filter(lambda i: i not in vol ,s))
print("Filter:",cfmrt)#Filter: ['p', 'y', 't', 'h', 'n', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g']


l=[1,2,3,4,5,6,7,8,9,10]
lstup=list(map(lambda i:i+1,l))
print(lstup)#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

elst=list(filter(lambda i: i%2==0,l))
print("Even using filter: ",elst)#Even using filter:  [2, 4, 6, 8, 10]

olst=list(filter(lambda i: i%2!=0,l))
print("Odd using filter: ",olst)#Odd using filter:  [1, 3, 5, 7, 9]

t=(20,40,30,50,12,34,24,89)
tupup=tuple(map(lambda i:i//10,t))
print(tupup)#(2, 4, 3, 5, 1, 3, 2, 8)

divtup=tuple(filter(lambda i: i%10==0, t))
print("Using Filter: ",divtup)#Using Filter:  (20, 40, 30, 50)

s={'python','html','css','java','mysql'}
setup= set(map(lambda i:i.upper(),s))
print(setup)#{'CSS', 'HTML', 'JAVA', 'MYSQL', 'PYTHON'}

stset=set(filter(lambda i:i.startswith('p'),s))
print(stset)#{'python'}

d={1:"afrin",2:"ramya",3:'Keerthana',4:'revathi',5:'sunitha'}
dup=list(map(lambda i:d[i].title(),d))
print(dup)#['Afrin', 'Ramya', 'Keerthana', 'Revathi', 'Sunitha']

products={'mouse':10,'keyboard':0,'laptops':30,'phone':0,'charger':13}
prodisplay=list(filter(lambda i:products[i]>0,products))
print(prodisplay)#['mouse', 'laptops', 'charger']

from functools import reduce

l=[1,2,3,4]
suml=reduce(lambda s,a:s+a,l)
print("Reduce:",suml)#Reduce: 10

s={'python','html','css','java','mysql'}
names=reduce(lambda n,name: n+' '+name,s)
print(names)#java html python mysql css

t=(1,2,3,4,5)
product=reduce(lambda pro,item: pro*item,t)
print(product)#120

d={'mysql':90,'python':80,'java':70,'html':80}
sumup=reduce(lambda s,i: str(s)+str(d[i]),d )
print(sumup)#mysql807080