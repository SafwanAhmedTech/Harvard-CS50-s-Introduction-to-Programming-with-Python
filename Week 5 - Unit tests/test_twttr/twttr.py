def main():
    word = input('Enter: ')
    print(shorten(word))


def shorten(word):
    new_word = ''
    for letter in word:
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            continue
        else:
            new_word = new_word + letter

    return new_word



if __name__ == "__main__":
    main()
