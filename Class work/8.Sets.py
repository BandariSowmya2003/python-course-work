#1.creating Sets

#set with unique elements
s={1,2,3,4}
print(type(s))#<class 'set'>

#empty set
empty_set=set()
print(type(empty_set))#<class 'set'>

#set with duplicates elements
s={1,2,4,3,5,4,2}
print(s)#{1, 2, 3, 4, 5}

#2.Operations on sets

#1.Membership(|)
s={1,2,4,3,5}
print(4 in s)#True
print(5 not in s)#False

#2.Union(&)
s1={3,4,5}
s2={1,2,6}
print(s1|s2)#{1, 2, 3, 4, 5, 6}

#3.Intersection()
s1={3,4,5}
s2={1,2,6,3}
print(s1&s2)#{3}

#4.Difference
s1={3,4,5,1}
s2={1,2,6}
print(s1-s2)#{3,4,5}

#5.Symmetric Difference
s1={3,4,5}
s2={1,2,6,5}
print(s1^s2)#{1, 2, 3, 4, 6}

#6.Subset
s1={3,4,5}
s2={3,4,5}
print(s1<=s2)#True

#7.Superset
s1={3,4,5}
s2={3,4,5}
print(s1>=s2)#True

#8.Disjoint Sets
s1={3,4,5}
s2={1,2,6}
print(s1.isdisjoint(s2))#True

#3.Built-in Methods for sets

#add
s={1,2,6,5}
s.add(7)
print(s)#{1,2,5,6,7}

#remove
s={1,2,6,5}
s.remove(6)
print(s)#{1,2,5}

#discard
s={1,2,6,5}
s.discard(5)
print(s)#{1,2,6}

#pop
s={1,2,6,5}
s.pop()
print(s)#{2,6,5}

#clear
s={1,2,6,5}
s.clear()
print(s)#set()

#Union(&)
s1={3,4,5}
s2={1,2,6}
print(s1|s2)#{1,2,3,4,5,6}

#Intersection()
s1={3,4,5}
s2={1,2,6,3}
print(s1&s2)#{3}

#Difference
s1={3,4,5,1}
s2={1,2,6}
print(s1-s2)#{3,4,5}

#Symmetric Difference
s1={3,4,5}
s2={1,2,6,5}
print(s1^s2)#{1,2,3,4,6}

#update
s1={1,2,6,5}
s2={2,4,6,7}
s1.update(s2)
print(s1)#{1,2,4,5,6,7}

#Intersection_update
s1={3,4,5}
s2={1,2,6,3}
s1.intersection_update(s2)
print(s1)#{3}

#Difference_update
s1={3,4,5,1}
s2={1,2,6}
s1.difference_update(s2)
print(s1)#{3,4,5}

#Symmetric Difference_update
s1={3,4,5}
s2={1,2,6,5}
s1.symmetric_difference_update(s2)
print(s1)#{1,2,3,4,6}

#copy
s={1,2,3,4}
m=s.copy()
print(m)#{1,2,3,4}

#isdisjoint
s1={1,2,6,5}
s2={3,4}
print(s1.isdisjoint(s2))#True

#issubset
s1={3,4,5}
s2={3,4,5}
print(s1.issubset(s2))#True

#7.issuperset
s1={3,4,5}
s2={3,4,5}
print(s1.issuperset(s2))#True

#4.Built_in functions for sets

#len
s={1,2,6,5}
print(len(s))#4

#max
s={1,2,6,5}
print(max(s))#6

#min
s={1,2,6,5}
print(min(s))#1

#sum
s={1,2,6,5}
print(sum(s))#14

#sorted
s={1,2,4,3,5,4,2}
print(sorted(s))#{1,2,3,4,5}

#5.Immutability and Frozensets
s=frozenset({1,2,3})
print(type(s))#<class 'frozenset'>
