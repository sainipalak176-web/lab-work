# Sort dictionary by keys

# Input
n = int(input())   # Number of elements
data = {}

# Read key-value pairs
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value

# Sort dictionary by keys
sorted_dict = {}

for key in sorted(data.keys()):
    sorted_dict[key] = data[key]

# Output
print(sorted_dict)

# Example Output:
# {'A': 10, 'B': 20, 'C': 30}