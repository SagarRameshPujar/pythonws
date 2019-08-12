#Program to find the prime numbers in the given range

lb = int(input("Enter the lower bound: "))
ub = int(input("Enter the upper bound: "))

for num in range(lb,ub + 1):
    is_prime = True
    if num > 1:
        for i in range(2,num // 2 + 1):
            if num % i == 0:
                is_prime = False
                break

    else:
        is_prime = False

    if is_prime:
        print(num, end = " ")    


    