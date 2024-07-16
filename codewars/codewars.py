def descending_order(num):
  string = str(num)
  sorted_string = ''.join(sorted(string, reverse=True))
  number = int(sorted_string)
  print(number)
  pass

descending_order(65321000)