#Given a list of integers, determine whether the sum of its elements is odd or even.
#Give your answer as a string matching "odd" or "even"

def odd_or_even(list):
  add = 0
  for i in list:
    add += i
  if add % 2 == 0:
    print("even")
  else: 
    print("odd")
    

odd_or_even([0])
  