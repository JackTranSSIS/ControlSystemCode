import time
import board
from analogio import AnalogOut

led = AnalogOut(board.A0)



while True:
  for i in range(0, 65535, 50):
    led.value = i
    
    time.sleep(0.2)
    
  led.value = 0
