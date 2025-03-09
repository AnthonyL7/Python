def check_for_factor(base, factor):
    if base%factor == 0:
        print('true')
        return True
    else:
        print('false')
        return False

check_for_factor(10,2)