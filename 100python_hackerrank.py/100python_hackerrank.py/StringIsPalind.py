# Check whether string is palindrome

# Input
text = input()       # Example input: madam

# Reverse the string
reverse_text = ""
for i in range(len(text) - 1, -1, -1):
    reverse_text += text[i]

# Check palindrome
if text == reverse_text:
    print("Palindrome")
else:
    print("Not Palindrome")

# Example Output:
# Palindrome