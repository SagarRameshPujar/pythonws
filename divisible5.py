#Program to find the numbeers which is divisible by 5 in the given range

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
c_div = 0
n_div = 0

for num in range(lower_bound,upper_bound + 1):
    if num % 5 == 0:
        c_div += 1
    else:
        n_div += 1
print(f"in range {lower_bound} and {upper_bound} divisibles of 5 is {c_div}")



 

