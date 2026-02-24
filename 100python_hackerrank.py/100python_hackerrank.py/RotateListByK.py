# Rotate a list by K positions

# Input
numbers = list(map(int, input().split()))
# Example input: 1 2 3 4 5

k = int(input())     # Example input: 2

# Length of list
n = len(numbers)

# Handle k greater than list size
k = k % n

# Rotate list
rotated_list = numbers[k:] + numbers[:k]

# Output
print(rotated_list)   # Output: [3, 4, 5, 1, 2]