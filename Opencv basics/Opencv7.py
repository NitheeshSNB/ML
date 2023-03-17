#Detecting colors in opencv
import cv2
import numpy as np
def imgread():
    def empty(a):
        pass
    path= "../Resources/lambo.png"
    #To create Trackbars to capture color in real time
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,240)
    #To create TrackBar
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty) #The third and fourth parameters are the start and stop value for the hue. In Opencv there are inly 180(0-179) values for hue not 360
    cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 241, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", 155, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
    while True: #For the track bar to be read the image need to be put in a loop or we should use a webcam
        img=cv2.imread(path)
        #To Convert image into a HSV space
        imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        #To get Track Bar action
        h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
        #To create a mask to define the object we want to find the color for
        lower= np.array([h_min,s_min,v_min])
        upper= np.array([h_max,s_max,v_max])
        msk=cv2.inRange(imgHSV,lower,upper)
        #To get the result we use bitwise and function in open csv. This function adds two images together and create a new one. If there are matching pixels in both the images then it returns 1(true)
        imgresult=cv2.bitwise_and(img,img,mask=msk)

        #cv2.imshow("Image",img)
        cv2.imshow("HSV Image",imgHSV)
        cv2.imshow("Mask",msk)
        cv2.imshow("Result",imgresult)
        cv2.waitKey(1)

imgread()