def count_positives_sum_negatives(arr):
  positive_sum = 0
  negative_sum = 0
  empty = []
  for i in arr:
    if i > 0:
      positive_sum += i
    elif i < 0:
      negative_sum += i
    else:
      print(empty)
  empty.insert(0, positive_sum)
  empty.append(negative_sum)
  print(empty)
count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])