# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:52:10 2019

@author: Ankita
"""

from gtts import gTTS#module to convert text to speech
import os#to play conversion audio
mytext="its Ankita welcome !!"
language='en'#laguage in which we ant to convert
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")