
n = int(input("Enter the number of terms for the Fibonacci series: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci series with {n} term: {a}")
else:
   
    fib_series = [a, b]
    for _ in range(2, n):
        c = a + b
        fib_series.append(c)
        a, b = b, c


    print(f"Fibonacci series with {n} terms: {fib_series}")