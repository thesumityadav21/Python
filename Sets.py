#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Sets
# S = {  }

s = {1,2,3,4,1}
print(s)


# In[7]:


lst = [[1,2,3], [1,2,3], [4,5,6]]

'''s = set(lst)
print(s)'''

print(lst)

t = ((1,2,3), (1,2,3), (4,5,6))
print(t)

# Will throw a error - unhashable type: 'set
s = {{1,2,3},{2,3,4}}

pritn(s)


# In[14]:


t =(1,2,3,4,5,6,1,2,3,4)
print(sum(t)) #31
print(sum(s))



# In[13]:


t ={1,2,3,4,5,6,1,2,3,4}
print(sum(s))


# In[22]:


s ={"Coding","thinker", 1, "Java", "python", 2, "python" }
print(len(s))


# In[33]:


# Union, Intersection and Difference

# Union
s1 = {1,2,3,4,5,6}
s2 = {4,5,7,8,9,2,1}

print(s1|s2)

# Interction 
print(s1&s2)

#difference
print(s1-s2)
print(s2-s1)

#add method - Set Updation - Sets are mutable but tuples are not
s2.add(15)
print(s2)

#print in sorted manner and will convert into list
print(sorted(s1-s2))

# In Set
print(set(sorted(s1-s2)))


# In[ ]:





# In[ ]:





# In[ ]:




