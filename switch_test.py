import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
Output_pin = 12
GPIO.setup(Output_pin,GPIO.OUT,initial=GPIO.HIGH)

while(True):
    print("on")
    GPIO.output(Output_pin,GPIO.LOW)
    time.sleep(3)
    print("off")
    GPIO.output(Output_pin,GPIO.HIGH)
    time.sleep(3)

    
GPIO.cleanup()
