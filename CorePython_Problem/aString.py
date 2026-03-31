# Input data
s = "programming"

# Find first non-repeating character
for char in s:
    if s.count(char) == 1:
        print(char)
        break

# Output: p