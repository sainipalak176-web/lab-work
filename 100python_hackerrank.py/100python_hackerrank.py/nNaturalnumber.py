# Find sum of first N natural numbers

# Input
n = int(input())      # Example input: 5

# Initialize sum
total = 0

# Calculate sum using for loop
for i in range(1, n + 1):
    total += i

# Output
print(total)          # Output: 15