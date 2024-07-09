def find_it(seq):
  if isinstance(seq, str):
    return False
  else: 
    i = dict.fromkeys(seq,0)
    for x in seq:
      i[x] += 1
    for key, value in i.items():
      if value % 2 != 0:
        print(key)

  pass

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])