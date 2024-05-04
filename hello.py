userInput = int(input("Write a year date:"))
print("The entered number is:", userInput)

year = userInput

if (year % 4 == 0) and (year % 100 != 0):
  print("its a leap year")
else:
  print("Its not a leap year")
if (year % 400 == 0):
  print("Its not a leap year")


"""if (year % 4 == 0):
  if (year % 100 == 0):
      if (year % 400 == 0):
         print("Its a leap year")
      else:
        print("Not a leap year")
  else:
      print("Its a leap year")
else: 
  print("Not a leap year") 
"""
