# Sample input
text = "swiss"

# Initialize variable to store first non-repeating character
first_non_repeating = None

# Loop through each character
for char in text:
    if text.count(char) == 1:
        first_non_repeating = char
        break

# Print original text and the first non-repeating character
print("Original Text:", text)
if first_non_repeating:
    print("First Non-Repeating Character:", first_non_repeating)
else:
    print("No non-repeating character found.")