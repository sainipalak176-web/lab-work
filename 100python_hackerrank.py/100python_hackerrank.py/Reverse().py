# Reverse a list without reverse method

# Input
numbers = list(map(int, input().split()))
# Example input: 1 2 3 4 5

# Reverse list using loop
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# Output
print(reversed_list)   # Output: [5, 4, 3, 2, 1]