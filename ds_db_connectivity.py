# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:14:58 2019

@author: Ankita
"""

from sqlalchemy import create_engine
import sqlite3
import pandas as pd
engine=create_engine("sqlite:///Form.db")#create engine
con=engine.connect()#connect engine
print(engine.table_names())

a=pd.read_sql_table("Student",engine)#getting info
print("the table data===",a)
print(type(a))

b=pd.read_sql_table("Student",engine,columns=["Fullname","Email"])
print("the table data111===",b)
q="select * from Student where country ='Nepal'"#finding a particular data

dd=pd.read_sql_query(q,engine)
print("the data selection===",dd)


q1=pd.DataFrame(["HY","ankitaaaa",1,"india","ffas"])
q1.to_sql(name="Studenn",con=engine)
