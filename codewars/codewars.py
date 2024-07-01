def xo(s):
    s = s.lower()
    char = 'xo'
    if 'x' not in s or 'o' not in s:
        print(False)
    for i in char:
        count = s.count(i)
        if count % 2 != 0:
            print(False)
    print(True)     

xo('zzoo')