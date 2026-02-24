# Reverse a string without slicing

# Input
text = input()      # Example input: hello

# Initialize empty string for reversed
reverse_text = ""

# Reverse using loop
for i in range(len(text) - 1, -1, -1):
    reverse_text += text[i]

# Output
print(reverse_text)   # Output: olleh