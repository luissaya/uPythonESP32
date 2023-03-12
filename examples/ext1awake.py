#Only RTC GPIOs can be used as a wake up source. GPIO0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17

import esp32
from machine import Pin, deepsleep
from time import sleep

#set the external wakeup as input
wake1 = Pin(14, mode = Pin.IN)
wake2 = Pin(12, mode = Pin.IN)

#level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
esp32.wake_on_ext1(pins = (wake1,wake2), level = esp32.WAKEUP_ANY_HIGH)


print('Im awake. Going to sleep in 2 seconds')
sleep(2)
print('Going to sleep now')
deepsleep()