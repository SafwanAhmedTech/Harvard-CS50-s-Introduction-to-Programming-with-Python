def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    new_text = '12'
    if len(s) < 2 or len(s) > 6:
        return False

    for n in range(2):
        if s[n].isalpha() == False:
            return False

    for n in range(len(s)):
        if s[n].isdigit():
            new_text = s[n:len(s) + 1]
            break

    if new_text[0] == '0':
        return False


    for n in range(len(new_text)):
        if new_text[n].isdigit():
            continue
        else:
            return False

    for n in range(len(s)):
        if s[n] == '.' or s[n] == ' ' or s[n].isalnum() == False:
            return False

    return True




main()
