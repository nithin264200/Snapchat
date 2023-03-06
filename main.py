from cv2 import cv2
import cvzone
capture=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay=cv2.imread('beard.png',cv2.IMREAD_UNCHANGED)
while True:
    camera,frame=capture.read()
    gray_color=cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
    faces=cascade.detectMultiScale(gray_color)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w ,y+h),(0,255,0),2)
        overlay_resize=cv2.resize(overlay, (w,h))
        frame=cvzone.overlayPNG(frame,overlay_resize,[x,y])
    cv2.imshow('snap',gray_color)
    if cv2.waitKey(10)==ord('v'):
        break