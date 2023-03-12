from machine import Pin
import time

led=Pin(2,Pin.OUT)
led.off()
count=0
# print some text to the serial console
print('Hello MicroPython!')


def blink(n,ms):
    for x in range(n):
        led.on()
        time.sleep_ms(ms)
        led.off()
        time.sleep_ms(ms)

while(1):
    count+=1
    print(count)
    blink(1,2000)
    help('modules')

