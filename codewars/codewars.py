# Find whether the number is a square
import math
def is_square(n):
    if n >= 0:
      if math.sqrt(n) % 1 == 0:
          print(True)
      else: 
          print(False)
    else: 
        print("False")


is_square(-1)

