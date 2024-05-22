#Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    print(numbers[0] + numbers[1])
    

list = [19,5,42,2,77]    
sum_two_smallest_numbers(list)