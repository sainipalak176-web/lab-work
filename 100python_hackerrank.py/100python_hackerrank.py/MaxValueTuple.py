# Find maximum value in a tuple

# Input
values = tuple(map(int, input().split()))
# Example input: 10 25 7 40 15

# Assume first element is maximum
maximum = values[0]

# Find maximum using loop
for num in values:
    if num > maximum:
        maximum = num

# Output
print(maximum)   # Output: 40