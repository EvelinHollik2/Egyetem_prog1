import sys


def count_of_odds(numbers: list[int]) -> int:
    count = 0
    for number in numbers:
        if number % 2 == 1:
            count += 1
    return count


def main():
    numbers = []
    argc = len(sys.argv)
    for i in range(1, argc):
        numbers.append(int(sys.argv[i]))

    print(count_of_odds(numbers))


if __name__ == '__main__':
    main()
