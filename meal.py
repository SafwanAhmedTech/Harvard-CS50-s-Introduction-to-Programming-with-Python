
def main():
    time = input('Time: ')
    time = convert(time)
    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')


def convert(time):
    first, second = time.split(':')
    second = float(second)
    second = second / 60
    first = float(first)
    first += second
    return first


if __name__ == "__main__":
    main()
