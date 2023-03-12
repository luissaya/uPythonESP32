# Complete project details at https://RandomNerdTutorials.com
from machine import deepsleep
from machine import Pin
from time import sleep

led = Pin (2, Pin.OUT)

#blink LED
led.value(1)
sleep(0.5)
led.value(0)
sleep(0.5)
led.value(1)
sleep(0.5)
led.value(0)
sleep(0.5)
led.value(1)
sleep(0.5)
led.value(0)
sleep(0.5)

# wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
# you should remove this sleep line in your final script
sleep(2)

print('Im awake, but Im going to sleep')

#sleep for 10 seconds (10000 milliseconds)
deepsleep(5000)