# Find frequency of each character in string

# Input
text = input()      # Example input: hello

# Dictionary to store frequency
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Output
for key in frequency:
    print(key, ":", frequency[key])

# Example Output:
# h : 1
# e : 1
# l : 2
# o : 1