def even_chars(st):
    if len(st) < 2 or len(st) > 100:
        print("invalid string")
    else:
        chars = []
        for i in range(1, len(st), 2):
            if i % 2 == 1:
               chars.append(st[i])
        print(chars)

even_chars("a")