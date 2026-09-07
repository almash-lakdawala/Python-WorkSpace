from collections import Counter

d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}

vals = [x for v in d.values() for x in v]
freq = Counter(vals)
res = sorted(list(freq.keys()))
print(res)