import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

try:
    while True:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        sleep(.5)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        sleep(.5)
except KeyboardInterrupt:
    GPIO.cleanup()
