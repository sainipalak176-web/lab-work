def char_frequency(s):
    freq = {}
    
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    return freq

# Example
text = "hello"
print(char_frequency(text))
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}