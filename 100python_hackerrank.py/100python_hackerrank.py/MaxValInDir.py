# Find key with maximum value

# Input
n = int(input())   # Number of elements
data = {}

# Read key-value pairs
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value

# Find key with maximum value
max_key = max(data, key=data.get)

# Output
print(max_key, data[max_key])

# Example Output:
# B 95