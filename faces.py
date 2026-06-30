def main():
    text = input('Enter: ')
    print(convert(text))

def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁' )

main()
