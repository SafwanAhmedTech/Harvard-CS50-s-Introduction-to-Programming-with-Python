import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$', s):
        f_first = match.group(1)
        f_last = match.group(2)
        f_time = match.group(3)
        s_first = match.group(4)
        s_last = match.group(5)
        s_time = match.group(6)
        f_new = int(f_first)
        if f_time == "AM":
            if f_new == 12:
                f_new = 0
        else:  # PM
            if f_new != 12:
                f_new += 12

        s_new = int(s_first)
        if s_time == "AM":
            if s_new == 12:
                s_new = 0
        else:  # PM
            if s_new != 12:
                s_new += 12
        if f_last == None:
            f_last = '00'
        if s_last == None:
            s_last = '00'
        return f"{f_new:02}" + ':' + f_last + ' to ' + f"{s_new:02}" + ':' + s_last

    else:
        raise ValueError



if __name__ == "__main__":
    main()

#do this all again and use regex man

