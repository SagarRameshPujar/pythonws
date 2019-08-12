#Program to find the Fibonacci Series
num = int(input("Enter the number: "))
a , b = 0 , 1
print(a,end = " ")
print(b,end = " ")

for i in range(2,num):
    c = a + b
    print(c,end = " ")
    a , b = b , c

    

