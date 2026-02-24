# Perform union of two sets

# Input
set1 = set(map(int, input().split()))
# Example input: 1 2 3 4

set2 = set(map(int, input().split()))
# Example input: 3 4 5 6

# Union of sets
union_set = set1 | set2

# Output
print(union_set)   # Output: {1, 2, 3, 4, 5, 6}