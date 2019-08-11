#Program to find the grade
score = int(input("Enter the secured score: "))

if score >= 91 and score <= 100:
    print("A")
elif score >= 61 and score <= 90:
    print("B")
elif score >= 51 and score <= 60:
    print("C")
else:
    print("D")
    