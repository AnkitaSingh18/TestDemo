# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:31:47 2019

@author: Ankita
"""

import matplotlib.pyplot as plt
import pandas as pd
#dataframe plotting

df1=pd.DataFrame([[1,2,3,4,5],[10,20,30,40,50],[80,100,120,130,140]],columns=["a","b","c","d","e"])
plt.plot(df1,label=["A","B","C","D","E"])
plt.title("Dataframe plot")
plt.xlabel("MY CUSTOM X")
plt.ylabel("MY CUSTOM Y")
plt.show()


x=[1,2,3,4,5,6,7,8,9,10]
y=[10,20,30,40,50,40,30,20,10,20]
plt.scatter(x,y,marker="*",s=40)
plt.plot(x,y)
plt.xlabel("label name for x")
plt.ylabel("label name for y")
plt.title("Scatter plot")
plt.show()

plt.plot([10,20,30],[10,20,10],label="My series",color="red")
plt.plot([1,2,3],[10,20,10],label="my series1",color ="green")
plt.title("scatter with multipl line ")
plt.xlabel("MY CUSTOM X")
plt.ylabel("MY CUSTOM Y")
plt.legend()#used for colors
plt.show()


#bar grapgh
plt.bar([1,3,5,7,9],[5,2,7,8,2],label="first")
plt.bar([2,4,6,8,10],[10,20,30,40,50],label="second",color="g")
plt.xlabel("number")
plt.ylabel("height")
plt.title("bar graph n data")
plt.legend()
plt.show()
#histograpgh

import numpy as np
data=np.random.randint(10,80,size=50)
data1=list(data)
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(data1,bins,histtype="bar",rwidth=0.8)
plt.title("data for own frequency")
plt.show()

base=[1,2,3,4,5]
d1=[7,8,6,11,7]
d2=[2,3,4,3,2]
d3=[7,8,7,2,2]
d4=[8,5,7,8,13]
plt.stackplot(base,d1,d2,d3,d4,colors=["m","c","r","k"])
plt.xlabel("x_data_base")
plt.ylabel("y_data_all attributes")
plt.title("stackplt")

plt.plot([],[],color="m",label="d1",linewidth=5)
plt.plot([],[],color="c",label="d2",linewidth=5)
plt.plot([],[],color="r",label="d3",linewidth=5)
plt.plot([],[],color="k",label="d4",linewidth=5)
plt.legend()
plt.show()


slices=[10,20,30,20,5,8,50,56]

data2=["A","B","C","D","E","F","G","H"]
plt.pie(slices,labels=data2)

plt.title("pie chart")
plt.show()
cols=list("rmkywcbg")
plt.pie(slices,labels=data2,colors=cols,startangle=90,
        shadow=True,explode=(0,0.2,0,0,0,0.40,0,0))













