#square(n) Sum
def square_sum(numbers):
  total = 0
  for i in numbers:
    total += i ** 2
  print(total)

square_sum([0,3,4,5])