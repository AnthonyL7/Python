def xo(s):
    s = s.lower()
    char = 'xo'
    count_x = s.count('x')
    count_o = s.count('o')
    if 'x' not in s and 'o' not in s:
        print(True)
    if 'x' in s and 'o' not in s:
        print(False)
    if 'x' not in s and 'o' in s:
        print(False)
    if count_x % 2 != 0 or count_o % 2 != 0 and count_x == 0 or count_o == 0:
        print(False)
    return True
   

xo('zpzpzpp')