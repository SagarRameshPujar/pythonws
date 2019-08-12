#Program to find the sum of Digits
num = int(input("Enter the number: "))
num1 = num
res = 0
while num1 != 0:
    res += num1 % 10
    num1 //= 10
print(f"The sum of digits of the {num} is {res}")