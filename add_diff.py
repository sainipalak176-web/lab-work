#user-defined function to find addition and difference
def add_and_difference(a,b):
    addition= a + b
    difference = a - b
    return addition, difference
 # Taking input from user
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    #calling the function
    sum_result,diff_result = add_and_difference(num1,num2)
    #display the result
    print("Addition =",sum_result)
    print("Difference =",diff_result)