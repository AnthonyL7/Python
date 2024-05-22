#Return a string's even characters
def even_chars(st):
  
  for i in range(0, len(st)):
    if i % 2 == 1:
        print(st[i])

even_chars("abcdefghijklm")