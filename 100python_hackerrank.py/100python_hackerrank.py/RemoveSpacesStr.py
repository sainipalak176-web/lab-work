# Remove spaces from string

# Input
text = input()      # Example input: Hello World Python

# Initialize empty string
no_space_text = ""

# Remove spaces using loop
for ch in text:
    if ch != " ":
        no_space_text += ch

# Output
print(no_space_text)   # Output: HelloWorldPython