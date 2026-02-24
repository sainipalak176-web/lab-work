# Reverse a string using for loop

# Input
text = input()      # Example input: hello

# Initialize empty string
reverse_text = ""

# Reverse using for loop
for i in range(len(text) - 1, -1, -1):
    reverse_text += text[i]

# Output
print(reverse_text)   # Output: olleh