#Program to change warp perspective
import cv2
import numpy as np


def imgread():
    #To Read Photo
    img=cv2.imread("../Resources/Kings.JPG")
    width,height=250,350
    #To define the points of the card
    pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
    #To define which corner we are reffering
    pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
    #To define the matrix for the perspective
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    #To warp the perspective given by the matrix
    imgwarp=cv2.warpPerspective(img,matrix,(width,height))
    cv2.imshow("Kings",imgwarp)
    cv2.waitKey(0)

def joinimg():
    img=cv2.imread("../Resources/Kings.JPG")
    #To stack img horizontally
    imgh=np.hstack((img,img,img))
    #To stack img vertically
    imgv=np.vstack((imgh,imgh))

    cv2.imshow("image",img)
    cv2.imshow("image horizontal", imgh)
    cv2.imshow("image vertical", imgv)
    cv2.waitKey(0)
#This way of Stacking posses two problems
#If we try to add more images it may go out of frame
#If the images are of different channels then the joining is difficult
