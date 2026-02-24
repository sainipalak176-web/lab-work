# Count vowels using function

# Function to count vowels
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count

# Input
s = input()        # Example input: hello

# Output
print(count_vowels(s))   # Output: 2