from machine import Pin, ADC
from time import sleep

# assign ADC at GPIO34 
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
# pot.width(ADC.WIDTH_12BIT)   #Default 12bits

while True:
  #RETURN THE RAW ADC VALUE ACCORDING TO THE RESOLUTION
  pot_value = pot.read()
  print(pot_value)
  sleep(0.2)