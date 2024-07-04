from gpiozero import LED
from time import sleep

red = LED(11)

for _ in range (25):
	red.on()
	sleep(2)
	red.off()
	print("blink")
