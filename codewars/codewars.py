# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#Implement the function which takes an array containing the names of people that like an item.

def likes(names):
  
  #Create conditional statement to show that no one likes this
  if not names:
    print('no one likes this')
  
  #Create elif conditional statements to show that one more people like it
  elif len(names) == 1:
    print(F"{names[0]} likes this")
  elif len(names) == 2:
    print(F"{names[0]} and {names[1]} like this")
  elif len(names) == 3:
    print(F"{names[0]}, {names[1]} and {names[2]} like this")
  elif len(names) >= 4:
    print(F"{names[0]}, {names[1]} and 2 others like this")

likes(["Max", "John", "Mark"])