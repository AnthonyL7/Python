def digital_root(n):
        while n >= 10:
                n = sum(int(digit) for digit in str(n))
        print(n)


digital_root(493193)