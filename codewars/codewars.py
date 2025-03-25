def friend(x):
  result = [name for name in x if len(name) == 4]

  print(result)
friend(["Ryan", "Kieran", "Jason", "Yous"])