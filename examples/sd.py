import os, machine



sd = machine.SDCard(slot=2)
vfs=os.VfsFat(sd)
os.mount(sd, "/sd")  # mount
fn = open('/sd/textsd.txt', 'w')
fn.write('some data')
fn.close()
os.listdir('/sd')    # list directory contents
# Slot 2 uses pins sck=18, cs=5, miso=19, mosi=23
# import machine, uos
# uos.mount(machine.SDCard(slot=2, sck=18, miso=19, mosi=23, cs=5), "/sd")