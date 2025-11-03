import sys


def lnko(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main():
    with open(sys.argv[1]) as file:
        for line in file:
            numbers = line.strip("\n").split(" ")
            lnk = int(numbers[0])
            for i in range(1, len(numbers)):
                lnk = lnko(lnk, int(numbers[i]))
            print(lnk)


if __name__ == '__main__':
    main()
