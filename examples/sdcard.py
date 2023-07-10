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

import machine
from machine import Pin, SPI, SoftSPI
import sdcard
import os

toggle = 0

#Initialize the onboard LED as output
led = machine.Pin(2,machine.Pin.OUT)

# Toggle LED functionality
def BlinkLED(timer_one):
    global toggle
    if toggle == 1:
        led.value(0)
        toggle = 0
    else:
        led.value(1)
        toggle = 1

# Initialize the SD card
#######Hardware SPI#######
##Default SPI pins
    # SPI  |  MOSI  |  MISO  |  SCLK  |   CS   |
    # VSPI | GPIO23 | GPIO19 | GPIO18 | GPIO5  |
    # HSPI | GPIO13 | GPIO12 | GPIO14 | GPIO15 |
# hspi = SPI(1, 10000000)
# hspi = SPI(1, 10000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
# vspi = SPI(2, baudrate=80000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
######Software SPI#########
spi=SoftSPI(1 ,sck=Pin(14),mosi=Pin(12),miso=Pin(13)) #default baudrate 100Khz
sd=sdcard.SDCard(spi,Pin(27))

# Create a instance of MicroPython Unix-like Virtual File System (VFS),
vfs=os.VfsFat(sd)

# Mount the SD card
os.mount(sd,'/sd')

# Debug print SD card directory and files
print(os.listdir('/sd'))

# Create / Open a file in write mode.
# Write mode creates a new file.
# If  already file exists. Then, it overwrites the file.
file = open("/sd/sample.txt","w")

# Write sample text
for i in range(20):
    file.write("Sample text = %s\r\n" % i)
    
# Close the file
file.close()

# Again, open the file in "append mode" for appending a line
file = open("/sd/sample.txt","a")
file.write("Appended Sample Text at the END \n")
file.close()

# Open the file in "read mode". 
# Read the file and print the text on debug port.
file = open("/sd/sample.txt", "r")
if file != 0:
    print("Reading from SD card")
    read_data = file.read()
    print (read_data)
file.close()

# Initialize timer_one. Used for toggling the on board LED
timer_one = machine.Timer(0)

# Timer one initialization for on board blinking LED at 200mS interval
timer_one.init(freq=5, mode=machine.Timer.PERIODIC, callback=BlinkLED)