from machine import Pin, Timer

toggle = 0

#Initialize the onboard LED as output
led = Pin(2,Pin.OUT)

# Toggle LED functionality
def BlinkLED(timer_one):
    global toggle
    if toggle == 1:
        led.off()
        toggle = 0
    else:
        led.on()
        toggle = 1

# Initialize timer_one. Used for toggling the on board LED
timer_one = Timer(-1)

# Timer one initialization for on board blinking LED at 200mS interval
timer_one.init(freq=5, mode=Timer.PERIODIC, callback=BlinkLED)