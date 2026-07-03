def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    new = d[1:]
    new = float(new)
    return new


def percent_to_float(p):
    # TODO
    new = p[:-1]
    new = float(new)
    new = new / 100
    return new


main()
