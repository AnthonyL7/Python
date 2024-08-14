import re

def order(sentence):
  words = sentence.split()
  match = re.search(r'\d+', sentence)
  sorted_words = sorted(words, key=lambda word: int(re.search(r'\d+', word).group()))

  sorted_sentence = ' '.join(sorted_words)
  print(sorted_sentence)


order("is2 Thi1s T4est 3a")