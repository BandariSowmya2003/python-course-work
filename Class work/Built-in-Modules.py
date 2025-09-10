#Built-in-Modules
#Sys module

#1.
import sys

print(sys.argv)
#Output:['C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\Modules.py']

#2.
import sys

print(sys.path)

#Output:
['C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\idlelib',
 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip',
 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\DLLs',
 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\Lib',
 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313',
 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']

#3.
import sys

print(sys.version)

#Output:
3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]

#4.
import sys

print("Before exit")
print(sys.exit())
print("After exit")
#Output:
Before exit

#2.Platform Modules
import platform
print(platform.system())#Windows
print(platform.release())#11
print(platform.processor())#Intel64 Family 6 Model 142 Stepping 12, GenuineIntel

#3.Math Modules
import math
print(math.pi)#Output:3.141592653589793
print(math.e)#Output:2.718281828459045
print(math.sqrt(49))#Output:7.0
print(math.pow(2,3))#Output:8.0

print(round(31.2))#31
print(round(41.7))#42

print(math.ceil(23.5))#24
print(math.ceil(12.3))#13
print(math.ceil(14.7))#15

print(math.floor(11.4))#11
print(math.floor(4.33333))#4
print(math.floor(13.4))#13

print(abs(-13))#13
print(abs(-12.3))#12.3

print(math.fabs(-13))#13.0
print(math.factorial(5))#120
print(math.gcd(9,27))#9

print(math.log(2))#0.6931471805599453
print(math.log(2,2))#1.0
print(math.sin(45))#0.8509035245341184
print(math.cos(45))#0.5253219888177297
print(math.tan(45))#1.6197751905438615

print(math.degrees(45))#2578.3100780887044
print(math.radians(45))#0.7853981633974483

#4.Random module
import random

random.seed(10)

print(random.random())#0.11915781930872604

print(random.randint(1,9))#3
print(random.uniform(1,7))#3.1959610524159165

l=["Jyothsna","Madhavi","Sowmya","Akshaya"]
print(random.choice(l))#Jyothsna

print(random.choices(l,k=2))#['Jyothsna', 'Akshaya']

print(l)#['Jyothsna', 'Madhavi', 'Sowmya', 'Akshaya']

random.shuffle(l)
print(l)#['Madhavi', 'Jyothsna', 'Akshaya', 'Sowmya']

#5.Itertools.

from itertools import combinations,permutations

s='abcdef'
t=tuple(combinations(s,2))
p=tuple(permutations(s,3))

for i in t:
    print(''.join(i),end=',')

print()#Output:ab,ac,ad,ae,af,bc,bd,be,bf,cd,ce,cf,de,df,ef,

for i in p:
    print(''.join(i),end=',')

#Output:
abc,abd,abe,abf,acb,acd,ace,acf,adb,adc,ade,adf,aeb,aec,aed,aef,afb,afc,afd,
afe,bac,bad,bae,baf,bca,bcd,bce,bcf,bda,bdc,bde,bdf,bea,bec,bed,bef,bfa,bfc,
bfd,bfe,cab,cad,cae,caf,cba,cbd,cbe,cbf,cda,cdb,cde,cdf,cea,ceb,ced,cef,cfa,
cfb,cfd,cfe,dab,dac,dae,daf,dba,dbc,dbe,dbf,dca,dcb,dce,dcf,dea,deb,dec,def,
dfa,dfb,dfc,dfe,eab,eac,ead,eaf,eba,ebc,ebd,ebf,eca,ecb,ecd,ecf,eda,edb,edc,
edf,efa,efb,efc,efd,fab,fac,fad,fae,fba,fbc,fbd,fbe,fca,fcb,fcd,fce,fda,fdb,
fdc,fde,fea,feb,fec,fed,

#6.Deque,Defaultdict,Counter Modules

from collections import  deque,defaultdict,Counter

s=[1,2,3,2,4,3,5,6,2,1,2,5,3,5]

#1.
s='Hello World Python Program'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
#Output:
{'H': 1, 'e': 1, 'l': 3, 'o': 4, ' ': 3, 'W': 1, 'r': 3, 'd': 1, 'P': 2,
 'y': 1, 't': 1, 'h': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1}


#2.
feq=Counter(s)
print(feq)
#Output:
Counter({'o': 4, 'l': 3, ' ': 3, 'r': 3, 'P': 2, 'H': 1, 'e': 1, 'W': 1,
         'd': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1})


#3.
d=defaultdict(str)
d[1]=d[1]+"Sowmya"
print(d)#defaultdict(<class 'str'>, {1: 'Sowmya'})

#4.
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)
#Output:
defaultdict(<class 'int'>, {'H': 1, 'e': 1, 'l': 3, 'o': 4, ' ': 3, 'W': 1,
                            'r': 3, 'd': 1, 'P': 2, 'y': 1, 't': 1, 'h': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1})

#5.
from collections import  deque,defaultdict,Counter

d=deque()
d.appendleft(12)
d.pop()

d.append(12)
d.popleft()

print(d)#deque([])
