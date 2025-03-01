def invert(lst):
  empty = []
  append = 0
  if lst is []:
     print(empty)
  else:
    for i in lst:
      if i > 0:
        append = i * -1
      else:
        append = i * -1
      empty.append(append)
    print(empty)
invert([1,-2,3,-4,5])