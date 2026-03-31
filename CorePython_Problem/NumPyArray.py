import numpy as np

# Input data
arr = np.array([10, 20, 30, 40, 50])

# Calculate values
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

# Print results
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)

# Output:
# Mean: 30.0
# Median: 30.0
# Standard Deviation: 14.142135623730951