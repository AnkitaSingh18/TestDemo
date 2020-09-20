# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 12:53:49 2019

@author: Ankita
"""
import pandas as pd
import numpy as np


aa=pd.DataFrame(np.random.randint(0,10,(6,4)))
print(aa)
#bb=pd.DataFrame(np.random.randint(0,10,(10,4)))
#print(bb)
"""ds=aa.reindex_like(bb)#resizing or reshaping
print(ds)
ds1=bb.reindex_like(aa)
print(ds1)"""
#ds2=aa.reindex_like(bb,method="ffill",limit=2)
#print(ds2)
aw=aa.rename(columns={0:"A",1:"B",2:"C",3:"D"})
print(aw)
aw1=aw.rename(columns={"A":"AGE","B":"ADD","C":"XYZ","D":"WYZ"})
print(aw1)
#sorting

df=pd.DataFrame(np.random.randn(10,2),index=[0,1,4,3,5,2,8,9,6,7],columns=["col1","col2"])
print(df)
print(df.sort_index)
print(df.sort_index(axis=1))
print(df.sort_values(by="col1"))
print(df.sort_values(by="col1",kind="merge"))



