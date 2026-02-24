# Perform difference of two sets

# Input
set1 = set(map(int, input().split()))
# Example input: 1 2 3 4

set2 = set(map(int, input().split()))
# Example input: 3 4 5 6

# Difference of sets (elements in set1 but not in set2)
difference_set = set1 - set2

# Output
print(difference_set)   # Output: {1, 2}