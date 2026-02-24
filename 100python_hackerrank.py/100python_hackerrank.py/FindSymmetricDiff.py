# Find symmetric difference of two sets

# Input
set1 = set(map(int, input().split()))
# Example input: 1 2 3 4

set2 = set(map(int, input().split()))
# Example input: 3 4 5 6

# Symmetric difference
sym_diff = set1 ^ set2

# Output
print(sym_diff)   # Output: {1, 2, 5, 6}