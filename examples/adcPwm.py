from machine import Pin, ADC, PWM
from time import sleep

# assign ADC at GPIO34 
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB) #Full range: 3.3v
pot.width(ADC.WIDTH_10BIT)#resolution 10bits      
pwmLed = PWM(Pin(2), freq=20000, duty=0) 

while True:
  pwmLed.duty(pot.read())