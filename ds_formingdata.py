# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:45:40 2019

@author: Ankita
"""

import numpy as np
import pandas as pd
N=20
df=pd.DataFrame({
        
        "x":np.linspace(0,stop=N-1,num=N),
        "y":np.random.rand(N),
        "c":np.random.choice(["low","high","medium"],N).tolist(),
        "d":np.random.normal(100,10,size=(N)).tolist()
        })
print(df)
#renaming and reindexing
"""print(df.keys())
print(df.columns)
a1=df.reindex(index=[0,2,5],columns=["c","d","x"])#slicing
print(a1)"""
#print("describe===",df.describe())
for n in df:  #iterating a dataframe gives columns names
    print("the values of the column==",n)
for keys,values in df.iteritems():
    print("the values of the keys and columns==",keys,values)
for row_index,row in df.iterrows():
        print("the values of rows and index==",row_index,row)
for row in df.itertuples():#doestnot manipulate the data
    print("the values of row==",row)