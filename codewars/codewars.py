def is_triangle(a, b, c):
  if a > 0 and b > 0 and c > 0:
    if c + b > a and a + b > c and c + a > b:
      print(True)
  print(False)
  pass

is_triangle(7,2,2)