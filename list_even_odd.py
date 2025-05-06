import random
number=[random.randint(0,100) for _ in range(10)]
print(" Number is :",number)

even_count=0
odd_count=0

for num in number:
    if num %2 == 0:
        even_count =even_count+1
    else:
        odd_count=odd_count+1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
    

import random

# Generate a random list of 10 integers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(10)]
print("Randomly generated list:", numbers)

# Lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Separate even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print results
print("Even numbers:", even_numbers)
print("Total even numbers:", len(even_numbers))

print("Odd numbers:", odd_numbers)
print("Total odd numbers:", len(odd_numbers))
