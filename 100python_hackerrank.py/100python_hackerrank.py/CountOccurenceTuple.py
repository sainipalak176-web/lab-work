# Count occurrence of element in tuple

# Input
values = tuple(map(int, input().split()))
# Example input: 1 2 2 3 4 2 5

element = int(input())   # Example input: 2

# Count occurrence
count = 0
for num in values:
    if num == element:
        count += 1

# Output
print(count)   # Output: 3