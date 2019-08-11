#Program to find the numbers which is even increase by 1 and odd is increase by 2

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))


for num in range(lower_bound,upper_bound + 1):
    if num % 2 == 0:
        num += 1
    else:
        num += 2
    print(num,end =  " ")