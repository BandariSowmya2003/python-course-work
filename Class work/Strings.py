#1.Operations on strings
#1.1 Concatenation
str1="Sowmya"
str2="Bandari"
result=(str1+ " " + str2)
print(result)
#1.2 Repetition
print("Python! "*5)
#1.3 Indexing
Text="Program"
print(Text[0])
print(Text[-6])
#1.4 Slicing
print(Text[0:3])
print(Text[:4])
print(Text[3:])
#1.5 Membership
print("Pro" in Text)
print("Java" not in Text)

#2.Built in functions
#2.1 len()
text = "Python program"
print(len(text))
#2.2  max() and min()
print(max("AbcXYz"))
print(min("AbcXYz"))
#2.3 sorted()
print(sorted("database"))
#2.4 chr() and ord()
print(ord("D"))
print(chr(87))

#Methods
#1. Case Conversion Methods
a="Government"
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.swapcase())
print(a.casefold())

#2. Alignment & Formatting Methods
b="Anantha Lakshmi"
print(b.center(20,"*"))
print(b.ljust(20,"-"))
print(b.rjust(30,"-"))
print("25".zfill(6))

#3. Search & Find Methods
x="Python Programming Language"
print(x.find('P'))
print(x.rfind('o'))
print(x.index('r'))
print(x.rindex('g'))
print(x.count('a'))

#4. String Testing Methods
a="Bharathi"
print(a.startswith("B"))
print(a.endswith("hi"))
print(a.isalpha())
print(a.isalnum())
print(a.islower())
print(a.isupper())
print(a.isspace())
print(a.istitle())
print(a.isidentifier())
print(a.isdecimal())
print(a.isdigit())
print(a.isnumeric())

#5. Replace & Modify Methods
s="mango"
print(s.replace("ma", "bi"))
print(s.translate(str.maketrans("m", "b")))
print(s.maketrans("man", "%#5"))

#6. Splitting & Joining Methods
a = "Codegnan"
print(a.split(","))
print(a.rsplit(",", 1))
a = '''Codegnan
Destination'''
print(a.splitlines())
a = "codegnan-institute"
print(" ".join("a"))
print(a.partition("-"))
print(a.rpartition("-"))

#7. Whitespace & Trimming Methods
x = "Hello"
print(x.strip())
x = "----hello"
print(x.lstrip("-"))
x = "hello-----"
print(x.rstrip("-"))

#8. Encoding & Decoding Methods
x = "Hello"
print(x.encode("utf-8"))
x = b"hello"
print(x.decode("utf-8"))