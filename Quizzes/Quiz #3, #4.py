#!/usr/bin/env python
# coding: utf-8

# # Quiz #3

# Q. 03-01.

# In[3]:


from numpy import sqrt


# In[4]:


class coordinates:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def calc_dist(self):
        return sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)

c2 = coordinates(-3, -5, 4, 1)

print(c2.calc_dist())


# Q.03-02.

# In[6]:


def palindrome(s):
    if len(s) !=1:
        s1 = palindrome(s[1:])+s[0]
        return s1
    else:
        return s
    
s="I have no soda"
if s==palindrome(s):
    print(s,"is palindrome")
    
else:
    print(s, "is not palindrome")


# Q. 03-03

# In[7]:


n_list = [100,200,300]


# In[8]:


mapped_numbers = list(map(lambda x: x * 2, n_list))


# In[9]:


mapped_numbers2 = list(map(lambda x: x * 3, n_list))


# In[10]:


mapped_numbers3 = list(map(lambda x: x * 4, n_list))


# In[11]:


print(mapped_numbers,mapped_numbers2,mapped_numbers3)


# Q. 03-04.

# 1.	Def calc_digit(n): (define el primer valor)
# 2.	       Def final(digit): (define el segundo final)
# 3.	              Return digit**n (se eleva el valor inicial arriba del segundo valor y se muestra)
# 4.	       Return final (se muestra el resultado de la operación arriba)
# 5.	
# 6.	Num_list=[] (se crea una lista vacía)
# 7.	For num in range(1,6): (se inicia pidiendo un rango de números desde el 1 hasta el 6)
# 8.	Num_list.append(calc_digit(num)) (une la lista vacía de num_list con la definición de calc_digit)
# 9.	Print(num_list[num-1] (num)) (imprime el cuadrado de los mismos numeros del rango 1 al 6).
# 

# In[13]:


def calc_digit(n):
    def final(digit):
        return digit**n
    return final

num_list = []
for num in range(1,6):
    num_list.append(calc_digit(num))
    print(num_list[num - 1](num))


# Q. 03-05.

# In[14]:


import numpy as np


# In[15]:


class Data:
    def __init__(self, value):
        self.value = value
        
    def __mul__(self, other):
        return Data(self.value * other.value)
    
    def __truediv__(self,other):
        return Data(self.value / other.value)


a = Data(np.array([30,40]))
b = Data(np.array([10,20]))
c = a * b
d = a/b


# In[16]:


c.value


# In[17]:


d.value


# # Quiz #4

# Q. 04-01

# In[18]:


stack = []
stack.append("Banana")
stack.append("Apple")
stack.append("Tomato")
stack.pop()
stack.append("Strawberry")
stack.append("Grapes")
stack.pop()
print("resultado:",stack)


# Q. 04-02

# In[19]:


stack = []
items = [10 * i for i in range(1,10)]
for item in items:
    stack.append(item)
    if (item // 10) % 2 == 0:
        stack.pop()
print(stack)


# Q. 04-03

# In[20]:


queue = []
items = [10 * i for i in range(1,11)]
for item in items:
    queue.append(item)
    if (item // 10) % 2 == 0:
        queue.pop()
print(queue)


# Q. 04-04

# In[21]:


def find_two(nums):
    x = y = 0
    for i in range(1, len(nums)):
        if nums[x] < nums[i]:
            x = i
        elif nums[y] > nums[i]:
            y = i
    return x, y


# In[22]:


nums = [11, 37, 45, 26, 59, 28, 17, 53]
i, j = find_two(nums)
print(nums[i], nums[j])


# Q.04-05

# 16 comparaciones

# Q. 04-06

# In[23]:


from random import randint

maximum = int(input("Enter the number of maximum; "))
number = int(input("Enter your guessing number: "))
count = 0
low, high = 1, maximum
while low < high:
    mid = (low + high) // 2
    count += 1
    if mid == number:
        print(f"Your number is {number}.")
        break
    elif mid > number:
        high = mid - 1
    else:
        low = mid +1
print(f"Total", count, "times are searched.")


# La salida de count es 6

# Q. 04-07

# El resultado del conteo es 2

# Q. 04-08

# In[30]:


class hash_table:
    def __init__(self):
        self.table = [None] * 127
    
    # Función hash
    def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value): # Metodo para ingresar elementos
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
    def Search(self,value): # Metodo para buscar elementos
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
  
    def Remove(self,value): # Metodo para eleminar elementos
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            print("No hay elementos con ese valor", value)
        else:
            print("Elemento con valor", value, "eliminado")
            self.table[hash] is None;


# In[32]:


H = hash_table()
texto = "Alicia en el país de las maravillas"
H.Insert(texto)
print(H.Search(texto))


# Q. 04-09

# In[33]:


class HashTable:
    
    def __init__(self,size):
        self.size=size
        self.table={}
        for i in range(size):
            self.table[i]=[]
    
    def hash(self,key):
        return key % self.size
    
    def get(self,key):
        return self.table[self.hash(key)]
    
    def put(self,key,value):
        bucket=self.table[self.hash(key)]
        if value not in bucket:
            bucket.append(value)
            
            
table =HashTable(10) #crea la tabla con 10 elementos
books=[
    "the little prince",
    "the old man and the sea",
    "the little mermaid",
    "beauty and the beast",
    "the last leaf",
    "alice in wonderland" ] 
#crea la lista de libros que se guardaran en la tabla, hay menos libros que espacios en la tabla

for book in books:
    key=sum(map(ord,book)) #define la key y el lugar donde se guarda
    table.put(key,book)    #asigna lso pares key,book en la tabla
for key in table.table.keys(): #para todas las posibles key imprime que libro hay
                                #recordemos que hay espacios vacios
    print(key,table.table[key]) #imprime la key y el libro si es que hay

