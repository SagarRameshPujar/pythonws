# Program to print the multiplication of the table

num1 = int(input("Enter the number1 :"))
num2 = int(input("Enter the number2 :"))
num3 = int(input("Enter the number3 :"))

if num1 > num2 and num1 > num3:
    big = num1
elif num2 > num3:
    big = num2
else:
    big = num3
    
print (f"{big} is biggest of {num1},{num2} and {num3}")
