# Find smallest element in a list

# Input
numbers = list(map(int, input().split()))
# Example input: 10 25 7 40 15

# Assume first element is smallest
smallest = numbers[0]

# Find smallest using loop
for num in numbers:
    if num < smallest:
        smallest = num

# Output
print(smallest)   # Output: 7