
def calculate():

    stopLooping = False
    while not stopLooping:
        # Take 2 operands and operator from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter '+' to add,'-' to subtract, '/' to divide, '*' to multiply, and 'q' to quit: ")
        #using if statements to execute the operation
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "/":
            print(num1 / num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "q":
            #This will break the loop once user inputs q 
            stopLooping = True

print("Testing test-branch")

calculate()