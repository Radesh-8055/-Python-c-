num1 = float(input("enter first number: "))
num2 = float(input("enter the second number: "))

print("choose opearation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice= input("enter operator (+, -, *, /): ")

if choice == "+":
    print("result:",num1 + num2)

elif choice == "-":
    print("result:",num1 - num2)

elif choice == "*":
    print("result:",num1 * num2)

elif choice == "/":
    if num2 != 0:
        print("result:",num1 / num2)
    else:
        print("division by zero error")
else:
    print("invalid operator")

