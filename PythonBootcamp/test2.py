year = 2028

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")



string = "hello, world"
char = "w"
if char in string:
        print("The string contains the character", char)
else:
        print("The string does not contain the character", char)