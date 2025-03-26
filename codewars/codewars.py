def password(st):
  has_lower = False
  has_upper = False
  is_digit = False
  if len(st) >= 8:
    for char in st:
      if char.islower():
        has_lower = True
      elif char.isupper():
        has_upper = True
      elif char.isdigit():
        is_digit = True
    if has_lower and has_upper and is_digit:
        print('True')
    else:
      print('False')
  else:
    print('False')

password('abcd1234')