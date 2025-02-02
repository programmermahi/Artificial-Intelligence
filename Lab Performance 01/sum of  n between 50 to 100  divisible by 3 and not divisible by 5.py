total_sum = 0
divisible_numbers = []

for num in range(50, 101):
    if num % 3 == 0 and num % 5 != 0:
        divisible_numbers.append(num)
        total_sum += num

print(f"Sum of numbers between 50 and 100 divisible by 3 and not by 5: {total_sum}")
print(f"Total numbers between 50 and 100 divisible by{divisible_numbers}")