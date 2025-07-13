#Dictonary

#1. Dictonary
Student={"name":"Sowmya","Course":"MCA","Roll no":3,"Batch no":2025}
print(Student) #{'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025}
print(type(Student)) #<class 'dict'>

#2. Dictonary Operations

#2.1 Accessing Values
Student={"name":"Sowmya","Course":"MCA","Roll no":3,"Batch no":2025}
print(Student["name"]) #Sowmya
print(Student.get("Roll no")) #3
print(Student.get("city","Not Available")) #Not Available

#2.2 Adding and Updating Items
Student={"name":"Sowmya","Course":"MCA","Roll no":3,"Batch no":2025}
Student["age"]=22
Student["city"]="Anantapur"
print(Student) #{'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}

#2.3 Removing items From a Dictionary

#Using Pop()
Student={"name":"Sowmya","Course":"MCA","age":22,"Batch no":2025}
age=Student.pop("age")
print(age) #22
print(Student) #{'name': 'Sowmya', 'Course': 'MCA', 'Batch no': 2025}

#Using del()
Student={"name":"Sowmya","Course":"MCA","age":22,"Batch no":2025}
del Student["Course"]
print(Student) #{'name': 'Sowmya', 'age': 22, 'Batch no': 2025}

#Using popitem()
Student={"name":"Sowmya","Course":"MCA","age":22,"Batch no":2025}
Student.popitem()
print(Student) #{'name': 'Sowmya', 'Course': 'MCA', 'age': 22}

#Using clear()
Student={"name":"Sowmya","Course":"MCA","Roll no":3,"Batch no":2025}
Student.clear()
print(Student) #{}

#3. Dictonary Built-in Methods

#3.1 Dictionary Methods for Accessing Data
#dict.get(key,default)
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}
print(Student.get("name","Not Found")) #Sowmya

#dict.keys()
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}
print(Student.keys()) #dict_keys(['name', 'Course', 'Roll no', 'Batch no', 'age', 'city'])

#dict.values()
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}
print(Student.values()) #dict_values(['Sowmya', 'MCA', 3, 2025, 22, 'Anantapur'])

#dict.items()
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}
print(Student.items()) #dict_items([('name', 'Sowmya'), ('Course', 'MCA'), ('Roll no', 3), ('Batch no', 2025), ('age', 22), ('city', 'Anantapur')])

#3.2 Dictonary Methods for Adding and Updating Data
#dict.update(new_dict)
Student={"name":"Sowmya","Course":"MCA","Roll no":3,"Batch no":2025}
Student.update({"city":"America"})
print(Student) #{'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'city': 'America'}

#dict.setdefault(key,default)
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'city': 'America'}
print(Student.setdefault("city","Unknown")) #America

#3.3 Dictionary Methodscfor Removing Data
#dict.pop(key,default)
Student={"name":"Sowmya","Course":"MCA","age":22,"Batch no":2025}
age=Student.pop("age")
print(age) #22
print(Student) #{'name': 'Sowmya', 'Course': 'MCA', 'Batch no': 2025}

#del dict[key]
Student={"name":"Sowmya","Course":"MCA","age":22,"Batch no":2025}
del Student["Course"]
print(Student) #{'name': 'Sowmya', 'age': 22, 'Batch no': 2025}

#dict.popitem()
Student={"name":"Sowmya","Course":"MCA","age":22,"Batch no":2025}
Student.popitem()
print(Student) #{'name': 'Sowmya', 'Course': 'MCA', 'age': 22}

#dict.clear()
Student={"name":"Sowmya","Course":"MCA","Roll no":3,"Batch no":2025}
Student.clear()
print(Student) #{}

#4. Built-in Functions for Dictionaries
#4.1 len(dict)
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}
print(len(Student)) #6

#4.2 max(dict)
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}
print(max(Student)) #name

#4.3 Min(dict)
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}
print(min(Student)) #Batch no

#4.4 Sorted(dict)
Student={'name': 'Sowmya', 'Course': 'MCA', 'Roll no': 3, 'Batch no': 2025, 'age': 22, 'city': 'Anantapur'}
print(sorted(Student)) #['Batch no', 'Course', 'Roll no', 'age', 'city', 'name']


#5. Nested Dictionaries
Students={"Sowmya":{"age":22,"course":"MCA"},"Kusuma":{"age":23,"course":"MBA"}}
print(Students["Kusuma"]["course"]) #MCA
print(Students["Sowmya"]["age"]) #22


#6. Dictionary Comprehension
Squares={x:x*x for x in range(1,6)}
print(Squares) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}