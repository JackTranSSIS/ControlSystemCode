import board
from analogio import AnalogIn
import time



input = AnalogIn(board.A0)

while True:
  print(input)
  time.sleep(0.5)
