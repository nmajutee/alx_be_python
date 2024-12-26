# Match Case statements for handling multiple operations in a simple calculator program.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        result = num1 + num2
        print("The result is {}".format(result))
    case "-":
        result = num1 - num2
        print("The result is {}".format(result))
    case "*":
        result = num1 - num2 
        print("The result is {}".format(result))
    case "/":
        if num2 != 0:
            result = num1 / num2
            print("The result is {}".format(result))
        else:
            print("Cannot divide by zero.")
    case _:
        print("Select the right operator")