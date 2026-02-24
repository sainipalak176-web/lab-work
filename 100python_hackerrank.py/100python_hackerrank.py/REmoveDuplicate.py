# Remove duplicate elements from list

# Input
numbers = list(map(int, input().split()))
# Example input: 1 2 2 3 4 4 5

# Remove duplicates
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

# Output
print(unique_list)   # Output: [1, 2, 3, 4, 5]