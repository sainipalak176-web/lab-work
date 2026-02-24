# Calculate power without using exponent operator

# Input
base = int(input())      # Example input: 2
power = int(input())     # Example input: 3

# Initialize result
result = 1

# Calculate power using for loop
for i in range(power):
    result = result * base

# Output
print(result)            # Output: 8