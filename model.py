import os                       #for handing system files
import numpy as np
from PIL import Image
import cv2
import pickle
#print(help(cv2.face))
face_cascade = cv2.CascadeClassifier("cascades\\haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer = cv2.face.createLBPHFaceRecognizer()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))    #make path of the file
image_dir = os.path.join(BASE_DIR,"images")              #enter in the src folder

current_id = 0   #for identifing new labels
label_ids={} #for holding values of labels
y_labels = []  #empty list which containing name
x_train = []  #empty lst which containing pixel value

for root,dirs,files in os.walk(image_dir):         #check of all files in dir
    for file in files:                             #fetch for all jpg and png files
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root,file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","_")
            print(path,label)
            
            if not label in label_ids:      #labels for checking images
                label_ids[label] = current_id
                current_id += 1 
            id_ = label_ids[label]
            print(label_ids)
            
            #y_labels.append(label)   #any number
            #x_train.append(path)    #verify  the image and convert in numpy array
            
            pil_image = Image.open(path).convert("L")  #grayscale
            size=(550,550 )   #resize
            final_image = pil_image.resize(size,Image.ANTIALIAS)
            image_array = np.array(final_image,"uint8") #convert images into array
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array,scaleFactor = 1.5, minNeighbors = 5)

            for (x,y,w,h) in faces:
                
                #print(x,y,w,h)   #for reading all cordinate of faces
                roi = image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
                
                
print("The Y labels",y_labels)
print("The X train",x_train) 

with open("labels.pickle","wb") as f:
    pickle.dump(label_ids,f)


recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")

print("DONE")
              
                
