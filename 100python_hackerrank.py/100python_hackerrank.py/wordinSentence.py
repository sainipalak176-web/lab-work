# Count number of words in a sentence

# Input
sentence = input()   # Example input: Hello world this is Python

# Split sentence into words
words = sentence.split()

# Count words
count = 0
for word in words:
    count += 1

# Output
print(count)         # Output: 5