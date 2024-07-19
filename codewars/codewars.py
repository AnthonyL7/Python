import re

def printer_error(s):

  range_count = 0
  for char in s:
    if char not in 'abcdefghijklm':
      range_count += 1
  string = f"{range_count}/{len(s)}"
  print(string)
  
    
printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu")