def odd_ones_out(numbers):
  dict = {}
  result = []
  for i in numbers:
    dict[i] = dict.get(i,0)+1

  for i in numbers:
    if dict[i] % 2 == 0:
      result.append(i)
  print(result)
  

odd_ones_out([1, 1, 2, 2, 3, 3, 3])