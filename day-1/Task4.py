number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
print("1. Addtion\n2. Subtraction\n3. Multiplication\n4. Division")
choice = int(input("Enter Choice : "))
if ( choice == 1):
    print("The Addition Of", number1, "+" , number2, "Is:", number1 + number2)
elif (choice == 2):
    print("The Subtraction Of", number1, "-" , number2, "Is:", number1 - number2)
elif (choice == 3):
    print("The Multiplication Of", number1, "*" , number2, "Is:", number1 * number2)
elif (choice == 4):
    print("The Division Of", number1, "/" , number2, "Is:", number1 / number2)
else:
    print("Invalid Input")
