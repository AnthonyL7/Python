def digital_root(n):
        while n >= 10:
                n = [int(digit) for digit in str(n)]
                n = sum(n)     
        
        print(n)


digital_root(942)
