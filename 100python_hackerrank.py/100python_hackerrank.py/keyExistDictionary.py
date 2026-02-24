# Check whether key exists in dictionary

# Input
n = int(input())   # Number of elements
data = {}

# Read key-value pairs
for i in range(n):
    key = input()
    value = int(input())
    data[key] = value

# Key to check
check_key = input()   # Example input: B

# Check existence
if check_key in data:
    print("Key exists")
else:
    print("Key does not exist")

# Example Output:
# Key exists