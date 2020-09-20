# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:13:10 2019

@author: Ankita
"""

from textblob import TextBlob#library for sentiments such as good or bad
a="Your work is excellent"
b="Your work is totally bad"

test1=TextBlob(a)
test2=TextBlob(b)

print("the sentiment==",test1.sentiment)
print("the sentiment==",test2.sentiment)
#polarity shows negative and positive review