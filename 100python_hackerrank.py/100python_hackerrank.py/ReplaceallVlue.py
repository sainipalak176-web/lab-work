# Sample input
text = "Hello World, Python is amazing!"

# Define vowels
vowels = "aeiouAEIOU"

# Initialize an empty string for result
result = ""

# Replace vowels with *
for char in text:
    if char in vowels:
        result += "*"
    else:
        result += char

# Print original text and modified text
print("Original Text: " + text)
print("Modified Text: " + result)