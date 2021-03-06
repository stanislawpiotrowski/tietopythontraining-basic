def collatz(number):
    tmp = number % 2
    if tmp:
        tmp = 3 * number + 1
    else:
        tmp = number // 2
    print(tmp)
    return tmp


def main():
    print("Provide input")
    number = int(input())
    while number != 1:
        number = collatz(number)


if __name__ == '__main__':
    main()
