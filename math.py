#MATH IN PYTHON

friends = 5

#freinds = friends +1
#friends += 1

#friends = friends -1
#friends -= 2

#friends *= 3

#friends /= 2
#friends= friends ** 3  # exponential sign is **

#friends **= 3
friends = friends % 2
print(friends)

#result = round (x)
#result = abs(y)
x = 3.14
y =5
#result = pow(4, 3)
#print (result)

import math

x= 9.9

print(math.pi)
print(math.e)

print(math.sqrt(x))
#print(math.ceil(x))

#print(math.floor(x))

radius = float(input('enter the radius of a circle :'))

c = 2 * math.pi * radius

print(c)

Area = math.pi * pow(radius,2)
print(Area)


a= float(input('enter value of a:'))
b =  float(input('enter value of b:'))

ca= math.sqrt(pow(a,2) + pow(b,2))

print(ca)



import numpy as np

a = np.array([10,20,30])
print(a)
print(type(a))
print(a.shape)
print(a.ndim)
print(a.size)

b = np.array([10,"Abc",3.9])
print (b)
print(type(b))
print(b.dtype)
np.zeros(5)
np.ones(5)
