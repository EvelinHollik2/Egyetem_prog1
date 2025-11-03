a = 5
b = 7
# felcserélés

a, b = b, a
print("az 'a' értéke = ", a)
print("a 'b' értéke = ", b)

a = a+b
b = a-b
a = a-b
print("az 'a' értéke (másodjára) = ", a)
print("a 'b' értéke (másodjára)= ", b)

tmp = a
a = b # a=7
b = tmp
print("A értéke: " +str(a) + ", B értéke: " +str(b))

