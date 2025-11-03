import random

s1 = set()
s2 = set()

n = int(input("n = "))
m = int(input("m = "))

while len(s1) < n: # -> s1 hossza kisebb mint n
    s1.add(random.randint(1,10))

while len(s2) < m:
    s2.add(random.randint(1,10))

print(s1)
print(s2)

print("Unio = ", s1.union(s2))
print("Metszet = ", s1.intersection(s2))
print("Különbség = ", s1.difference(s2))
print("szimetrikus különbség = ", s1.symmetric_difference(s2))