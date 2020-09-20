# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:36:44 2019
numpy operations
@author: Ankita
"""

import numpy as np
a1=np.random.randint(0,10,(8,8))
print(a1)
"""print(a1[1:,2])"""#print 1st row and 2nd column

#print(a1[:,[2,3])

#x=np.array([1,2,5],[3,7,5])
#print(x)
"""print(a1[6:,4:])
a=np.array([4,5])
b=np.array([3,4])
c=np.array(a1([a,b]))
print(c)"""
a=(a1[[2,2],[3,3]])
print(a)
b=(a1[[3,4],[3,4]])
print(b)
#c=(a1[a,b])
#print(c)
a=np.array(["hello","hii"],dtype='<U8')
b=np.array([1,2],dtype='<U8')
c=np.char.add(a,b)
print(c)
d=np.char.multiply(a,5)#repeatation
print(d)
e=np.char.center(a,20,fillchar="*")
print(e)
s=np.char.capitalize(a)
print(s)
s1=np.char.upper(a)
print(s1)
s2=np.char.swapcase(a)
print(s2)
a2=np.char.split(a,"l")
print(a2)
a3=np.char.replace(b,"l","a")
print(a3)
a4=np.array(0,64,(8,8))
print(a4)