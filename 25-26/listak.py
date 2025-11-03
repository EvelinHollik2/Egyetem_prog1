#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for i in range(len(a)):
#    print(a[i])


#lista át adás:
#b = [2,5,6]
#c = b
#b[0] = 10
#print(b, c)

#teljes másolat:
#d=[2,5,4]
#d.append(3)
#d.pop()
#e=d.pop(1)
#print(d)

#a=[1,2,3,4]
#a[1:3] = [6,7]
#
#print(a)

#sorted : fordított sorrendbe pakolja a listát
#sorted(a, reversed =True)

#.sort : sorrendbe pakolás
#a = ['g','s','a','b','c','d']
#a.sort()
#print(a)

#listába beszúrás
#a = [1,2,3,4]
#a.insert(1, "alma")
#print(a)

#listaértelmezés (zh-s)
#lista = [kifejezés for elem in lista if feltétel == True]
#s= "alma"
#li=[c for c in s]
#print(li)

#szám lista generálás
#li =[i for i in range(10)]
#print(li)

#csak a páros számok kiiratása
#li = [i for i in range(10) if i%2 ==0]
#print(li)

#van e a szóban "a" betű
#gyumolcs =["alma", "banán", "körte"]
#uj = [x for x in gyumolcs if 'a' in x]
#print(uj)

#1.feladat:
#li = ["aladar", "bela", "cecil"]
#uj = [nev.capitalize() for nev in li]
##uj = [nev[0].upper() +nev[1:] for nev in li]
#print(uj)

#2.feladat:
#li2 = [0 for i in range(10)]
#print(li2)

#3.feladat:
#li3 = [i for i in range(1, 11)]
#uj2 = [i*2 for i in li3]
#print(uj2)

#4.feladat:
#li = [str(i) for i in range(1, 11)]
#uj = (int(i) for i in li)
#print(uj)

#5. feladat:
#s = "1234567"
#li2=(int(i) for i in s)
#print(li2)

#6.feladat:
#s= "the quick brown fox jumps over the lazy dog"
#uj = [len(word) for word in s.split(" ")]
#print(uj)

#7.feladat:
#s= "the quick brown fox jumps over the lazy dog"
#uj = [word[0] for word in s.split(" ")]
#print(uj)


#töltsetek fel egy listát n darab 1 és 10 közötti véletlenszám generátorral előállított páros számmal
import random

#n = int(input("Hány számot generáljunk? "))
#li = [random.randint(1, 10) for i in range(n*2) if random.randint(1, 10) % 2 == 0][:n]

#print(li)

n = int(input("n="))
li = []
while True:
    if len(li) == n:
        break
    x = random.randint(1,10)
    if x%2 ==0:
        li.append(x)

print(li)