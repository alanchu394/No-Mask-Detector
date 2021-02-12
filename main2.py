import numpy as np
import cv2
import sys


face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt2.xml")
image = cv2.imread("test2.jpg")




gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor = 1.2,    
    minNeighbors = 1)
for(x,y,w,h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    color = (255,0,0)
    stroke = 2
    end_cord_x = x+w
    end_cord_y = y+h
    cv2.rectangle(image,(x,y),(end_cord_x,end_cord_y),color, stroke)
cv2.imshow("frame",image)
cv2.waitKey(0)

