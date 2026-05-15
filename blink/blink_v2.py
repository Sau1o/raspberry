import RPi.GPIO as GPIO
import time
GPIO.setup(14,GPIO.OUT)
while true:
	GPIO.output(14.True)
	time.sleep(2)
	GPIO.output(14,False)
	Time.sleep(2)
