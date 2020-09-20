# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 12:21:33 2019
colums add id 3 digits for first 100 rows then 4 digitesn so on
flying pokemon in fire file
@author: Ankita
"""

import numpy as np
import pandas as pd
a=pd.read_csv("C:\\Users\\Ankita\\Downloads\\pokemon.csv")
a=pd.DataFrame(a)
print("print the data==\n",a)
b=a.shape
print(b)
c=a.ndim
print(c)
d=a.keys()
print(d)
d1=a.head()
d2=a.tail()
print("d1==",d1)

#operation on datsets
x1=a.describe()
print("Describing the data====",x1)
x2=a.sort_values(["Name"],ascending=True)
print("sorted names==",x2)
x3=a.drop(columns=["Type 1"])
print("droping===",x3)
x4=a.iloc[0]
print("iloc function used for sort acc to index==",x4)
x5=a.iloc[5,6]
print("iloc second func====",x5)
x6=a.loc[a["Type 1"]=="Fire"]
print("sorting along labels===",x6)
z=x6.to_csv("C:\\Users\\Ankita\\Downloads\\Fire.csv")

#handling the null or missing values
y1=a["Type 1"].isnull()
print("Printing the missing values==",y1)
y2=a.notnull()
print("detecting missing values",y2)
y3=a.dropna()
print("dropping the missing values",y3)
y3.to_csv("C:\\Users\\Ankita\\Downloads\\ankss_cleandata.csv")
z1=a.fillna(0)#fills the specific values
print("fill the output==\n(z1)",z1)
z2=a.fillna(method="pad")#fills method forward
print("the pad funct==",z2)
z3=a.fillna(method="backfill")
print(z3)


t1=pd.read_csv("C:\\Users\\Ankita\\Downloads\\pokemon.csv",skiprows=3)
print("the value of t1==",t1)
t2=pd.read_csv("C:\\Users\\Ankita\\Downloads\\pokemon.csv",header=None)
print("the values of t2==",t2)#treat the label as data
t3=pd.read_csv("C:\\Users\\Ankita\\Downloads\\pokemon.csv",header=None,names=["a","b","c","d","e","f","g","h","i","j","k","l","m","n"])
print("provide the names t3==",t3)
t4=pd.read_csv("C:\\Users\\Ankita\\Downloads\\pokemon.csv",nrows=12)
print("provide the rows",t4)
t5=pd.read_csv("C:\\Users\\Ankita\\Downloads\\pokemon.csv",na_values=["not available","N.A"])
print("filling na in place of missing valuest5==",t5)



