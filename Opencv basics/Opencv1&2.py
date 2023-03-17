import cv2
import numpy as np
print("First computer vision project")

def imgread():
    #To Read Photo
    img=cv2.imread("../Resources/IMG-20210629-WA0053.jpg")
    cv2.imshow("Output",img)
    cv2.waitKey(0)

def vidcap():
    #To Read Video
    vid=cv2.VideoCapture("Resources/pexels-rodnae-productions-8711391.mp4")
    while True:
        success,imga= vid.read()
        cv2.imshow("Video",imga)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def webvid():
    #To Capture Through Webcam
    webc=cv2.VideoCapture(0)
    webc.set(3,630)
    webc.set(4,470)
    webc.set(10,100)
    while True:
        su,imag=webc.read()
        cv2.imshow("webvideo",imag)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break

#Basic Functions in OpenCV
def Graysc():
    #To convert colored images to gray scale images
    img=cv2.imread("../Resources/IMG-20210629-WA0053.jpg")
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #In OpenCV the color scheme is BGR(Blue,Green,Red) not RGB
    cv2.imshow("Grayimg",imggray)
    cv2.waitKey(0)

def Blurimg():
    #To Blur the image
    img=cv2.imread("../Resources/IMG-20210629-WA0053.jpg")
    imgb=cv2.GaussianBlur(img,(11,11),2) #The second argument in the GaussianBlur function is the kernel size it teks a tuple of two elements and the elements define the size of the kernel(the nos could only be odd nos)
    cv2.imshow("Blurred Image",imgb)
    cv2.waitKey(0)

def Edgedet():
    #To detect edges
    img = cv2.imread("../Resources/Kings.JPG")
    kernel=np.ones((5,5),np.uint8) #Here we are creating a matrix containing 1 as all of its elts and of size (5,5)
    imgcanny=cv2.Canny(img,100,100) #The Cannt Function detect edges it take the image and two threshold values as arguments
    cv2.imshow("Edge image",imgcanny)
    #To Make edges thicker(To Dialate)
    imgdia=cv2.dilate(imgcanny,kernel,iterations=1) #The Second Argument the kernal soz takes a matrix, we need to provide the size and the elements of the matrix. To do this we use numpy
    cv2.imshow("Dilated Image",imgdia)
    #To make edges Thinner
    imgerr=cv2.erode(imgcanny,kernel,iterations=1)
    cv2.imshow("eroded image",imgerr)
    cv2.waitKey(0)

webvid()