# Safely remove a key from dictionary

# Input
n = int(input())   # Number of elements
data = {}

# Read key-value pairs
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value

# Key to remove
remove_key = input()   # Example input: B

# Safely remove key
data.pop(remove_key, None)

# Output
print(data)

# Example Output:
# {'A': 10, 'C': 30}   # If B existed, it is removed