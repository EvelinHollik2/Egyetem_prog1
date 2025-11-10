#faktorális számítás
def fakt(n:int)->int:
    if n == 1:
        return 1
    else:
        return n*fakt(n-1)

def main():
    print(fakt(1))
    print(fakt(5))
    print(fakt(10))

if __name__ == "__main__":
    main()