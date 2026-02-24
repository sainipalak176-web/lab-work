# Find largest element in a list

# Input
numbers = list(map(int, input().split()))
# Example input: 10 25 7 40 15

# Assume first element is largest
largest = numbers[0]

# Find largest using loop
for num in numbers:
    if num > largest:
        largest = num

# Output
print(largest)   # Output: 40