#Program to find electricity bill
units = int(input("Enter the used units: "))
min_bill = 50

if units >= 1 and units <= 100:
    used_bill = units * 3
elif units >= 101 and units <= 500:
    used_bill = units * 4
elif units > 500 :
    used_bill =units * 8
total_bill = used_bill + min_bill
print(f"Min_bill = {min_bill} and units used = {units} \
 total bill = {total_bill}")