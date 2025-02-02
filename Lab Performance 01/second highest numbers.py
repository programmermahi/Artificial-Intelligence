list_val = []  
  
num_list = int(input("Enter number of elements in list: "))  
  
  
for i in range(1, num_list + 1):  
    element = int(input("Enter the elements: "))  
    list_val.append(element)  
  
  
list_val.sort()  
      
print("Second largest element is:", list_val[-2])  