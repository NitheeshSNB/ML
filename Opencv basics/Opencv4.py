#Program to insert texts and shapes into an image
import cv2
import numpy as np


def imgread():
    #To Read Photo
    #Creating a Matrix with all its elements as zero. Here zero refers black
    img=np.zeros((512,512,3),np.uint8) #The image created by the matrix is a gray scale image as it contains only 512x512 boxes
    print(img.shape)
    #To color the image
    img[150:300,250:500]= 150,60,55 #Here we are selecting the whole image and setting its BGR value to our desired value. To color only a part of the image we need to define the range
    cv2.imshow("Image",img) #This creates a image with full black screen with 512x512 size given by the matrix
    cv2.waitKey(0)

def toinsertshape():
    img=np.zeros((512,512,3),np.uint8)
    #To insert line in image
    cv2.line(img,(0,0),(250,250),(50,65,70),thickness=2)
    #To insert Rectangle
    cv2.rectangle(img,(250,300),(350,500),(0,0,250),cv2.FILLED) #Here the FILLED dunction fills the image with the given color
    #To insert Circle
    cv2.circle(img,(400,350),35,(255,255,255),3)
    #To insert text
    cv2.putText(img,"HELLOEVERYONE",(0,200),cv2.FONT_HERSHEY_TRIPLEX,1,(235,30,56),2)
    cv2.imshow("line",img)
    cv2.waitKey(0)

toinsertshape()
