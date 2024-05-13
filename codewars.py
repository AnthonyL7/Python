# Write a function which calculates the average of the numbers in a given list.
def find_average(numbers):
    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)
        print(average)
    elif len(numbers) == 0:
        print(0) 


find_average([])