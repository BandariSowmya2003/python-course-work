#1.Creating Lists
#1.1 Empty list
list = []
print(list)#[]

#1.2 List with Elements
l=[1,3,2,4,5,6]
print(type(l))#<class 'list'>
l=['apple','banana','mango','cherry']
print(type(l))#<class 'list'>
l=[5,'Codegnan',2.67,True,3+6j]
print(type(l))#<class 'list'>

#1.3 Nested Lists
nested_list=[[1,4,2,5,6,], ['p','q','r'],[True,False]]
print(type(nested_list))#<class 'list'>

#2.Accessing Elements
#2.1 Indexing(positive & negative)
l=['java','database','python']
print(l[0])#java
print(l[-1])#python
print(l[1])#database

#2.2 Slicing
l=[1,2,3,4,5,5,7,8,5,4,3,9]
print(l[1:5])#[2,3,4,5]
print(l[:4])#[1,2,3,4]
print(l[5:])#[5,7,8,5,4,3,9]
print(l[-5:-1])#[8, 5, 4, 3]
print(l[::-1])#[9, 3, 4, 5, 8, 7, 5, 5, 4, 3, 2, 1]

#3. Modify List
#3.1 Changing elements
l=[20,40,60,80]
l[2]=50
print(l)#[20,40,50,80]

#3.2 Adding elements
l=[1,2,3,4,5,5,7,8,5,4,3,9]
#append
l.append(10)
print(l)#[1, 2, 3, 4, 5, 5, 7, 8, 5, 4, 3, 9, 10]
#insert
l.insert(1,7)
print(l)#[1, 7, 2, 3, 4, 5, 5, 7, 8, 5, 4, 3, 9, 10]
#extend
l.extend([2])
print(l)#[1, 7, 2, 3, 4, 5, 5, 7, 8, 5, 4, 3, 9, 10, 2]

#3.3 Removing Elements
l=[1,2,3,4,5,5,7,8,5,4,3,9]
#remove
l.remove(5)
print(l)#[1, 2, 3, 4, 5, 7, 8, 5, 4, 3, 9]
#pop
l.pop(2)
print(l)#[1,2,4,5,7,8,5,4,3,9]
l.pop()
print(l)#[1, 2, 4, 5, 7, 8, 5, 4, 3]
#delete
del l[3]
print(l)#[1, 2, 4, 7, 8, 5, 4, 3]
#clear
l.clear()
print(l)#[]

#4.List Methods
#append
l=[1,2,3,4,5,5,7,8,5,4,3,9]
l.append(7)
print(l)#[1, 2, 3, 4, 5, 5, 7, 8, 5, 4, 3, 9, 7]
#extend
l=[1,2,3,4,5,5,7,8,5,4,3,9]
l.extend([6])
print(l)#1, 2, 3, 4, 5, 5, 7, 8, 5, 4, 3, 9, 6]
#insert
l.insert(9,6)
print(l)#[1, 2, 3, 4, 5, 5, 7, 8, 5, 6, 4, 3, 9, 6]
#remove
l.remove(1)
print(l)#[2, 3, 4, 5, 5, 7, 8, 5, 6, 4, 3, 9, 6]
#pop
l=[1,2,3,4,5,5,7,8,5,4,3,9]
l.pop(11)
print(l)#[1, 2, 3, 4, 5, 5, 7, 8, 5, 4, 3]
#clear
l.clear()
print(l)#[]
#index
l=[1,2,3,4,5,5,7,8,5,4,3,9]
print(l.index(8))#7
#count
l=[1,2,3,4,5,5,7,8,5,4,3,9]
print(l.count(3))#2
#sort
l.sort()
print(l)#[1, 2, 3, 3, 4, 4, 5, 5, 5, 7, 8, 9]
#reverse
l.reverse()
print(l)#[9, 8, 7, 5, 5, 5, 4, 4, 3, 3, 2, 1]
#copy
m=[2,4,5]
l=m.copy()
print(l)#[2,4,5]
#sorted
l=[1,2,3,4,5,5,7,8,5,4,3,9]
print(sorted(l))#[1, 2, 3, 3, 4, 4, 5, 5, 5, 7, 8, 9]
l=[1,2,3,4,5,5,7,8,5,4,3,9]
l.sort(reverse=True)
print(l)#[9, 8, 7, 5, 5, 5, 4, 4, 3, 3, 2, 1]
#maxium
l=[1,2,3,4,5]
print(max(l))#5
#minimum
l=[1,2,3,4,5]
print(min(l))#1
#sum
l=[1,2,3,4,5]
print(sum(l))#15
#len
l=[1,2,3,4,5]
print(len(l))#5
#any
l=[1,2,3,4,5]
print(any(l))#True
#all
l=[1,2,3,4,5]
print(all(l))#True









