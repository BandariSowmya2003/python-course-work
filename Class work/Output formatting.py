#Output Formatting

#printing text
print('hello world')

#printing multiple items
name='ganavi'
age=4
print('name: ', name,'age: ', age)

#using sep to change the seperator
print('2025','16','07', sep='-')

#using end to control line endings
print('hello,', end='')
print('world!')

#printing special characters
#new line(\n)
print('line 1\nline 2')

#tab(\t)
print('name:\tAlice')

#1.Using commas
name='Ganavi'
age=4
score=99
print('name:', name,'age:', age, 'score:', score)

#using modulo operator
name='babu'
age=25
score=95.5
print('name:%s | age:%d | score:%.2f' % (name, age, score))

#using f-trings
name='charlie'
age=28
score=87.898
print(f'name: {name} | age:{age} | score:{score:.2f}')

#using str.format()
name='Ganavi'
age=4
score=99.8
print('name:{} | age:{} | score:{:.1f}'.format(name, age, score))
