#Program to find the given number is prime or not

num = int(input("Enter the number: "))
flag = True

if num > 1:
    for i in range(2,num // 2+1):
        if num % i == 0:
            flag = False
            break
else:
    flag = False

if flag:
    print(f"Given number is {num} is prime")
else:
    print(f"Given number is {num} not prime")


        


        
    

