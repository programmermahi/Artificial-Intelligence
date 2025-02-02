def find_largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

largest = find_largest(num1, num2)
print(f"The largest number between {num1} and {num2} is: {largest}")