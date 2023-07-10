from machine import Pin, ADC
from time import sleep

# assign ADC at GPIO34 
uvOut = ADC(Pin(34))
uvRef = ADC(Pin(35))
### SET ATTENUATION
uvOut.atten(ADC.ATTN_11DB)   #Full range: 3.3v
uvRef.atten(ADC.ATTN_11DB)
### SET RESOLUTION
uvOut.width(ADC.WIDTH_12BIT) #Can be 9-10-11-12
uvRef.width(ADC.WIDTH_12BIT)

def convert_mWm2(x):
  in_min = 0.99
  in_max = 2.8
  out_min = 0.0
  out_max = 15.0
  if x <  in_min:
    return out_min
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def average(pin,quantity):
  pinAverage = 0
  for i in range(quantity):
      pinAverage += pin.read()
  return pinAverage/quantity

while True:
  uvAverage = average(uvOut,20) 
  uvVoltage = 3.3/(uvRef.read())*(uvAverage)
  #RETURN THE RAW ADC VALUE ACCORDING TO THE RESOLUTION
  uv_intensity = convert_mWm2(uvVoltage)
  print('uv voltage Out Average adc: ',uvAverage)
  print('ref voltage adc: ',uvRef.read())
  print('uv voltage: ',uvVoltage)
  print('uv intensity: ',uv_intensity,'mW/cm2')
  sleep(1)
