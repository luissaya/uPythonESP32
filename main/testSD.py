'''
https://docs.micropython.org/en/latest/library/machine.SDCard.html#machine-sdcard
https://docs.micropython.org/en/latest/esp32/quickref.html#hardware-spi-bus
https://www.instructables.com/ESP32-Micro-SD-Card-Interface/
# Demonstrates ESP32 interface to MicroSD Card Adapter
# Create a text file and write running numbers.
# Open text file, read and print the content on debug port
  
* The ESP32 pin connections for MicroSD Card Adapter SPI

# MicroSD Card Adapter Power Pins
* MicroSD VCC pin to ESP32 +5V
* MicroSD GND pin to ESP32 GND

# MicroSD SPI Pins
* MicroSD MISO pin to ESP32 GPIO13
* MicroSD MOSI pin to ESP32 GPIO12
* MicroSD SCK pin to ESP32 GPIO14
* MicroSD CS pin to ESP32 GPIO27
'''
import os
from machine import Pin, SoftSPI, SDCard

# import sdcard

# Initialize the SD card
# Slot 2 uses pins sck=18, cs=5, miso=19, mosi=23
# vspi = SPI(2, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
# sd = SDCard(vspi,Pin(5))
# sd = SDCard(slot=2, width=1, sck=18, cs=5, miso=19, mosi=23)
# sd = SDCard(slot=2, width=1, sck=Pin(18), cs=Pin(5), miso=Pin(19), mosi=Pin(23))
# sd = SDCard(slot=2)
spisd = SoftSPI(-1, miso=Pin(13), mosi=Pin(12),sck=Pin(14))
sd = SDCard(spisd,Pin(27))

print(os.listdir())
# Create a instance of MicroPython Unix-like Virtual File System (VFS),
vfs=os.VfsFat(sd)

# Mount the SD card
os.mount(vfs,'/sd')
# os.umount('/sd')     # eject

# Debug print SD card directory and files
print(os.listdir())

# # Create / Open a file in write mode.
# # Write mode creates a new file.
# # If  already file exists. Then, it overwrites the file.
# file = open("/sd/sample.txt","w")

# # Write sample text
# for i in range(20):
#     file.write("Sample text = %s\r\n" % i)
    
# # Close the file
# file.close()

# # Again, open the file in "append mode" for appending a line
# file = open("/sd/sample.txt","a")
# file.write("Appended Sample Text at the END \n")
# file.close()

# # Open the file in "read mode". 
# # Read the file and print the text on debug port.
# file = open("/sd/sample.txt", "r")
# if file != 0:
#     print("Reading from SD card")
#     read_data = file.read()
#     print (read_data)
# file.close()