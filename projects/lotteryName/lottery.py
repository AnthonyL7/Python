#Gather input from user
import random 
list = []
inputs = 4
for i in range(inputs):
  gamertag =  input("Gamertag: ")
  list.append(gamertag)

chosen = random.choice(list)
print(f"The chosen one is: {chosen}")
