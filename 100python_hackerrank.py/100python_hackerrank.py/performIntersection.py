# Perform intersection of two sets

# Input
set1 = set(map(int, input().split()))
# Example input: 1 2 3 4

set2 = set(map(int, input().split()))
# Example input: 3 4 5 6

# Intersection of sets
intersection_set = set1 & set2

# Output
print(intersection_set)   # Output: {3, 4}