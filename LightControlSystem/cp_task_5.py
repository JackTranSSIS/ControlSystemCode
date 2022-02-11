import board
from analogio import AnalogOut, AnalogIn

light_sensor = AnalogIn(board.A0)
led = AnalogOut(board.A1

led.value = 60000


while True:
  print(light_sensor.value)
