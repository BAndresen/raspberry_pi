import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

try:
    while True:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        sleep(.5)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
        sleep(.5)
except KeyboardInterrupt:
    GPIO.cleanup()
