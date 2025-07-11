#1.Operations on strings
#1.1 Concatenation
str1="Sowmya"
str2="Bandari"
result=(str1+ " " + str2)
print(result)#Sowmya Bandari
#1.2 Repetition
print("Python! "*5)#Python! Python! Python! Python! Python! 
#1.3 Indexing
Text="Program"
print(Text[0])#P
print(Text[-6])#r
#1.4 Slicing
print(Text[0:3])#Pro
print(Text[:4])#Prog
print(Text[3:])#gram
#1.5 Membership
print("Pro" in Text)#True
print("Java" not in Text)#True

#2.Built in functions
#2.1 len()
text = "Python program"
print(len(text))#14
#2.2  max() and min()
print(max("AbcXYz"))#z
print(min("AbcXYz"))#A
#2.3 sorted()
print(sorted("database"))#['a', 'a', 'a', 'b', 'd', 'e', 's', 't']
#2.4 chr() and ord()
print(ord("D"))#68
print(chr(87))#W

#Methods
#1. Case Conversion Methods
a="Government"
print(a.lower())#government
print(a.upper())#GOVERNMENT
print(a.capitalize())#Government
print(a.title())#Government
print(a.swapcase())#gOVERNMENT
print(a.casefold())#government

#2. Alignment & Formatting Methods
b="Anantha Lakshmi"
print(b.center(20,"*"))#**Anantha Lakshmi***
print(b.ljust(20,"-"))#Anantha Lakshmi-----
print(b.rjust(30,"-"))#---------------Anantha Lakshmi
print("25".zfill(6))#000025

#3. Search & Find Methods
x="Python Programming Language"
print(x.find('P'))#0
print(x.rfind('o'))#9
print(x.index('r'))#8
print(x.rindex('g'))#25
print(x.count('a'))#3

#4. String Testing Methods
a="Bharathi"
print(a.startswith("B"))#True
print(a.endswith("hi"))#True
print(a.isalpha())#True
print(a.isalnum())#True
print(a.islower())#False
print(a.isupper())#False
print(a.isspace())#False
print(a.istitle())#True
print(a.isidentifier())#True
print(a.isdecimal())#False
print(a.isdigit())#False
print(a.isnumeric())#False

#5. Replace & Modify Methods
s="mango"
print(s.replace("ma", "bi"))#bingo
print(s.translate(str.maketrans("m", "b")))#bango
print(s.maketrans("man", "%#5"))#{109: 37, 97: 35, 110: 53}

#6. Splitting & Joining Methods
a = "Codegnan"
print(a.split(","))#['Codegnan']
print(a.rsplit(",", 1))#['Codegnan']
a = '''Codegnan
Destination'''
print(a.splitlines())#['Codegnan', 'Destination']
a = "codegnan-institute"
print(" ".join("a"))#a
print(a.partition("-"))#('codegnan', '-', 'institute')
print(a.rpartition("-"))#('codegnan', '-', 'institute')

#7. Whitespace & Trimming Methods
x = "Hello"
print(x.strip())#Hello
x = "----hello"
print(x.lstrip("-"))#hello
x = "hello-----"
print(x.rstrip("-"))#hello

#8. Encoding & Decoding Methods
x = "Hello"
print(x.encode("utf-8"))#b'Hello'
x = b"hello"
print(x.decode("utf-8"))#hello