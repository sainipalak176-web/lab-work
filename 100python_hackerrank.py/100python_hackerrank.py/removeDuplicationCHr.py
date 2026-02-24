# Sample input
text = "programming"

# Initialize an empty string to store result
result = ""

# Loop through each character and add it to result if not already added
for char in text:
    if char not in result:
        result += char

# Print original text and result
print("Original Text: " + text)
print("Text after removing duplicates: " + result)