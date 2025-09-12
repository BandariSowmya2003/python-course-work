# Recursions
#1.
def bullets(n):
    if n==0:
        return 
    print(n)
    bullets(n-1)

bullets(10)
#Output:
'''
10
9
8
7
6
5
4
3
2
1

'''
#2.

def bullets(n):
    if n==0:
        return 
    bullets(n-1)
    print(n)
bullets(10)

#Output:
'''
1
2
3
4
5
6
7
8
9
10

'''
#3.

def bullets(n):
    if n==0:
        return 
    print("Before:",n)
    bullets(n-1)
    print("After:",n)
bullets(10)

#Output:
'''
Before: 10
Before: 9
Before: 8
Before: 7
Before: 6
Before: 5
Before: 4
Before: 3
Before: 2
Before: 1
After: 1
After: 2
After: 3
After: 4
After: 5
After: 6
After: 7
After: 8
After: 9
After: 10

'''