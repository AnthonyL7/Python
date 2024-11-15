def correct(s):
  if '0' in s or '5' in s or '1' in s:
    s1 = s.replace("0","O").replace('5', 'S').replace('1','I')
    print(s1)
  pass

correct("DUBL1N")