# Sample sentence
sentence = "Python programming is both fun and educational"

# Split the sentence into words
words = sentence.split()

# Initialize variables to store the longest word
longest_word = ""
max_length = 0

# Find the longest word
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

# Print the output within the code
print("Original Sentence: " + sentence)
print("Longest Word: " + longest_word)