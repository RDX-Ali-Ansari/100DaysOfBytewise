number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))

print("The Numbers Are\n", number1, number2, number3)

if (number1 > number2 and number1 > number3):
    print("Greatest Number Is:", number1)
elif (number2 > number1 and number2 > number3):
    print("Greatest Number Is:", number2)
else:
    print("Greatest Number Is:", number3)
