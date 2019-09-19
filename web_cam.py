#video using webcam and communication between pc and arduino using pyserial lib.
import numpy as np
import cv2
cap=cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS,72)
while(True):
    ret,frame=cap.read()
    cv2.imshow('ashw',frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    
cap.release()
cv2.destroyAllWindows()



import numpy as np
import cv2

image = cv2.imread('circle1.jpg')
cv2.imshow("gg",image)

imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cnt = contours[4]
#img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
c = max(contours, key=cv2.contourArea)
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 8, (0, 0, 255), -1)
cv2.circle(image, extRight, 8, (0, 255, 0), -1)
cv2.circle(image, extTop, 8, (255, 0, 0), -1)
cv2.circle(image, extBot, 8, (255, 255, 0), -1)
cv2.imshow("Image", image)

cv2.waitKey(0)
 
