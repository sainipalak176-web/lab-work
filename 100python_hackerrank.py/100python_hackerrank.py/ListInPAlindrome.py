# Check whether list is palindrome

# Input
numbers = list(map(int, input().split()))
# Example input: 1 2 3 2 1

# Check palindrome
is_palindrome = True

for i in range(len(numbers) // 2):
    if numbers[i] != numbers[len(numbers) - 1 - i]:
        is_palindrome = False
        break

# Output
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output (for example):
# Palindrome