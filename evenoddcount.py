#Program to check wheather given number is Amstrong number or not
num = int(input("Enter the number: "))
temp = num
ec = 0
oc = 0
pc = 0
elist = []
olist = []
plist = []
def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
    return True

while temp != 0:
    rem = temp % 10
    if is_prime(rem):
        pc += 1
        plist.append(rem)
    if is_even(rem):
        ec += 1
        elist.append(rem)
    else:
        oc += 1
        olist.append(rem)
    temp = temp // 10
print(f"Total even digits is {ec}, odd digits is {oc} and prime digits:{pc} in {num}")
print(f"Prime digits: {plist}")
print(f"Odd digits: {olist}")
print(f"Even digits: {elist}")