from machine import Pin, PWM
from time import sleep

pwmLed = PWM(Pin(2))         # create PWM object from a pin
freq = pwmLed.freq()         # get current frequency (default 5kHz)
pwmLed.freq(1000)            # set PWM frequency from 1Hz to 40MHz

duty = pwmLed.duty()         # get current duty cycle, range 0-1023 (default 512, 50%)
pwmLed.duty(0)             # set duty cycle from 0 to 1023 as a ratio duty/1023, (now 25%)

# duty_u16 = pwm0.duty_u16() # get current duty cycle, range 0-65535
# pwm0.duty_u16(2**16*3//4)  # set duty cycle from 0 to 65535 as a ratio duty_u16/65535, (now 75%)

# duty_ns = pwm0.duty_ns()   # get current pulse width in ns
# pwm0.duty_ns(250_000)      # set pulse width in nanoseconds from 0 to 1_000_000_000/freq, (now 25%)

# pwm0.deinit()              # turn off PWM on the pin

# pwm2 = PWM(Pin(2), freq=20000, duty=512)  # create and configure in one go
# print(pwm2)                               # view PWM settings
count = 0
dt=0
while(1):
    dt=count*1023/100.0
    pwmLed.duty(int(dt))
    if(count==100):
        count=0
    else:
        count+=1
    sleep(0.2)
