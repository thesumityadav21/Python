
        
# Write a Program to find the sum of all the divisors of a given number

# take num = given number and sum = 0
# Inside loop check the number is completely divisble by divisor or not
# if (num%i == 0)
# print sum = sum + i
'''
num = 12
sum = 0
for i in range ( 1, num + 1):
    if (num%i==0):
        sum = sum + i
        print(sum)
print(sum)  '''

# Write a Program to find all the divisors except the number it self
# num = num + 1 to num then it not print the number i.e. 12.
'''num = 12
for i in range ( 1, num):
    if (num%i==0):
        print(i) '''

# Write sum of all the divisor exluding the number 
# also finds perfect number
num = 2
sum = 0
for i in range ( 1, num ):
    if (num%i==0):
        sum = sum + i
        print(sum)
        
# Write a program to count the number of divisors of a given number
# Write a Program to count the number of divisors b/n 1 and that number itself
