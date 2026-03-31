import numpy as np

# Input array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Replace odd numbers with -1
arr[arr % 2 != 0] = -1

# Output
print("Modified Array:", arr)