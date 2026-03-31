# Example 1
n = 153

original = n
num_digits = len(str(n))

sum_of_powers = 0
temp = n

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

if sum_of_powers == original:
    print(True)   # Output: True
else:
    print(False)


# Example 2
n = 123

original = n
num_digits = len(str(n))

sum_of_powers = 0
temp = n

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

if sum_of_powers == original:
    print(True)
else:
    print(False)  # Output: False