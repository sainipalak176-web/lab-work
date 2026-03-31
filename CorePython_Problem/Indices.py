import numpy as np

# Input array
arr = np.array([10, 25, 30, 15, 40])

# Given value
value = 20

# Find indices
indices = np.where(arr > value)

# Output
print("Indices:", indices)