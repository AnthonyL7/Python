def is_valid_walk(walk):

    ns_count = 0
    ew_count = 0
    if len(walk) > 10 or len(walk) < 10:
       print(False)
    else:
      for i in walk:
        if i == 'n':
            ns_count += 1
        elif i == 's':
            ns_count -= 1
        elif i == 'e':
            ew_count += 1
        elif i == 'w':
            ew_count -= 1
      if ns_count == 0 and ew_count == 0:
        print(True)
      else:
        print(False)
      
    

is_valid_walk(['n', 's', 'e', 'w', 'n', 's', 'n', 'w', 'n', 's'])