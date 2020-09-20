# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:41:59 2019

@author: Ankita
"""

import pandas as pd
import numpy as np

d={"one":[1,1],"two":[2,2]}
c={"a","b"}
df=pd.DataFrame(data=d,index=c)
print(df)
print(df.index)
print(df.keys)
print(df.stack())
print(df.unstack())
print(df.T)


x=pd.DataFrame({"one":[1,1,1,1],"two":[2,2,2,2],"alpha":["a","b","c","a"]})
df1=pd.DataFrame(x)
print(df1)
x1=df1.groupby("alpha")
print(x1)
x2=x1.get_group("a")
print(x2)
x3=x1.get_group("b")
print(x3)
x11=df1.groupby(["alpha","one"])
print(x1)
x5=x11.groups
print(x5)
x6=df1.groupby(["alpha","one"]).sum()
print(x6)