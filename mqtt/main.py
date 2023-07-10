# main.py -- put your code here!
from time import sleep_ms
from machine import Pin, PWM
from mqtt import WIFI


# p2 = Pin(2,Pin.OUT)
# count = 0
print('Hello MicroPython!')
wifiesp = WIFI()
wifiesp.modeSTA("Sayaverde","sayaverdeporobravo")
print(wifiesp.macADDRESS)
print(wifiesp.ipADDRESS)
pwm2 = PWM(Pin(2), freq=1, duty=127)  # create and configure in one go
while(1):
  # count+=1
  # p2.on()
  # sleep_ms(500)
  # p2.off()
  # sleep_ms(500)
  # print(count)

  print(pwm2)                               # view PWM settings
  sleep_ms(4000)
  # pwm2.deinit() #stop PWM
  print("change frec")
  pwm2.freq(10) #change frecuency
  print(pwm2)    
  sleep_ms(1000)
  print("return frec")
  pwm2.freq(1)
  sleep_ms(4000)
  # pwm2.deinit()
  # sleep_ms(3000)