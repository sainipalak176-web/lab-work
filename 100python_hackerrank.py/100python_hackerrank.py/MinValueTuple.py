# Find minimum value in a tuple

# Input
values = tuple(map(int, input().split()))
# Example input: 10 25 7 40 15

# Assume first element is minimum
minimum = values[0]

# Find minimum using loop
for num in values:
    if num < minimum:
        minimum = num

# Output
print(minimum)   # Output: 7