# Sort a list without using sort method

# Input
numbers = list(map(int, input().split()))
# Example input: 5 2 8 1 3

# Bubble Sort logic
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Output
print(numbers)   # Output: [1, 2, 3, 5, 8]