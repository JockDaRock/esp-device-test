import machine
import time
p0 = machine.Pin(2, machine.Pin.OUT)

def toggle(p):
    p.value(not p.value())

while True:
    toggle(p0)
    time.sleep(1)