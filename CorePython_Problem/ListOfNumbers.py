# Input data
numbers = [1, 2, 2, 3, 4, 3, 5, 1]

# Remove duplicates while maintaining order
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Print result
print(unique_numbers)
# Output: [1, 2, 3, 4, 5]