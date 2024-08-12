def two_sum(numbers, target):
  for i, val in enumerate(numbers):
    for j, val2 in enumerate(numbers[i+1:], start=i+1):
      if val + val2 == target:
        tuple = (i, j)
  print(tuple)

  
two_sum([1,2,3], 4)
