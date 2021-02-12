import cv2
import time

face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt2.xml")
cap = cv2.VideoCapture(0)

i=0
ready = True
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for(x,y,w,h) in faces:

        color = (255,0,0)
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color, stroke)
    cv2.imshow("frame",frame)
    if(len(faces) > 0 and ready):
        cv2.imwrite('NoMask/pic{:>05}.jpg'.format(i),frame)
        ready = False
        start = time.time()
        time.sleep(3.0 - time.time() + start)
        ready = True
        i+=1
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()