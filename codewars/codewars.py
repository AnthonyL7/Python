def sum_digits(number):
  digits = [int(digit) for digit in str(abs(number))]
  print(sum(digits))

sum_digits(-32)

