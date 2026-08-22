def fun(p, t, r):
    return (p * t * r) / 100

p, t, r = 8, 6, 8

res = fun(p, t, r)
print(res)



si = lambda p, t, r: (p * t * r) / 100

p, t, r = 8, 6, 8

res = si(p, t, r)
print(res)