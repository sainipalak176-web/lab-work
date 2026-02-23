#function to calculate product of two numbers
def product (a,b):
    return a*b
    #function to calculate divison of two numbers
    def divison(a,b):
        if b==0;
        return "divison by zero is not allowed"
        else:
            return a/b
            #taking input from user
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:" ))
            #function calls
            prod_result = product(num1,num2)
            div_result = divison(num1,num2)
            #displaying result
            print("product =",prod_result)
            print("Divison =",div_result)