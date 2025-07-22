# simple calculator python

operation = input("Enter the operation : ")
num1 = float(input("Number : "))
num2 = float(input("Number : "))

if operation == "+" :
    result = num1 + num2
    print(result)

elif operation == "-" :
    result = num1 - num2
    print(result)

elif operation == "*" :
    result = num1 * num2
    print(result)

elif operation == "/" :
    result = num1 / num2
    print(result)

else :
    print(f"{operation} is not valid")