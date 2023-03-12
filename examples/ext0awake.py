#The ext0 mode allows you to use one GPIO as a wake up source. The ext1 mode allows you to set more than one GPIO as a wake up source at the same time.

import esp32
from machine import Pin, deepsleep
from time import sleep

#set the external wakeup as input
wake1 = Pin(14, mode = Pin.IN)

#level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)


print('Im awake. Going to sleep in 2 seconds')
sleep(2)
print('Going to sleep now')
deepsleep()