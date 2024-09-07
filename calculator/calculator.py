num1 = input("Enter first number: ")
operation = input("Enter operation: ")
num2 = input("Enter second number: ")

num2int = int(num2)
num1int = int(num1)


if operation == "+" or operation == "add"or operation == "addition":
    print(num1," + ",num2, "=",num1int+num2int)

elif operation == "-" or operation == "subtract" or operation == "subtraction":
    print(num1," - ",num2, "=",num1int-num2int)

elif operation == "/" or operation == "divide" or operation == "division":
    if num2int == 0:
        print("you cant divide by zero stupid head")
    else:
        print(num1," / ",num2, "=",num1int/num2int)


elif operation == "*" or operation == "multiply" or operation == "multiplication":
    print(num1," * ",num2, "=",num1int*num2int)
