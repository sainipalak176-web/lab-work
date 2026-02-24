# Replace negative numbers with zero

# Input
numbers = list(map(int, input().split()))
# Example input: 5 -3 8 -1 2

# Replace negatives with zero
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

# Output
print(numbers)   # Output: [5, 0, 8, 0, 2]