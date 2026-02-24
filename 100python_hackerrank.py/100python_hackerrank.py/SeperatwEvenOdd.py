# Separate even and odd numbers from list

# Input
numbers = list(map(int, input().split()))
# Example input: 1 2 3 4 5 6

# Lists for even and odd numbers
even_list = []
odd_list = []

# Separate numbers
for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

# Output
print("Even:", even_list)
print("Odd:", odd_list)

# Example Output:
# Even: [2, 4, 6]
# Odd: [1, 3, 5]