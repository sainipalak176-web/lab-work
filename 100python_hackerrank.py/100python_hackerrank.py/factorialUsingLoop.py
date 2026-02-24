# Find factorial using for loop

# Input
n = int(input())     # Example input: 5

# Initialize factorial
fact = 1

# For loop to calculate factorial
for i in range(1, n + 1):
    fact = fact * i

# Output
print(fact)          # Output: 120