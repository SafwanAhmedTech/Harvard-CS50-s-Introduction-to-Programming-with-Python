import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        list = ip.split('.')
        if len(list) != 4:
            raise ValueError
        for thing in list:
            if thing[0] == '0':
                if thing == '0':
                    continue
                else:
                    raise ValueError
            thing = int(thing)
            if thing >= 0 and thing <= 255:
                continue
            else:
                raise ValueError
        return True
    except ValueError:
        return False




...


if __name__ == "__main__":
    main()
