# 15 Jan
#for loop
# for variable_name in range ( start, end, Step):
# -------> Statement
# indentation - 4  general space or 1 tab space 

# range function

# print 1 to 100 numbers

for i in range (1,101):
        print(i)
# d/f
for i in range (101):
        print(i)
        
for i in range (0,101,1):
        print(i)

for i in range (1,101):
        print(i)
        
# print even numbers b/n 10 to 25

for i in range(10,25,2):
    print(i,end = " ")
    
    
# Pattern Programs

for i in range(1,6):
    print("*")
    
for j in range(1,6):
    print("*", end = "")
    
for i in range(1,6):
    for j in range(1,6):
        print("*", end = " ")
    print()
    
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = " ")
    print()
    
for i in range(0,6):
    for j in range(1,(6-i)+1):
        print("*", end = " ")
    print()
    
    
