import re

def printer_error(s):
  string = bool(re.search('[a-mA-M]', s))
  print(string)
    
printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")