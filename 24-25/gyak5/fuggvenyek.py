gyumolcs = ["alma", "körte", "banán", "mangó", "körte"]
uj = []
for x in gyumolcs:
    if 'a' in x:
        uj.append(x)
print(uj)

uj2 = [x for x in gyumolcs if 'a' in x]
print(uj2)

l1 = ["aladar",  "bela", "cecil"]
l2 = [x[0].upper() + x[1:] for x in l1]
print(l2)

l3 = [1,2,3,4,5,6,7,8,9,10]
l4 = [x*2 for x in l3]
print(l4)

l5 = ["1","2","3","4","5"]
l6 = [int(x) for x in l5]
print(l6)

l7 = ["1234567"]
l8 = [int(a) for i in l7 for a in i]
print(l8)

l9 = ["The quick brown fox jumps over the lazy dog"]
l10 = [len(a) a.split() for a in l9 ]
print(l10)
for a in l9:
    print(a)