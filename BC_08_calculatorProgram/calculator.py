
print("Welcome to the calculator program!")

operator=input("What is the operator ( + - * / ):")
num1=float(input("What is the first number:"))
num2=float(input("What is the second number:"))

if operator == "+":
    answer = num1 + num2
    print(round(answer, 2))
elif operator == "-":
    answer = num1 - num2
    print(round(answer, 2))
elif operator == "*":
    answer = num1 * num2
    print(round(answer, 2))
elif operator == "/":
    answer = num1 / num2
    print(round(answer, 2))
else:
    print(f"{operator} is not a valid operator!")
    