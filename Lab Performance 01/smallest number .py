numbers = [10, 20, 5, 40, 30]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(f"The smallest number is: {smallest}")