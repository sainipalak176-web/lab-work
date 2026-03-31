# Input data
data = {"A": 1, "B": 2, "C": 3}

# Swap keys and values
swapped = {value: key for key, value in data.items()}

# Print result
print(swapped)
# Output: {1: 'A', 2: 'B', 3: 'C'}