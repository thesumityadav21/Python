"""
initialization - Starting  value
while (condition): ending value
statement
increase/decrease

i = 1
while (i <= 10):
    print(i)
    i = i + 1
"""

'''
Conditional Statement 

if (Condition):
    Statement

if (condition):
    statement 1
else:
    statement 2

if (condition):
    statement 1
elif(condition 2):
    statement 2
elif(condition 3):
    statement 3
else:
    statement ( Not Mandatory)
'''

# Write a Program to print natural numbers from 1 to 10 but if I reach 5 program should terminate
"""
for i in range(1, 10):
    if i == 5:  # break terminates the loop
        break
    print(i)

for i in range(1, 10):
    if i == 5:  # skips the line 
        continue
    print(i)
"""
# User Input
'''
a = input('write your name')
print(a)

a = int(input('Write a Value'))
print(a*5)
'''

# Methods/functions
'''
def add():
    a = 5
    b = 6
    c = a + b
    print(c)


add()


def add(x, y):  # x,y are here is parameter
    z = x + y
    print(z)


add(2, 4)  # x,y are here is arguments
'''


def square(x):
    return x * x


'''square(4)
'''

'''n = int(input("enter a value of n"))
res = square(n)
print(res)'''

'''print(square(4))
'''

'''print(square(x=4))'''

'''res = 2 * square(4)
print(res)
'''

''' yield in place of return with object for returning multiple values'''


def student(fname: object, lname: object) -> object:
    print(fname + " " + lname)


student("raj", "chopra")

student(fname="hi", lname="how are you")

student(lname="chopra", fname="raj")  # No d/f in output after position change

# default approach

'''def add(x, y=10):
    return x + y


print(add(8))
'''

'''def add(x=8, y=10):
    return x * y


print(add())
print(add(4, 2))  # we can override values
'''

# When we don't the arguments then we use - *args

'''def add(*argv):
    sum = 0
    for i in argv:
        sum = sum + i
    return sum


res = add(10, 20, 30, 40, 50)
print(res)'''

'''def f(*x):
    for i in x:
        print(i)


res = f(10, 20, 30, 40, 50)
print(res)
'''
# none because of by default return

'''def f(*x):
    for i in x:
        print(i)
    return 0

res = f(10, 20, 30, 40, 50)
print(res)'''

# method **kwargs from Dictionary


# lambda expression - aynomunuous func
# n no. of arguments
# 1 = expressions
'''x = lambda x,y: x+y+z
print(x(4,5))'''

'''z = lambda a,b,x,d: a*b+x-d
print(z(1,2,34,5))'''


'''def double(x):
    y = lambda a: a * x
    return y


res = double(2)
print(res(5))'''
