import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
import threading
import sys
import os

import fcntl
import subprocess

GPIO.setmode(GPIO.BOARD)
Output_pin = 12
GPIO.setup(Output_pin,GPIO.OUT,initial=GPIO.HIGH)
'''
cap = cv2.VideoCapture(0)

print('camera open? {}'.format(cap.isOpened()))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
'''
cv2.namedWindow('image_win',flags = cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/test/haarcascade_frontalface_default.xml')

count = 5

class ipcamCapture:
    def __init__(self,URL):
        self.Frame = []
        self.status = False
        self.isstop = False
        
        self.cap = cv2.VideoCapture(URL)
    
    def start(self):
        print("ipcam started!")
        threading.Thread(target=self.queryframe, daemon=True, args=()).start()

    def stop(self):
        self.isstop = True
        print("ipcam stopped!")
        
    def getframe(self):
        return self.Frame
    
    def camera(self,gray):  
        faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.25,
        minNeighbors = 3,
        )
        return faces
    
    def queryframe(self):
        while (not self.isstop):
            self.status, self.Frame = self.cap.read()
            
            if not self.status:
                print("read fail")
                if __name__ == "__main__":
                    cv2.destroyAllWindows()
                    GPIO.cleanup()
                    ipcam.stop()
                    print("restart")
                    time.sleep(3)
                    restart()
                    
        self.cap.release()
#--------------------------------------------------------------
def restart():
    python = sys.executable
    os.execl(python,python,*sys.argv)
#--------------------------------------------------------------
URL = "0"
ipcam = ipcamCapture(0)

ipcam.start()

time.sleep(5)

while(True):
    '''
    ret,I = cap.read()
    
    if not ret:
        print("read fail")
    '''
    
    I = ipcam.getframe()
    
    cv2.imshow('./image_win',I)
    
    gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
    
    '''
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.25,
        minNeighbors = 3,
        )
    '''
    
    faces = ipcam.camera(gray)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(I,(x,y),(x+w, y+h),(0,255,0),2)
        
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = I[y:y+h,x:x+w]
        
        print("see")
        GPIO.output(Output_pin,GPIO.LOW)
        count = 5
     
    if count <= 0:
        GPIO.output(Output_pin,GPIO.HIGH)
    else:
        count -= 1
    
    cv2.imshow('./image_win',I)
    print(count)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        GPIO.cleanup()
        ipcam.stop()
        break