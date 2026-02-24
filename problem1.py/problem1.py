# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Before swap: num1 = {num1}, num2 = {num2}")

# Swapping without a third variable
num1, num2 = num2, num1

print(f"After swap: num1 = {num1}, num2 = {num2}")