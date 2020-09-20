# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 12:50:58 2019

@author: Ankita
"""

import pandas as pd
import numpy as np
N=12
ipl_data={'Team':['riders','riders','devils','devils','kings','kings','kings','kings','riders','royals','royals','riders'],
          'Rank':[1,2,2,3,3,4,1,1,2,4,1,2],
          'Year':np.random.choice(["2014","2016","2015"],N).tolist(),
          'points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df=pd.DataFrame(ipl_data)
print("the dataframe==\n",df)

op1=df.groupby('Team')
print("the output for groupby function==\n",op1)

aa=op1.get_group('riders')
print(aa)
op2=df.groupby('Team').groups   #view groups
print("the groping of objects==\n",op2)
op3=df.groupby(['Team','Year']).groups  #group by with multiple columns
print("the multiple grouping==\n",op3)


#iterating with groupby object
grouped=df.groupby('Year')
for name,group in grouped:
    print("the name as per the team==\n",name)
    print("the group as per the year==\n",group)
    
op4=grouped.get_group("2014")  #to get group
print("the get group function==\n",op4)

op5=grouped['points'].agg(np.mean)
print("the aggregation==\n",op5)


op6=grouped['points'].agg([np.sum,np.mean,np.std])
print("few functions of aggregation==\n",op6)



N=20
val1={"city":np.random.choice(["delhi","mumbai","noida","kerela","goa"]),
     "age":np.random.randint(15,35,(N)).tolist(),
     "contact":np.random.randint(99999,1000000,(N)).tolist()}

#print("Val====",val)
val2=pd.DataFrame(val)
print("the dataframe===\n",val2)

#concatenation
concate=pd.cancat([df,val1],ignore_index=True)
print("concatenation of both data==\n",concate)
kyss=pd.concat([df,val1],keys=["ipl_data","city_data"])
print("keys==",kyss)