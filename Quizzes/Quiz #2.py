#!/usr/bin/env python
# coding: utf-8

# # Q.2-01

# In[5]:


l1 = ['I like', 'I love']
l2 = ['pancake.', 'kiwi juice.', 'espresso.']
palabras = []


# In[6]:


for i in l1:
    for e in l2:
        union = "{} {}".format(i,e)
        palabras.append(union)
        
for i in range(1,7):
     print(palabras[i-1])


# # Q.2-02

# In[1]:


person = {'Name' : 'David Doe', 'Age' : 26, 'weight' : 82, 'Job' : 'Data Scientist'}


# In[2]:


person["Father"]="John Doe"


# In[3]:


print(person)


# # Q2-03

# In[77]:


list = [5, 6, 3, 9, 2, 12, 8, 7]


# In[78]:


list.pop(5)


# In[79]:


print(list)


# In[80]:


list.append(12)


# In[81]:


print(list)


# # Q.2-04

# In[44]:


my_list=[[1,2],[3,4],[5,6]]
list=[]


# In[45]:


for x in range(0, 3):
    list.extend(my_list[x])
list


# # Q.2-05

# In[47]:


maria = {'korean' : 94, 'english' : 91, 'mathematics' : 89, 'science' : 83}


# In[48]:


notas_sum = sum(maria.values())
notas_amount = len(maria.values())

print(notas_sum/notas_amount)


# # Q.2-06

# In[55]:


import copy


# In[56]:


school = {'kim' : {'age' : 16, 'hei' : 170, 'grade' : 3}
          ,'lee' : {'age' : 15, 'hei' : 168, 'grade' : 2},
          'choi' : {'age' : 14, 'hei' : 173, 'grade' : 1}}


# In[57]:


school2 = copy.deepcopy(school)
print(school2)


# # Q.2-07

# In[58]:


paises = ("China", "India", "Estados Unidos", "Indonesia")
poblaciones = (1391, 1364, 327, 264)


# In[63]:


union = zip(paises, poblaciones)

for element in union:
    print(element)

