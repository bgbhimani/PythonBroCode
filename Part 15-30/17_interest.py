p = 0
r = 0
n = 0

while True:
    p = float(input("Enter The Principle: "))
    if p <= 0 :
        print("Principle Must Be > 0")
    else:
        break

while r <=0:
    r = float(input("Enter The Rate: "))
    if r <= 0 :
        print("Rate of interest Must Be > 0.")

while n <=0:
    n = float(input("Enter The time in months: "))
    if n <= 0 :
        print("time period Must Be > 0.")

i = p*r*n/100
total = p* pow((1+r/100),n)
print(f"Simple Interest is: {i}₹")
print(f"Total Principle is: {p}₹")

print(f"total amount to pay is: {i+p}₹")
print(f"total amount to pay is: {total}₹")