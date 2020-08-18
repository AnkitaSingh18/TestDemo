import os         #for handing system files
import numpy as np
from PIL import Image
import cv2 
import pickle
import shutil

a = input("Enter the name of your folder:")
b = "images\\"
path1 = os.path.join(b,"AVAN_%s"%a)
if os.path.exists(path1) and os.path.isdir(path1):
    shutil.rmtree(path1)
    print("Done")
if not os.path.isfile(path1):
    os.makedirs(path1)
    
    print("Done1")
    
cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier("cascades\\haarcascade_frontalface_alt2.xml")
count=0
success =True
while success:
    #capture video frame by frame
    success,image1 = cap.read()
    success,im = cap.read()
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image1, (x,y), (x+w,y+h), (255,0,0), 2)
        #vidcap1.set(cv2.CAP_PROP_POS_MSEC,(count))
        cv2.imwrite("%s\\imgN%d.jpg" %(path1,count),im)      # save frame as JPEG file
        cap.set(cv2.CAP_PROP_POS_MSEC,(count**100)) #used to hold speed of frane generation
        
        
        print ('Read a new frame: ', success)
        count += 1
        cv2.imshow("res",image1)
    if(count>=100):
        break
    elif cv2.waitKey(20) & 0xFF == ord("q"):
        break
    
              
print("the total frames=",count)
cap.release()
cv2.destroyAllWindows()
    


