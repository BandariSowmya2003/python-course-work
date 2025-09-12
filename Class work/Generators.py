#Generators
#1.
def display(l):
    for i in l:
        yield i

l=['reels100','reels200','reels300','reels400','reels500']
scroll=display(l)

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

#Output:

'''
reels100
reels200
reels300
reels400
reels500

'''

#2.
def students(names):
    for i in names:
        yield i

names=['Sowmya','Jyothsna','Madhavi','Kusuma','Kavitha','Yashwanthi','Akshaya','Swathi','Akhila','Bharani']
display=students(names)

print(next(display))
print(next(display))
print(next(display))
print(next(display))
print(next(display))
print(next(display))
print(next(display))
print(next(display))
print(next(display))
print(next(display))

#Output:

'''
Sowmya
Jyothsna
Madhavi
Kusuma
Kavitha
Yashwanthi
Akshaya
Swathi
Akhila
Bharani

'''
