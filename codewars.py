#Given an array of integers, return a new array with each value doubled.
def maps(a):
      #using a list comprehension to display a list
      print([i * 2 for i in a])
      
      #using a for loop to display each value doubled
      for i in a:
          multi = i * 2
          print(multi)

maps([-1,0,2,3,4,5,6,7,8,9,10])