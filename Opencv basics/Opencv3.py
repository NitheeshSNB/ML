import cv2
import numpy as np
print("First computer vision project")
#Note: In OpenCV the x axis is towards the right and the y axis is towards bottom(not towards conventional top)
def imgread():
    #To Read Photo
    img=cv2.imread("../Resources/IMG-20210629-WA0053.jpg")
    cv2.imshow("Output",img)
    print(img.shape) #To get the size of the image
    #The shape attribute returns a tuple whose first value is the height(y-axis), second one is the width(x-axis), third one is no.of channels which is BGR
    cv2.waitKey(0)
    #To resize an image
    imgresize= cv2.resize(img,(500,620))
    cv2.imshow("Resized image",imgresize)
    cv2.waitKey(0)
    #To crop an image
    imgcrop= img[0:350,450:750] #First range is the height(y-axis), second range is the width(x-axis)
    cv2.imshow("crop image",imgcrop)
    cv2.waitKey(0)

imgread()

