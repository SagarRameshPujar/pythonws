#Program to find the given number is Palindrome or not
num = int(input("Enter the number: "))
num1 = num
rev = 0
while num != 0:
    rev = rev * 10 + num % 10
    num = num // 10
if rev == num1:
    print(f"Given number {num1} is palindrome ")
else:
    print(f"Given number {num1} is not palindrome ")
    