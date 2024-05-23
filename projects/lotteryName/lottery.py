#Gather input from user
import random 
#Ask for how many players they have 
players = int(input("How many are you going to put in the lottery: "))

#Create an empty list
list = []

#Create a for loop to iterate 
for i in range(players):
  gamertag =  input("Gamertag: ")
  list.append(gamertag)

chosen = random.choice(list)
print(f"The chosen one is: {chosen}")
