# Generators

"""def fun():
    yield statement"""

'''def series(): # Creation of function
    for i in range(1, n + 1):
        yield i


n = int(input('input'))  # Creation a function
for i in series():
    print(i)
'''

# Series of output through Generator function

'''def square():
    for i in range(1, n + 1):
        yield i * i


n = int(input('input'))
for i in square():
    print(i)'''

# Types of Variables

'''
1. Local
2. Global
3. Non-local'''

'''a = 10
def fun1 ():
    b = 20
    print("inside fun1 : ", b) 
    print("inside fun1 : " ,a) 

# print("outside fun1 : ", b) # here b is not accessable

fun1()
print("outside fun1 : ", a)
print("outside fun1 : ", b)'''

'''a = 10
def fun1 ():
    global a # By using Global, we access global variable
    a =  a + 10
    print("inside fun1 : ", a)

fun1()
print("outside fun1 : ", a)'''

'''
a = 10
def fun1 ():
    global a
    a =  a + 10
    b = 30
    print("inside fun1 : ", a)
    print("inside fun1 : ", b)


print("outside fun1 : ", a)
fun1() '''


# Non-local - Used when there is nested functions.

# --------- Functions Completes ---------


# OOPs
# 1. encapsulation
# 2. inheritance
# 3. polymorphism

# Class - blueprint, Logical entity, no memory space, n no. of object can be created

# Objects - Real world entity, Occupy Memory Space

# __init__() :- Default Constructor, To construct an Object

# self :- Parameter 

# . :- dot Operator










