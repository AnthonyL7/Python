def square_digits(num):
  digits = []
  if num > 0: 
    for digit in str(num):
      digit = int(digit)
      digits.append(digit)
    square_digits = [digit ** 2 for digit in digits]
    print(int("".join(map(str, square_digits))))
  
  else: 
    return 0
  pass

square_digits(0)