FACE DETECTION  AND RECOGNITION SYSTEM

Introduction
•	Face detection and face recognition is a computer vision technology that helps to locate/visualize human faces in digital images. This technique is a specific use case of object detection technology that deals with detecting instances of semantic objects of a certain class (such as humans, buildings or cars) in digital images and videos. With the advent of technology, face detection has gained a lot of importance especially in fields like photography, security, and marketing.
•	Face Detection: it has the objective of finding the faces (location and size) in an image and probably extract them to be used by the face recognition algorithm.
•	Face Recognition: with the facial images already extracted, cropped, resized and usually converted to grayscale, the face recognition algorithm is responsible for finding characteristics which best describe the image.
Pre-requisites
Hands-on knowledge of Numpy and Matplotlib is essential before working on the concepts of OpenCV. 
•	Python
•	Numpy
•	Matplotlib

REQUIRED LIBRARIES:
1.Computer vision(OPENCV)
2. Numpy
3. OS
4. Pickle
5. Shutil
SOFTWARE REQUIRED:  SPYDER(PYTHON)
ALGORITHMS USED: 
1.HAAR CASCADE CLASSIFIER: This is basically a machine learning based approach where a cascade function is trained from a lot of images both positive and negative. Based on the training it is then used to detect the objects in the other images.
So how this works is they are huge individual .xml files with a lot of feature sets and each xml corresponds to a very specific type of use case.
•	2. LOCAL BINARY PATTERNS HISTOGRAMS: LBPH is one of the easiest face recognition algorithms. It can represent local features in the images. It is possible to get great results (mainly in a controlled environment). It is robust against monotonic gray scale transformations. It is provided by the OpenCV library (Open Source Computer Vision Library).


PROJECT DESCRIPTION:

1.Computer Vision — Detecting objects using HaarCascade Classifier
Computer vision is a field of study which encompasses on how computer see and understand digital images and videos.
Computer vision involves seeing or sensing a visual stimulus, make sense of what it has seen and also extract complex information that could be used for other machine learning activities.
Step -1
Import cv2 and numpy and also use the CascadeClassifier function of OpenCV to point to the location where we have stored the XML file, haarcascade_frontalface_default.xml.
Step 2
Now the 2nd step is to load the image and convert it into gray-scale. Generally the images that we see are in the form of RGB channel(Red, Green, Blue). So, when OpenCV reads the RGB image, it usually stores the image in BGR (Blue, Green, Red) channel. For the purposes of image recognition, we need to convert this BGR channel to gray channel. The reason for this is gray channel is easy to process and is computationally less intensive as it contains only 1-channel of black-white.
Step 3
Using the face_classifier which is an object loaded with haarcascade_frontalface_default.xml, we are using an inbuilt function with it called the detectMultiScale.
This function will helps to find the features/locations of the new image. The way it does is, it will use all the features from the face_classifier object to detect the features of the new image.

2. The face recognition systems can operate basically in two modes:
•	Verification or authentication of a facial image: it basically compares the input facial image with the facial image related to the user which is requiring the authentication. 
•	Identification or facial recognition: it basically compares the input facial image with all facial images from a dataset with the aim to find the user that matches that face. 
•	Using the LBP combined with histograms we can represent the face images with a simple data vector.
•	As LBP is a visual descriptor it can also be used for face recognition tasks, as can be seen in the following step-by-step explanation.
3. Training the Algorithm: First, we need to train the algorithm. To do so, we need to use a dataset with the facial images of the people we want to recognize. We need to also set an ID (it may be a number or the name of the person) for each image, so the algorithm will use this information to recognize an input image and give you an output. Images of the same person must have the same ID. With the training set already constructed, let’s see the LBPH computational steps.
ER DAIGRAM  
 
