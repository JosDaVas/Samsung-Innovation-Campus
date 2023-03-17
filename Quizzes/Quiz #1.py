#!/usr/bin/env python
# coding: utf-8

# # Q.01-01

# In[1]:


print(1+2+3+4+5)


# # Q.02-01

# In[3]:


numero=int(input("Ingrese el numero de suma de impares: "))

suma=0
contador=1

while(contador<=2*numero-1):
    
    suma=suma+contador
    contador=contador+2

print("el valor de la suma de impares de 0 a", numero, "es", suma)


# # Q.02-02

# In[5]:


numero = int(input("Ingrese el numero a comprobar: "))

if numero %2==0:
    print ("el numero", numero, "es par")
else:
    print ("El numero", numero, "es impar")


# # Q.03-01

# In[1]:


print("*" * 10)
print("#" * 10)


# # Q.04-01

# In[4]:


nombre = input('Nombre: ')
apellido = input('Apellido: ')
Provincia = input('Provincia donde reside: ')
Distrito = input('Su dirección: ')

print("Su nombre es", nombre, apellido, "proviene de", Provincia, Distrito)


# # Q.05-01

# In[10]:


booleanos = [False, True]

print('x\ty\tx or y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y, sep = '\t')


# # Q.06-01

# In[3]:


x = int(input('Ingrese un numero: ')) 
y = int(input("Ingrese otro numero: "))
if x>y:
  print(y, x)
elif x<y:
  print(x, y)
else:
  print(x, y)


# # Q.07-01

# In[1]:


edad = int(input('Ingrese su edad: '))

if edad < 18:
    print('Usted es menor de edad.')

else:
    estado_civil = (int(input('Escriba 1 si esta casado y 0 si es soltero: ')))
    while (estado_civil != 1) and (estado_civil != 0):
        print('Elija opción 1 u opción 0')
        estado_civil = (int(input('escriba 1 si esta casado y 0 si es soltero')))
        print()
if (estado_civil == 1):
    print('Usted es un adulto y esta casado')
else:
    print('Usted es un adulto y esta soltero')


# # Q.08.01

# In[10]:


for num in range(2, 13):
    count = 0
    for n in range(12):
        n += 1
        if num%n == 0:
            count += 1
    if (count >= 3):
        print(f"{num} es un numero compuesto")
    else:
        print(f"{num} es un numero primo")


# # Q.09-01

# In[1]:


lower = 100
upper = 999

for num in range(lower, upper + 1):

   # orden de los numeros
   order = len(str(num))
    
   # Suma
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

