# Create dictionary from two lists

# Input
keys = input().split()        # Example input: A B C
values = list(map(int, input().split()))   # Example input: 10 20 30

# Create dictionary
data = {}
for i in range(len(keys)):
    data[keys[i]] = values[i]

# Output
print(data)

# Example Output:
# {'A': 10, 'B': 20, 'C': 30}