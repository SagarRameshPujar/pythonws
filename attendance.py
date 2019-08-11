#Program to find attendance and score
attendance = int(input("Enter the attendence: "))
score = int(input("Enter the score: "))
grace = 0

if attendance > 90:
    if score >= 70 and score <= 90:
        grace = 5
    elif score >= 91 and score <= 95:
        grace = 2
score = score + grace
print(f"Attendance = {attendance} and Score = {score} and Grace = {grace}")


         
