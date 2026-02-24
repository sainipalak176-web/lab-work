# Merge two lists and remove duplicates

# Input
list1 = list(map(int, input().split()))
# Example input: 1 2 3 4

list2 = list(map(int, input().split()))
# Example input: 3 4 5 6

# Merge lists
merged_list = list1 + list2

# Remove duplicates
unique_list = []

for num in merged_list:
    if num not in unique_list:
        unique_list.append(num)

# Output
print(unique_list)   # Output: [1, 2, 3, 4, 5, 6]