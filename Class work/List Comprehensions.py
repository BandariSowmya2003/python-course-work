#List Comprehensions

#1.
l=[]
for i in range(5):
    l.append(i)

ul=[i for i in range(5)]
print(l,ul)

#Output:
'''
[0, 1, 2, 3, 4] [0, 1, 2, 3, 4]

'''

#2.
even=[]
n=20
for i in range(1,n+1):
    if i%2==0:
        even.append(i)

ueven=[i for i in range(1,n+1) if i%2==0]
print(even,ueven)

#Output:
'''
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20] [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
#3.
l=[1,2,3,4,5,6,7]
res=[]
for i in l:
    if i%2==0:
        res.append("Even")
    else:
        res.append("Odd")

ures=["Even" if i%2==0 else "Odd" for i in l]
print(res,ures)

#Output:
'''
['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

'''

#4.
l=[[1,2],[3,4],[5,6],[7,8]]
'''
0=1+2=3
1=3+4=7
2=11
3=15
'''
res=[]
for i in l:
    res.append(sum(i))
ures=[sum(i) for i in l]
print(res,ures)

#Output:
'''
[3, 7, 11, 15] [3, 7, 11, 15]

'''
#5.
l=[1,2,3,4]
res=[]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        res.append((l[i],l[j]))

ures=[(l[i],l[j]) for i in range(len(l)-1) for j in range(i+1,len(l))]
print(res,ures)

#Output:
'''
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

'''

#6.
s=set()
for i in range(1,11):
    s.add(i)

us=[i for i in range(1,11)]
print(s,us)

#Output:
'''
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
#7.
d={}
for i in range(1,10):
    d[i]=i*i

ud=[i*i for i in range(1,10)]
print(d,ud)

#Output:
'''
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
[1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
