import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22, 24, 21, 23, 25, 26, 24]  

plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b', label='Temperature (°C)')

plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variations Over a Week')
plt.grid(True)
plt.legend()

plt.show()