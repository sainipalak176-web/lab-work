# Check whether one set is subset of another

# Input
set1 = set(map(int, input().split()))
# Example input: 1 2

set2 = set(map(int, input().split()))
# Example input: 1 2 3 4

# Check subset
if set1.issubset(set2):
    print("Subset")
else:
    print("Not Subset")

# Output (for example):
# Subset