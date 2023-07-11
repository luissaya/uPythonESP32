# main.py -- put your code here!
from time import sleep_ms
from machine import Pin, PWM
from mqtt import WIFI, MQTT, PUBLISH
import json

SSID = "Sayaverde"
PASSWORD = "sayaverdeporobravo"
CLIENT_ID = "ESP32_test"
BROKER = "public.mqtthq.com"
PORT = 1883
TOPIC_SUB = "esp32test1"
TOPIC_PUB = "esp32test2"
DATA = {"sepalLength": "6.4","sepalWidth":  "3.2","petalLength": "4.5","petalWidth":  "1.5"}
# p2 = Pin(2,Pin.OUT)
# count = 0
DATAE = {"alarma": '0', "llave": '0', "zona": '0'}
# DATAE = {}
print('Hello MicroPython!')
wifiesp = WIFI()
wifiesp.modeSTA(SSID,PASSWORD)
print(wifiesp.macADDRESS)
print(wifiesp.ipADDRESS)

def CALLBACK(topic, payload):
  print(f"Received from Topic: {topic}, message: {payload}")
  data_dict = json.loads(payload)
  global DATAE
  DATAE = data_dict
  # print(f"data1 : {data_dict["llave"]}")

mqttESP = MQTT(CLIENT_ID,BROKER,PORT,TOPIC_SUB, CALLBACK)

pwm2 = PWM(Pin(2), freq=1, duty=127)  # create and configure in one go

while(1):
  # count+=1
  # p2.on()
  # sleep_ms(500)
  # p2.off()
  # sleep_ms(500)
  # print(count)
  print(pwm2)                               # view PWM settings
  sleep_ms(500)
  mqttESP.check_msg()
  print(f"RECEIVED alarma: {DATAE['alarma']}")
  # # pwm2.deinit() #stop PWM
  # print("change frec")
  # pwm2.freq(10) #change frecuency
  # print(pwm2)    
  # sleep_ms(1000)
  # print("return frec")
  # pwm2.freq(1)
  # sleep_ms(4000)
  # pwm2.deinit()
  sleep_ms(200)
  PUBLISH(TOPIC_PUB, DATA, mqttESP)
