# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:14:52 2019

@author: Ankita
"""

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk

nltk.download('punkt')
text="Hello how are you. i am fine"
print(word_tokenize(text))
print(sent_tokenize(text))

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak==")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said=()".format(text))
    except:
            print("sorry")