import cv2
import numpy as np

path= "../Resources/shapes.png"
img=cv2.imread(path)
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    contours,heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #The Retr external retrives the extreme or most outer contour
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), thickness=3)  # -1 to draw all the contours
            perim = cv2.arcLength(cnt,True) #True to denote the boundary is closed
            #print(perim)
            #To approximate how many corner points we have
            approx= cv2.approxPolyDP(cnt,0.02*perim,True)
            #print(len(approx))
            objcor = len(approx)
            #To draw a bounding box we get the width and height,x and y
            x,y,w,h = cv2.boundingRect(approx)
            print(cv2.boundingRect(approx))
            if objcor == 3: objectType = "Tri"
            elif objcor == 4:
                aspratio = w/float(h)
                if aspratio>0.95 and aspratio<1.05: objectType="Square"
                else:objectType="Rectaangle"
            elif objcor>4: objectType="Circle"
            else:objectType = "None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),2)
            #Bounding boxes are useful to find the width, length,height of the object
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,0.7,(0,0,0),2)




imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
imgBlank=np.zeros_like(img)
imgContour=img.copy()
getContours(imgCanny)

imgFinal = stackImages(0.7,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlank]))

cv2.imshow("Stack",imgFinal)

cv2.waitKey(0)