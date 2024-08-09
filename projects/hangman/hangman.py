from words import words
import random

#def random_generator():
if all(isinstance(i, str) for i in words):
  random_word = random.choice(words)
  print(random_word)


def game(rand):
  
  count = ""
  for i in rand:
    if type(i) == str:
      count += "_"
  print(count)

game(random_word)

def initiate_game(word):
  user_input = input("Try to guess the word one letter at a time: ")
  for i in word: 
    if user_input.lower() in word: 
      print(True)
    else: 
      print(False)

initiate_game(random_word)