n = 153
t = n
p = len(str(n))
s = 0

while t > 0:
    d = t % 10
    s += d ** p
    t //= 10

if s == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

    n = 153
    p = len(str(n))




    def arm(x):
        if x == 0:
            return 0
        return (x % 10) ** p + arm(x // 10)


    if arm(n) == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")