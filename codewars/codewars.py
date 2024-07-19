def open_or_senior(data):
  lst = []
  for age, score in data:
    if age >= 55 and score > 7:
      lst.append("Senior")
    else:
      lst.append("Open")
  print(lst)
  pass

open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])