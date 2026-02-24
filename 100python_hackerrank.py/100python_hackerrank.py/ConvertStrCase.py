# Sample input
text = "hELlo wORld, thIs is PYthon"

# Split the text into words
words = text.split()

# Convert each word to title case manually
title_case_words = []
for word in words:
    if len(word) > 0:
        # Capitalize first letter and make rest lowercase
        title_word = word[0].upper() + word[1:].lower()
        title_case_words.append(title_word)
    else:
        title_case_words.append(word)

# Join words back into a string
title_case_text = ' '.join(title_case_words)

# Print the output
print("Original Text: ", text)
print("Title Case Text:", title_case_text)