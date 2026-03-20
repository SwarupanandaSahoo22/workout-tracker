# Simple Calculaor

Operator = input("Enter your operator (+ - * /): ").strip()
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

if Operator == "+":
    result = (round(num1 + num2, 3))
    print(result)

elif Operator == "-":
    result = (round(num1 - num2, 3))
    print(result)

elif Operator == "*":
    result = (round(num1 * num2, 3))
    print(result)

elif Operator == "/":
    if num2 == 0:
        print("Can not divide by zero.")
    else:
        print(round(num1 / num2, 3))

else:
    print(f""""{Operator}" is not a valid operator.""")