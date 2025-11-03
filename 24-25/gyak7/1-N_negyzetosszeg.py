#i negyzet,és i = 1
#def szum(n: int) -> int:
#if n == 1:
#return 1
#else:
#return (n * n) - 2 + szum(n - 1)


# i negyzet - 2, és i = 1
#def szum(n: int) -> int:
#   if n == 1:
#        return 1
#   else:
#        return (n * n) - 2 + szum(n - 1)


#i negyzet - 2, és i = 3
#def szum(n: int) -> int:
#   if n == 4:
#        return 4*((4*4)-1)
#   else:
#        return n * (n * n) - 1 + szum(n - 1)


# i köb - 5, és i =2
#def szum(n: int) -> int:
#   if n == 2:
#        return 2*2*2-5
#   else:
#        return (n * n * n) - 5 + szum(n - 1)


#ha n = 0, n = 1, n >= 2
def szum(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return szum(n - 1) + szum(n - 2)


def main():
    print(szum(5))


if __name__ == '__main__':
    main()
