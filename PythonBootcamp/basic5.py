p = int(input("Principal amount: "))
r = int(input("Rate of interest: "))
t = int(input("Time in years: "))


Amt = p * (pow((1 + r / 100), t))
CI = Amt - p

print("Compound interest:", CI)