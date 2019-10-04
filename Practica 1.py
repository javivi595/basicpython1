#!/usr/bin/env python
# coding: utf-8

# In[18]:


a, b = map(int, input('Escribe base y altura del triangulo separado por espacio: \n').strip().split())
print(b*a/2)


# In[13]:


c= int(input('Introduce una temperatura en grados celsius:'))
print("La temperatura en grados fahrenheit es {:.2f}".format(c*(9/5)+32))


# In[14]:


n=int(input("Introduce un numero para saber si es par: "))
if n%2==0:
    print("El numero {} es par".format(n))
else:
    print("El numero {} es inpar".format(n))


# In[15]:


a, b= map(int, input('Escribe dos numeros para comparar cual es mayor: ').strip().split())
print ("El numero mayor es {}".format(max(a,b)))


# In[ ]:




