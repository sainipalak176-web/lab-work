# Find sum of all dictionary values

# Input
n = int(input())   # Number of elements
data = {}

# Read key-value pairs
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value

# Calculate sum of values
total = 0
for value in data.values():
    total += value

# Output
print(total)

# Example Output:
# 60   # If dictionary is {'A': 10, 'B': 20, 'C': 30}