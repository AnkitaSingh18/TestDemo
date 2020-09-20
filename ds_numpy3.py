# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:24:08 2019

@author: Ankita
"""
import pandas as pd
import numpy as np
"""a1=np.random.randint(1,10,[4,4])
print(a1)
print(a1.flat[7])#works as index,treats as linear array
print(a1.flat[8:12])
print(a1.flatten())#converts multidimesion array as linear array,returns copy,takes move memory
print(a1.ravel())"""

#print(a1.ravel(order="A"))#memory allocation
a=np.random.randint(1,10,(4,4))
print("array A=",a)
b=np.random.randint(1,10,(4,4))
print("array B=",b)
c=np.concatenate([a,b],0)#xaxis are rows
print(c)
d=np.concatenate([a,b],1)#yaxis are columns
print("concatenation",d)
e=np.stack((a,b),0)
print("stacking",e)
f=np.stack((a,b),1)
print("stacking using 1",f)
a2=np.hstack([a,b])
print("horizontal stacking",a2)#used for merging the data
a3=np.split(a,2)
print("spliting array =",a3)
a4=np.split(a,2,1)
print("a4=",a4)
print("array A=",a)
a5=np.append(a,[[7,5,6,8]],axis=0)
print("appended array A5=",a5)

b1=np.insert(a,2,[7,8,9,10],axis=0)
print("insertion in row",b1)
b2=np.insert(a,2,[7,8,9,10],axis=1)
print("insertion in column",b2)
c1=np.delete([a],2)
print("c1==",c1)
c2=np.sort(a,axis=0)
print("sorting c2==",c2)

d=np.dtype([("name","S10"),("height","i1"),("age","f4")])
cat=np.array([("Ank",18,41),("singh",19,30),("abc",17,40)],d)
print("cat==",cat)
p=np.sort(["height"])
print(p)
x=np.sort(cat,order=["height"])
print(x)
