# Find common elements between two lists

# Input
list1 = list(map(int, input().split()))
# Example input: 1 2 3 4 5

list2 = list(map(int, input().split()))
# Example input: 3 4 5 6 7

# Find common elements
common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

# Output
print(common)   # Output: [3, 4, 5]