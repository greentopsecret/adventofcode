if __name__ == '__main__':
    f = open('data/day1a.txt', 'r')
    input = f.read()
    cnt = 0
    prev = None
    for number in input.split(sep="\n"):
        if not number.isnumeric():
            break

        number = int(number)
        if prev and prev < number:
            cnt += 1
        prev = number

    f.close()
    print(cnt)
