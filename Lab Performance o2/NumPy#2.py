import numpy as np
array = np.random.rand(100)
normalized_array = (array - np.min(array)) / (np.max(array) - np.min(array))
print(normalized_array)