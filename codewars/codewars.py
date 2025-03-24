def find_nb(m):
  n = 1
  volume = (n(n+1)//2)**2 
  while volume < m:
    n += 1
    volume = (n(n+1)//2) ** 2
  return n if volume ==  m else -1
find_nb(4)

