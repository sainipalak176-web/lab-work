# Print all divisors of a number

# Input
n = int(input())     # Example input: 12

# Find and print divisors
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# Example Output:
# 1
# 2
# 3
# 4
# 6
# 12