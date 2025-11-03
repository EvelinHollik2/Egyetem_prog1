import sys


def count_of_odds() -> int:
    count = 0
    for number in sys.argv[1:]:  #[1:] elsőtől a végéig, a 0 nincs benne
        if int(number) % 2 == 1:
            count += 1
        return count


def main():
    print(count_of_odds())


if __name__ == '__main__':
    main()
