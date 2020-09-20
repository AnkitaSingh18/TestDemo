# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:39:43 2019

@author: Ankita
"""
#date range()
import pandas as pd
dt_range=pd.date_range("01-01-2019","01-13-2019")
op1=pd.date_range("1/2/2011",periods=35)
print("the date range==",op1)

#change the date frequency
op2=pd.date_range("1/1/2011",periods=15,freq='Y')
print("the frequency date==",op2)

#we change the date acc to time
indx=pd.DatetimeIndex(dt_range)
print("index==",indx)

start=pd.datetime(2011,1,1)
end=pd.datetime(2011,1,15)
op3=pd.date_range(start,end)
print("the end to start==",op3)

op4=pd.to_datetime("2018-01-15 3:45pm")
print("datetime==",op4)

from datetime import datetime
op5=pd.to_datetime(["2018-01-05","7/8/1952","Oct 10 1995"])#passing multiple format together
print("op5==",op5)
op6=datetime.now()
print("op6==",op6)
#----------------
op7=pd.DataFrame()
op7["Date"]=pd.date_range("1/1/2011",periods=72,freq="H")
op7["year"]=op7["Date"].dt.year
op7["month"]=op7["Date"].dt.month
op7["day"]=op7["Date"].dt.day
op7["hour"]=op7["Date"].dt.hour
op7["minute"]=op7["Date"].dt.minute

#----------time data analysis------
t=pd.tslib.Timestamp.now()
print("Current time==",t)
print("year==",t)
print("month==",t)
print("day==",t)
print("hour==",t)
print("minute==",t)
print("sec==",t)
t1=pd.Timedelta("2 days 2 hours 15 minutes 30 second")
print("the time delta==",t1)

t2=pd.Timedelta(6,unit='h')
print("the time with int value",t2)
t3=pd.Timedelta(days=2)
print("the date based==",t3)

s=pd.Series(pd.date_range("2012-1-1",periods=3,freq="D"))
td=pd.Series([pd.Timedelta(days=i) for i in range(3)])
df1=pd.DataFrame(dict(A=s,B=td))
print("the operations==\n",df1)
df1["C"]=df1["A"]+df1["B"]
print(df1)

#-------------------------------------
url='http://bit.ly/uforeports'
url_data=pd.read_csv(url)
print("url_data==",url_data)
timedata=url_data.Time
print("timedata==",timedata)
url_data["Time"]=pd.to_datetime(url_data.Time)
weekday=url_data.Time.dt.weekday_name
print("weekday==",weekday)
yr_data=url_data.Time.dt.dayofyear
print("yr_day_no==",yr_data)























