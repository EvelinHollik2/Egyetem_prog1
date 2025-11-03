n = int(input("n= "))
for i in range(4, n + 1, 4):
    print(i, end=" ")

m = int(input("m= "))
for i in range(4, m + 1):
    if(i % 4 ==0):
        print(i, end=" ")