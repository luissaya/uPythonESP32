# source https://mpython.readthedocs.io/en/latest/library/micropython/network.html
import time
import network
import ubinascii
import json
from umqtt.simple import MQTTClient


class WIFI:
  def __init__(self, debug = True):
    self.wlan = network.WLAN(network.STA_IF)
    self.debug = debug
    self.wlan.active(True)

  def modeSTA(self, ssid, password):
    if not self.wlan.isconnected():
      if self.debug: print('connecting to network...')
      self.wlan.connect(ssid,password)
      while not self.wlan.isconnected():
          if self.debug: print('.')
          time.sleep_ms(100)
          pass
    if self.debug: print('network config: ', self.wlan.ifconfig())
    if self.debug: print('MAC address: ', self.wlan.config('mac') )
    self.macADDRESS = self.__hex_mac_addr(self.wlan.config('mac'))
    self.ipADDRESS = self.wlan.ifconfig()[0] #(ip, subnet, gateway, dns)
  
  def __hex_mac_addr(self, macBinary):
    macAddr = ubinascii.hexlify(macBinary,':').decode().upper()
    return macAddr

class MQTT:
  def __init__(self, clientID, broker, port, topic_sub, debug = True):
    self.mqtt = MQTTClient(clientID, broker, port)
    self.debug = debug
    self.topic_sub = topic_sub
    self.mqtt.set_callback(self.__callback_sub()) 
    self.mqtt.connect()
    self.mqtt.subscribe(topic_sub)
    if debug : print("Connected to MQTT  Broker : {broker}, Port: {port}, client ID: {clientID} and subscribed to the topic: {topic_sub}")

  #run object.mqtt.check_msg() to periodically check the incoming data
  def __callback_sub(topic, payload):
    if self.debug : print("Received from Topic: {topic}, message: {payload}")

  def subscribeMQTT(self, topic):
    self.mqtt.subscribe(topic)
    if self.debug : print("Subscribed to the topic: {topic}") 

  #topic is bites and message is a dictionary
  def publishMQTT(self, topic, message):
    payload = json.dumps(message).encode()
    self.mqtt.publish(topic, message)
    if self.debug : print("Publish to the topic: {topic}, the message: {message}")