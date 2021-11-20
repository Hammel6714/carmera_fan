import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print('camera open? {}'.format(cap.isOpened()))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

cv2.namedWindow('image_win',flags = cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

while(True):
    
    ret,I = cap.read()
    
    if not ret:
        print("read fail")
      
    cv2.imshow('./image_win',I)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
        cap.release()
        cv2.destroyAllWindows()
        GPIO.cleanup()