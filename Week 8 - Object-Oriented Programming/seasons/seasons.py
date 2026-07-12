from datetime import date
import inflect
import sys


def main():
    dob = input("Date of Birth: ")
    print(minutes(dob))


def minutes(dob):
    try:
        dob = date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    difference = today - dob
    days = difference.days
    minutes = days * 1440

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")

    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
