# Find average of list elements

# Input
numbers = list(map(int, input().split()))
# Example input: 10 20 30 40 50

# Calculate sum
total = 0
for num in numbers:
    total += num

# Calculate average
average = total / len(numbers)

# Output
print(average)   # Output: 30.0