# Count vowels in a string

# Input
text = input()      # Example input: hello

# Initialize counter
count = 0

# Vowel checking
for ch in text:
    if ch.lower() in "aeiou":
        count += 1

# Output
print(count)        # Output: 2