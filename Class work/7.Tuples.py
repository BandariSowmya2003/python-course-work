#Creating Tuples

#1. Tuple Creation 
t=(1,2,3,4,5,6,7)
print(type(t)) #<class 'tuple'>

#Empty Tuple
t=()
print(t)

#Single element tuple
single_tuple=(2,3,4,5)
print(type(single_tuple))

#Multiple element tuple
t=(1,'mango',3.7)
print(type(t))

#Without Paranthesis (implicit tuple Creation)
t=1,2,3
print(type(t)) #<class 'tuple'>

#2. Accessing Tuple Elements
#2.1 Indexing
t=(11,22,33,44,55)
print(t[2]) #33

#2.2 Negative Indexing
t=(11,22,33,44,55)
print(t[-1]) #55

#2.3 Slicing
t=(11,22,33,44,55)
print(t[1:4]) #(22, 33, 44)

#3. Operation on Tuples
#3.1 Concatenation
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2) #(1, 2, 3, 4, 5, 6)

#3.2 Repetition
t=(1,2,3)
print(t*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)

#3.3 Membership Testing
t=(10,20,30)
print(20 in t) #True
print(40 in t) #False
print(40 not in t) #True

#3.4 Tuple Unpacking
t=(2,4,6,8)
a,b,c,d=t
print(a,b,c,d) #2 4 6 8

#4. Tuple Methods
#4.1 Count
t=(2,4,4,6,8,4,10)
print(t.count(4)) #3

#4.2 Index
t=(2,4,6,8,10)
print(t[3]) #8
print(t[-1]) #10

#5. Built -in Functions for Tuple
#5.1 Len()
t=(11,12,13,14,15,16)
print(len(t)) #6

#5.2 Max()
t=(11,12,13,14,15,16)
print(max(t)) #16

#5.3 Min()
t=(11,12,13,14,15,16)
print(min(t)) #11

#5.4 Sum()
t=(11,12,13,14,15,16)
print(sum(t)) #81

#5.5 iterable
t=([1,2,3,4])
print(t) #[1, 2, 3, 4]

#6. Immutability and Tuple Behavior
nested_tuple=(1,[a,b])
nested_tuple[1][0]=100
print(nested_tuple)#(1, [100, 4])