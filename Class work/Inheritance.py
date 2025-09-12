#Inheritance:

class A():
    def printa(self):
        print("\nThis is the parent class: A")
class B(A):
    def printb(self):
        print("This is the child class: B->A")

class C(B):
    def printc(self):
        print("This is grand child class: C->B->A")
              
c=C()
c.printa()
c.printb()
c.printc()


#Output:

'''
This is the parent class: A
This is the child class: B->A
This is grand child class: C->B->A

'''

#Multiple Inheritance:

class A:
    def printa(self):
        print("\nThis the parent class: A")

class B:
    def printb(self):
        print("This is the parent class: B")

class C:
    def printc(self):
        print("This is the parent class: C")

class D(A,B,C):
    def printd(self):
        print('''This the child class: D
                A B C
                \ | /
                  D   ''')

d=D()
d.printa()
d.printb()
d.printc()
d.printd()

#Output:
'''

This the parent class: A
This is the parent class: B
This is the parent class: C
This the child class: D
                A B C
                \ | /
                  D   
'''

#Hierarchy Inheritance:
class A:
    def printa(self):
        print("\nThis the parent class: A->(A,B,D)")

class B(A):
    def printb(self):
        print("This is the child class: B->A")

class C(A):
    def printc(self):
        print("This is the child class: C->A")

class D(A):
    def printd(self):
        print("This is the child class: D->A")

d=D()
d.printa()
d.printd()

#Output:

'''
This the parent class: A->(A,B,D)
This is the child class: D->A

'''