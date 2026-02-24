# Generate Fibonacci series using for loop

# Input
n = int(input())      # Example input: 7

# First two terms
a = 0
b = 1

# Print Fibonacci series
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# Example Output:
# 0 1 1 2 3 5 8