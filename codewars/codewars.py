
def persistence(n):
  count = 0
  while n >= 10:
    split = [int(n) for n in str(n)]
    product = 1 
    for num in split:
      product *= num
    n = product
    count += 1
  print(count)
    

persistence(999)