# Sample input
text = "Hello World! Python is Fun."

# Initialize counters
uppercase_count = 0
lowercase_count = 0

# Loop through each character and count
for char in text:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

# Print the original text and counts
print("Original Text:", text)
print("Number of Uppercase Letters:", uppercase_count)
print("Number of Lowercase Letters:", lowercase_count)