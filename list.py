import random
count=random.randint(10,20)
print("Random number :",count)
number_list = [random.randint(1,100 ) for _ in range(count)]
print("generated list :",number_list)
data={'numbers':number_list}
print("Dictionary :",data)
average=sum(number_list)/len(number_list)
maximum=max(number_list)
minimum=min(number_list)
print("Average :",average)
print("maximum:",maximum)
print("Minimum :",minimum)