import board
from analogio import AnalogOut, AnalogIn

light_sensor = AnalogIn(board.A0)
led = AnalogOut(board.A1)



while True:
  led.value = (light_sensor.value + 100)
  
