# Program to check given number is prime or not

num = int(input("Enter the number to check prime :"))

is_prime = True

if num > 1:
    for i in range(2, num// 2 + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"Given number :{num} is prime")
else:
    print(f"Given number :{num} is not a prime")