# Check palindrome string using function

# Function to check palindrome
def is_palindrome(text):
    reverse_text = ""
    for i in range(len(text) - 1, -1, -1):
        reverse_text += text[i]
    return text == reverse_text

# Input
s = input()      # Example input: madam

# Output
if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")

# Output (for input madam):
# Palindrome