# Sort dictionary by values

# Input
n = int(input())   # Number of elements
data = {}

# Read key-value pairs
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value

# Sort dictionary by values
sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))

# Output
print(sorted_dict)

# Example Output:
# {'A': 10, 'C': 20, 'B': 30}