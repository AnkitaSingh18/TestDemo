# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 13:46:18 2019

@author: Ankita
"""

import pandas as pd
import numpy as np

data=pd.Series(["WilliaM Rick","alber@t","john",np.nan,1234,"steveSMith"])
print(data.str.strip("m"))
print(data.str.split())
print(data.str.split("i"))
print(data.str.count("i"))
print(data.str.swapcase())
print(data.str.replace("i","o"))
print(data.str.upper())
print(data.str.find("a"))
print(data)
#datamanipulation