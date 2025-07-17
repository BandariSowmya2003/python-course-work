#Type conversions
#Converting from int
a=3
print(type(a))#<class 'int'>
print(float(a))#3.0
print(complex(a))#(3+0j)
print(bool(a))#True
print(str(a))#3
#print(list(a))#Error
#print(tuple(a))#Error
#print(set(a))#Error
#print(dict(a))#Error

#Converting from float
b=2.7
print(type(b))#<class 'float'>
print(int(b))#2
print(complex(b))#(2.7+0j)
print(bool(b))#True
print(str(b))#2.7
#print(list(b))#Error
#print(tuple(b))#Error
#print(set(b))#Error
#print(dict(b))#Error

#Converting from String
s='Python'
print(type(s))#<class 'str'>
print(bool(s))#True
print(list(s))#['p', 'y', 't', 'h', 'o', 'n']
print(tuple(s))#('p', 'y', 't', 'h', 'o', 'n')
print(set(s))#{'h', 'o', 't', 'p', 'y', 'n'}
#print(dict(s))#Error
#print(int(s))#Error
#print(float(s))#Error

#Converting from list
l=[1,2,3,4]
print(type(l))#<class 'list'>
print(str(l))#[1,2,3,4]
print(bool(l))#True
print(tuple(l))#(1,2,3,4)
print(set(l))#{1,2,3,4}
#print(dict(l))#Error
#print(int(l))#Error
#print(float(l))#Error

#Converting from tuple
t=(1,2,3,4)
print(type(t))#<class 'tuple'>
print(str(t))#(1,2,3,4)
print(bool(t))#True
print(list(t))#[1,2,3,4]
print(set(t))#{1,2,3,4}
#print(dict(t))#Error
#print(int(t))#Error
#print(float(t))#Error

#Converting from set
s={1,2,3,4}
print(type(s))#<class 'set'>
print(bool(s))#True
print(list(s))#[1,2,3,4]
print(tuple(s))#(1,2,3,4)
#print(int(s))#Error
#print(float(s))#Error
#print(dict(s))#Error


#Converting from dictionary
d={1:2,3:4}
print(type(d))#class 'dict'>
print(str(d))#{1:2, 3:4}
print(bool(d))#True
print(list(d))#[1,3]
print(set(d))#{1,3}
print(tuple(d))#(1,3)
#print(int(d))#Error
#print(float(d))#Error

#Converting from boolean
bool=True
print(type(bool))#<class 'bool'>
print(int(bool))#1
print(float(bool))#1.0
print(complex(bool))#(1+0j)
print(str(bool))#True
#print(dict(bool))#Error
#print(list(bool))#Error
#print(set(bool))#Error
#print(tuple(bool))#Error



#Converting dict to dict
d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
print(dict(d))#{'name': 'teja', 'batch': '22', 'subject': 'python'}
