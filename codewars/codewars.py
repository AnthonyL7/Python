def to_jaden_case(string):
  words = string.split()
  capitalized_words = [word.capitalize() for word in words]

  capitalized_string = ' '.join(capitalized_words)
  print(capitalized_string)

  pass

to_jaden_case("How can mirrors be real if our eyes aren't real")