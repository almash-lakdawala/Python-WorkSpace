num = 6

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print(f"factorial of {num} is {fact}")

# Using Recursive Function

def fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return 1 if n <= 1 else n * fact(n-1)

print(fact(5))
print(fact(-3))