import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img=cv2.imread("../Resources/IMG-20210629-WA0053.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Finding face using face cascade
#The second parameter is called scaleFactors, the third parameter is called minNeighbours
faces=faceCascade.detectMultiScale(imgGray,1.1,4)
#To create boundary box around faces we have detected
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,250),2)

cv2.imshow("Image",img)
cv2.waitKey(0)