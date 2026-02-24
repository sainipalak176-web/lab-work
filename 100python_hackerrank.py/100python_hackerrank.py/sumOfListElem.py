# Find sum of list elements

# Input
numbers = list(map(int, input().split()))
# Example input: 1 2 3 4 5

# Calculate sum
total = 0
for num in numbers:
    total += num

# Output
print(total)   # Output: 15