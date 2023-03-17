import cv2
import numpy as np
from collections import deque

def empty(a):
    print("")

cv2.namedWindow("Colors")
cv2.createTrackbar("Hue_min","Colors",64,180,empty)
cv2.createTrackbar("Sat_min","Colors",171,255,empty)
cv2.createTrackbar("Val_min","Colors",78,255,empty)
cv2.createTrackbar("Hue_max","Colors",153,180,empty)
cv2.createTrackbar("Sat_max","Colors",255,255,empty)
cv2.createTrackbar("Val_max","Colors",255,255,empty)

b_pt = [deque(maxlen=1024)]
g_pt = [deque(maxlen=1024)]
r_pt = [deque(maxlen=1024)]
y_pt = [deque(maxlen=1024)]

bindex = 0
gindex = 0
rindex = 0
yindex = 0

kernel = np.ones([5,5],np.uint8)
colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
colorindex = 0

#For canvas setup
paintwindow = np.zeros([471,636,3]) + 255
paintwindow = cv2.rectangle(paintwindow,(40,1),(140,65),(0,0,0),2)
paintwindow = cv2.rectangle(paintwindow,(160,1),(255,65),colors[0],-1)
paintwindow = cv2.rectangle(paintwindow,(275,1),(370,65),colors[1],-1)
paintwindow = cv2.rectangle(paintwindow,(390,1),(485,65),colors[2],-1)
paintwindow = cv2.rectangle(paintwindow,(505,1),(600,65),colors[3],-1)

cv2.putText(paintwindow,"CLEAR",(49,33),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0,),2,cv2.LINE_AA)
cv2.putText(paintwindow,"BLUE",(185,33),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintwindow,"GREEN",(300,33),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintwindow,"RED",(420,33),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintwindow,"YELLOW",(520,33),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.namedWindow("Paint", cv2.WINDOW_AUTOSIZE)


#Loading the webcam
wvid = cv2.VideoCapture(0)

while True:
    sucess, frame = wvid.read()
    #Flipping the frame
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    u_hue = cv2.getTrackbarPos("Hue_max","Colors")
    u_sat = cv2.getTrackbarPos("Sat_max","Colors")
    u_val = cv2.getTrackbarPos("Val_max","Colors")
    l_hue = cv2.getTrackbarPos("Hue_min","Colors")
    l_sat = cv2.getTrackbarPos("Sat_min","Colors")
    l_val = cv2.getTrackbarPos("Val_min","Colors")
    Upperhsv = np.array([u_hue,u_sat,u_val])
    Lowerhsv = np.array([l_hue,l_sat,l_val])

    #Adding boxes to live frames
    frame = cv2.rectangle(frame, (40, 1), (140, 65), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (160, 1), (255, 65), colors[0], -1)
    frame = cv2.rectangle(frame, (275, 1), (370, 65), colors[1], -1)
    frame = cv2.rectangle(frame, (390, 1), (485, 65), colors[2], -1)
    frame = cv2.rectangle(frame, (505, 1), (600, 65), colors[3], -1)
    cv2.putText(frame, "CLEAR", (49, 33), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (300, 33), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)

    Mask = cv2.inRange(hsv,Lowerhsv,Upperhsv)
    Mask = cv2.erode(Mask,kernel,iterations=1)
    Mask = cv2.morphologyEx(Mask,cv2.MORPH_OPEN,kernel)
    Mask = cv2.dilate(Mask,kernel,iterations=1)

    #find contours for point after detecting it
    cnts,_ = cv2.findContours(Mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if len(cnts)>0:
        #Sorting the contours and finding the biggest one
        cnt = sorted(cnts,key=cv2.contourArea,reverse=True)[0]
        #Getting radius of the found contour for the enclosed circle
        ((x,y),radius) = cv2.minEnclosingCircle(cnt)
        #Drawing the circle with given quads and raius
        cv2.circle(frame,(int(x),int(y)),int(radius),(0,0,255),2)
        #Detecting the center of the drwn contour
        M=cv2.moments(cnt)
        center = (int(M['m10']/M['m00']),int(M['m01']/M['m00']))

        #Now checking where the user clicks
        if center[1]<= 65:
            if 40<=center[0]<=140:
                b_pt = [deque(maxlen=512)]
                g_pt = [deque(maxlen=512)]
                r_pt = [deque(maxlen=512)]
                y_pt = [deque(maxlen=512)]

                bindex = 0
                gindex = 0
                rindex = 0
                yindex = 0
                paintwindow[67:,:,:] = 255
            elif 160<=center[0]<=255:
                colorindex = 0 #Blue
            elif 275<=center[0]<=370:
                colorindex = 1 #Green
            elif 390<=center[0]<=485:
                colorindex = 2 #Red
            elif 505<=center[0]<=600:
                colorindex = 3 #Yellow

        else:
            if colorindex == 0:
                b_pt[bindex].appendleft(center)
            elif colorindex == 1:
                g_pt[gindex].appendleft(center)
            elif colorindex == 2:
                r_pt[rindex].appendleft(center)
            elif colorindex == 3:
                y_pt[yindex].appendleft(center)
    else:
        b_pt.append(deque(maxlen=512))
        bindex+=1
        g_pt.append(deque(maxlen=512))
        gindex += 1
        r_pt.append(deque(maxlen=512))
        rindex += 1
        y_pt.append(deque(maxlen=512))
        yindex += 1

    points = [b_pt,g_pt,r_pt,y_pt]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(len(points[i][j])):
                if points[i][j][k-1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame,points[i][j][k-1],points[i][j][k],colors[i],2)
                cv2.line(paintwindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

    cv2.imshow("Tracking",frame)
    cv2.imshow("Paint",paintwindow)
    cv2.imshow("Mask",Mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

wvid.release()
cv2.destroyAllWindows()



        


