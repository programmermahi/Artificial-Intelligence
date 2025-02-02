
def sum_of_numbers(*args):
    return sum(args)

numbers = [10, 20, 30, 40, 50]
result = sum_of_numbers(*numbers)
print(f"The sum of the numbers is: {result}")