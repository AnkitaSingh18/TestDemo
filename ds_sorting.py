# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 12:14:32 2019

@author: Ankita
"""

import pandas as pd
import numpy as np
#in unsorted_df, the labels and their values are unsorted
unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=["col1","col2"])
print("the unsorted data==\n",unsorted_df)
#by label
sorted_df=unsorted_df.sort_index()
print("the sorted",sorted_df)
#by ordering
sorted_df_ord=unsorted_df.sort_index(ascending=False)
print("sorting index with ordered frame==\n",sorted_df_ord)
#sort the columns by passing axis with value 0 and 1
sorted_df_column=unsorted_df.sort_index(axis=0)
print("the sorting by the column==\n",sorted_df_column)

#by values
sorted_df_values=unsorted_df.sort_values(by='col1')
print("the sorting done by values==\n",sorted_df_values)
#sorting algorithm
sorted_df_algorithm==unsorted_df.sort_values(by='col1',kind='mergesort')
print(sorted_df_algo)