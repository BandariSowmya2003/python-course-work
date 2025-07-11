#1.Creating Lists
#1.1 Empty list
list = []
print(list)

#1.2 List with Elements
l=[1,3,2,4,5,6]
print(type(l))
l=['apple','banana','mango','cherry']
print(type(l))
l=[5,'Codegnan',2.67,True,3+6j]
print(type(l))

#1.3 Nested Lists
nested_list=[[1,4,2,5,6,], ['p','q','r'],[True,False]]
print(type(nested_list))

#2.Accessing Elements
#2.1 Indexing(positive & negative)
l=['java','database','python']
print(l[0])
print(l[-1])
print(l[1])

#2.2 Slicing
l=[1,2,3,4,5,5,7,8,5,4,3,9]
print(l[1:5])
print(l[:4])
print(l[5:])
print(l[-2:-5])
print(l[::-1])

#3. Modify List
#3.1 Changing elements
l=[20,40,60,80]
l[2]=50
print(l)

#3.2 Adding elements
l=[1,2,3,4,5,5,7,8,5,4,3,9]
#append
l.append(10)
print(l)
#insert
l.insert(1,7)
print(l)
#extend
l.extend([2])
print(l)

#3.3 Removing Elements
l=[1,2,3,4,5,5,7,8,5,4,3,9]
#remove
l.remove(5)
print(l)
#pop
l.pop(2)
print(l)
l.pop()
print(l)
#delete
del l[3]
print(l)
#clear
l.clear()
print(l)

#4.List Methods
#append
l=[1,2,3,4,5,5,7,8,5,4,3,9]
l.append(7)
print(l)
#extend
l=[1,2,3,4,5,5,7,8,5,4,3,9]
l.extend([6])
print(l)
#insert
l.insert(9,6)
print(l)
#remove
l.remove(1)
print(l)
#pop
l=[1,2,3,4,5,5,7,8,5,4,3,9]
l.pop(11)
print(l)
#clear
l.clear()
print(l)
#index
l=[1,2,3,4,5,5,7,8,5,4,3,9]
print(l.index(8))
#count
l=[1,2,3,4,5,5,7,8,5,4,3,9]
print(l.count(3))
#sort
l.sort()
print(l)
#reverse
l.reverse()
print(l)
#copy
m=[2,4,5]
l=m.copy()
print(l)
#sorted
l=[1,2,3,4,5,5,7,8,5,4,3,9]
print(sorted(l))
l=[1,2,3,4,5,5,7,8,5,4,3,9]
l.sort(reverse=True)
print(l)
#maxium
l=[1,2,3,4,5]
print(max(l))
#minimum
l=[1,2,3,4,5]
print(min(l))
#sum
l=[1,2,3,4,5]
print(sum(l))
#len
l=[1,2,3,4,5]
print(len(l))
#any
l=[1,2,3,4,5]
print(any(l))
#all
l=[1,2,3,4,5]
print(all(l))









