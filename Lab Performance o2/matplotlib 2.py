import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West']
revenue = [150000, 200000, 180000, 220000]  

plt.figure(figsize=(8, 5))
plt.bar(regions, revenue, color=['blue', 'green', 'orange', 'red'])

plt.xlabel('Region')
plt.ylabel('Sales Revenue ($)')
plt.title('Sales Revenue Across Different Regions')
plt.grid(axis='y')  

plt.show()