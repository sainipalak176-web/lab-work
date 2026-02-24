# Calculate power using recursive function

# Recursive function
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Input
b = int(input())     # Example input: 2
e = int(input())     # Example input: 4

# Output
print(power(b, e))   # Output: 16