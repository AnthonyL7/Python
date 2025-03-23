def sum_array(arr):
  if not isinstance(arr, list) or len(arr) < 3:
    print('0')

  arr_copy = arr.copy()
  arr_copy.remove(max(arr_copy))
  arr_copy.remove(min(arr_copy))

  total = sum(arr_copy)
  print(total)

sum_array([1, 1, 11, 2, 3])