from machine import Pin, ADC
from time import sleep

# assign ADC at GPIO34 
pot = ADC(Pin(34))
### SET ATTENUATION
# ADC.ATTN_0DB: No attenuation (100mV - 950mV)
# ADC.ATTN_2_5DB: 2.5dB attenuation (100mV - 1250mV)
# ADC.ATTN_6DB: 6dB attenuation (150mV - 1750mV)
# ADC.ATTN_11DB: 11dB attenuation (150mV - 2450mV)
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

### SET RESOLUTION
# ADC.WIDTH_9BIT = 9
# ADC.WIDTH_10BIT = 10
# ADC.WIDTH_11BIT = 11
# ADC.WIDTH_12BIT = 12
# pot.width(ADC.WIDTH_12BIT)
# by default is set to 12 (0-4095)


while True:
  #RETURN THE RAW ADC VALUE ACCORDING TO THE RESOLUTION
  pot_value = pot.read()
  print(pot_value)
  sleep(0.2)
  
# # Will return a float
# def convert(x, in_min, in_max, out_min, out_max):
#     return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# # Will return a integer
# def convert(x, in_min, in_max, out_min, out_max):
#     return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


# # Will return an integer between out_min and out_max
# def convert(x, i_m, i_M, o_m, o_M):
#     return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)


# # Test
# for i in range(200):
#     print(i, convert(i, 40, 80, 0, 1023))