#Program to illustrate Patterns

num = int(input("Enter the number: "))

for i in range(1,num + 1):
    print("* " * i) 

print("-" * 100)
for i in range(num,0, -1):
    print("* " * i)

print("-" * 100)
for i in range(1,num + 1):
    for j in range(1,i + 1):
        print(j, end = " ")
    print()

print("-" * 100)
for i in range(num,0,- 1):
    for j in range(1,i+1):
        print(j, end = " ")
    print()

print("-" * 100)
for i in range(1,num + 1):
    for j in range(1,num-i + 1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end = "")
    for l in range(k-1,0,-1):
        print(l,end="")
    print()


print("-" * 100)
n = 64
for i in range(1,num + 1):
    for j in range(1,num-i + 1):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(n+k),end = "")
    for l in range(k-1,0,-1):
        print(chr(n+l),end="")
    print()


