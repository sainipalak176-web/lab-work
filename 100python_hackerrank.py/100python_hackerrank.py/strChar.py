# Sample input
text = "abc"

# Initialize list to store substrings
substrings = []

# Generate all substrings
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        substrings.append(text[i:j])

# Print original text and all substrings
print("Original Text:", text)
print("All Substrings:", substrings)