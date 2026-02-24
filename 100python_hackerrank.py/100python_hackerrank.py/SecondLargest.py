# Find second largest number in list

# Input
numbers = list(map(int, input().split()))
# Example input: 10 25 7 40 15

# Remove duplicates
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Assume first two elements
largest = second_largest = unique_numbers[0]

for num in unique_numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

# Output
print(second_largest)   # Output: 25