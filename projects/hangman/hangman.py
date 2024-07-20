from words import words

def random():
  import random
  if all(isinstance(i, str) for i in words):
    random_word = random.choice(words)
    print(random_word)

random()

def game():
  count = ""
  for i in random:
    if type(i) == str:
      count += "_"
  print(count)