import board
from analogio import AnalogOut, AnalogIn

light_sensor = AnalogIn(board.A1)
led = AnalogOut(board.A0)



while True:
  led.value = (light_sensor.value + 100)
  
