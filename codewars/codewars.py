
def number(lines):
  if isinstance(lines, list):
    add = ["1: ", "2: ", "3: " ]
    lst = zip(add, lines)
    new_list = [num + char for num,char in lst]
    print(new_list)
  else:
    return []

number(["a", "b", "c"])