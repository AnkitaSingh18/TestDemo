# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:49:14 2019

@author: Ankita
"""

import pandas as pd
import numpy as np
print("THE RANDOM DATA==")

df1=pd.DataFrame([[1,2,3,4,5],[10,20,30,40,50],[25,8,40,8,7]],columns=["A","B","C","D","E"])
df1.plot()
df2=pd.DataFrame([1,2,3,4,5,4,3,2,1])
df2.plot()
#bar grapghs
df1.plot.bar()#vertical bar graph
df1.plot.barh(stacked=False)
df1.plot.barh(stacked=True)
#histograpgh
df1.plot.hist(bins=20)
df1.plot.box()
df1.plot.area()#area plot
df1.plot.pie(subplots=True)
