# Sample inputs
str1 = "listen"
str2 = "silent"

# Remove spaces and convert to lowercase for uniform comparison
str1_clean = str1.replace(" ", "").lower()
str2_clean = str2.replace(" ", "").lower()

# Check if sorted characters of both strings are the same
if sorted(str1_clean) == sorted(str2_clean):
    result = "The strings are anagrams."
else:
    result = "The strings are not anagrams."

# Print the output within the code
print("String 1:", str1)
print("String 2:", str2)
print(result)