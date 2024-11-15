def get_sum(a,b):
  if a == b:
    return a
  
  start = min(a,b)
  end = max(a,b)
  total = 0 
  total = sum(range(a, b+1))
  print(total)
    

get_sum(0,-1)