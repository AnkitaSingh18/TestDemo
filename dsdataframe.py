# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 12:13:20 2019

@author: Ankita
"""
import numpy as np
import pandas as pd
d={'one':pd.Series([1,2,3],index=['a','b','c']), 'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(d)
print("df==",df)
print("d==",d)
df['three']=pd.Series([10,20,30],index=["a","b","c"])#adding a column
print(df)
df["four"]=df["one"]+df["three"]
print(df)
x=df.pop("one")
print(x)#pops one coloumn
print(df)#poped colum is not shown
x1=df.drop(["two"],1)#drop it tempararily
print(x1)
print(df)
del df["two"]#delete column permanently
print(df)

#z=int1.append(int2)
#panel
data1={"item1":pd.DataFrame(np.random.randn(4,4)),"item2":pd.DataFrame(np.random.randn(4,2))}
print(data1)
p=pd.Panel(data1)
print(p)
aa=p["item2"]
print(aa)

"""
s={"Age":pd.Series([25,26,28,19,18,16,30,27,24,22],index=["a","b","c","d","e","f","g","h","i","j"]),"Name":pd.Series(["ankita","akash","riya","shivam","pawan","aditya","surbhi","gulab","anshika","bhavishya"],index=["a","b","c","d","e","f","g","h","i","j"]),"Rating":pd.Series([4.23,3.22,5.22,4.22,6.11,8.22,7.11,8.33,9.11,2.22],index=["a","b","c","d","e","f","g","h","i","j"])}
df1=pd.DataFrame(s)
print(df1)
n=df1.describe()
print(n)
a5=df1.T
print(a5)
a6=df1.axes#gives axes details
print(a6)
a7=df1.head()
print(a7)
a8=df1.tail()
print(a8)











"""










