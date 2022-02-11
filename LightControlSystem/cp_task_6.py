import board
from analogio import AnalogOut, AnalogIn

light_sensor = AnalogIn(board.A1)
led = AnalogOut(board.A0)

led.value = 60000


while True:
