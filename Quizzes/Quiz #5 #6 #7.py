#!/usr/bin/env python
# coding: utf-8

# # Quiz #5

# Q.05-01

# In[8]:


def bubblesort(S):
    n = len(S)
    print(n)
    for i in range(n):
        for j in range(n-1):
            if S[j] > S[j + 1]:
                print(f"posición j {j} posición j + 1 {j + 1}")
                S[j], S[j + 1] = S[j + 1], S[j]


# In[10]:


S = [50, 30, 40, 10, 20]
bubblesort(S)
print(S)


# Se ejecutaron 8 comparaciones

# Q. 05-02

# In[11]:


def insertionsort2(S):
    n = len(S)
    for i in range(1, n):
        print(S)
        x = S[i]
        j = i - 1
        while j >= 0 and S[j] > x:
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = x


# In[12]:


S = [50, 30, 40, 10, 20]
insertionsort2(S)
print(S)


# Se ejecutaron 7 comparaciones

# Q. 05-03

# In[17]:


S = [6, 2, 11, 7, 5, 4, 8, 16, 10, 3]
mergesort2 = (S, 0, len(S)-1)
print(mergesort2)


# Q. 05-04

# # Quiz #6

# Q. 06-01

# In[1]:


import math


# In[27]:


num = 5


# In[28]:


def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
print("El factorial de",num,"es", factorial(num))


# Q. 06-02

# In[34]:


def calcular(funcion, limite):
    for n in range(limite):
        n = random.randrange(1, 30)
        fac = funcion(n)


# Q. 06-03

# In[29]:


def sec_fib(n):
    if n > 1:
        return sec_fib(n-1) + sec_fib(n-2)
    return n

for i in range(10):
    print(sec_fib(i))


# Q. 06-04

# In[37]:


print('A merry xmas to all')


# In[39]:


'A = 4', 'M,E,R,R,Y = 4,5,7,6,3', 'X,M,A,S = 5,8,2,6', 'TO = 4,5', 'A,L,L = 4,2,2'


# In[45]:


Palabra1 = (4)
Palabra2 = (4+5+7+6+3)
Palabra3 = (5+8+2+6)
Palabra4 = (4+5)
Palabra5 = (4+2+2)


# In[46]:


Palabra1, Palabra2, Palabra3, Palabra4, Palabra5


# In[47]:


Palabra1**2, Palabra2**2, Palabra3**2, Palabra4**2, Palabra5**2


# # Quiz #7

# Q. 07-01

# In[135]:


import pandas as pd


# In[145]:


Data = {'col1': [1,2], 'col2': [3,4], 'col3': [5,6], 'col4': [7,8]}


# In[146]:


df= pd.DataFrame(Data)


# In[147]:


df


# Q. 07-02

# In[153]:


new_df = df[['col4']]


# In[154]:


new_df


# Q. 07-03

# In[152]:


df


# In[155]:


df.index = ["Primero", "Segundo"]


# In[156]:


df


# Q. 07-04

# In[163]:


df.isnull()


# Q. 07-05

# In[164]:


df.info()

