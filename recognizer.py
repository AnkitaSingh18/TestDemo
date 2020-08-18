import cv2
import numpy as np
import pickle


face_cascade = cv2.CascadeClassifier("cascades\\haarcascade_frontalface_alt2.xml") #used for detecting frontal face
recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.read("trainner.yml")

lables ={"person_name" : 1}
with open("labels.pickle","rb") as f:
    og_lables = pickle.load(f)
    lables ={v:k for k, v in og_lables.items()}

cap = cv2.VideoCapture(0)

while(True):
    
    #capture video frame by frame
    ret,frame=cap.read()
    
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #convert frames into gray for qbetter result and display in color
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.5, minNeighbors = 2) #this is for multiple face in frame
    
    for (x,y,w,h) in faces:
        #print(x,y,w,h)   #for reading all cordinate of faces
        roi_gray = gray[y:y+h,x:x+w]     #for capture selected area of face  (y:cor start,y:cor end)
        roi_color = frame[y:y+h,x:x+w]    #converting into color frame 
        #Prediction and recognizer
        id_,conf = recognizer.predict(roi_gray)
        if conf>=50 and conf <=95:
            #print(id_)
            print(lables[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = lables[id_]
            color = (255,255,255)
            stroke = 2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
        else:
            #imageTopass=dector(frame,face_cascade)
            font=cv2.FONT_HERSHEY_SIMPLEX
            name="UNKNOWN"
            print(name)
            color=(255,255,255)
            stroke=2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)       
        
        
        
        #draw rectangle to high light face pass(frame,width and height,color of line,thickness)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
        
    
    
    #showing captured frames
    cv2.imshow("cap_frame",frame)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    
    
    
#When everything done release this program
cap.release()
cv2.destroyAllWindows()
    
