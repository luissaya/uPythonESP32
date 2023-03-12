from machine import Pin
import time
import network

ssid="Sayaverde"
key="sayaverdeporobravo"

p2=Pin(2,Pin.OUT)
p2.on()
count=0
#wlan = network.WLAN(network.STA_IF) # create station interface
#wlan.active(True)       # activate the interface
#wlan.scan()             # scan for access points
#wlan.isconnected()      # check if the station is connected to an AP
#wlan.connect('ssid', 'key') # connect to an AP
#wlan.config('mac')      # get the interface's MAC address
#wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

#ap = network.WLAN(network.AP_IF) # create access-point interface
#ap.config(ssid='ESP-AP') # set the SSID of the access point
#ap.config(max_clients=10) # set how many clients can connect to the network
#ap.active(True)         # activate the interface
def do_connect(SSID,PASS):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID,PASS)
        while not wlan.isconnected():
            print('.')
            p2.on()
            time.sleep_ms(100)
            p2.off()
            pass
    print('network config: ', wlan.ifconfig())
    print('MAC address: ',wlan.config('mac') )

    # print some text to the serial console
print('Hello MicroPython!')
do_connect(ssid,key)
while(1):
    count+=1
    p2.on()
    time.sleep_ms(500)
    p2.off()
    time.sleep_ms(500)
    print(count)