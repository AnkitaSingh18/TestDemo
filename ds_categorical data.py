# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:19:50 2019

@author: Ankita
"""

import numpy as np
import pandas as pd
cat1=pd.Categorical(["a","b","c","a","b","c","d"],["c","a","b"])
print(cat1)
cat1=pd.Categorical(["a","b","c","a","b","c","d","a"],["c","a","b"],ordered=True)
print(cat1)
a=pd.Series(["a","b","c","d","b","a"],dtype="category")
print(a)
s=a.cat.add_categories(["e"])
print(s)
x=a.cat.remove_categories(["a"])
print(x)
