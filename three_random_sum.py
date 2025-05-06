import random
number= random.randint(100,999)
print("Random three number :", number)

digit_sum=sum(int(digit) for digit in str(number))
print("sum of digit :",digit_sum)

if digit_sum %2 == 0:
    print("The sum is even")
else:
    print("the sum is odd")