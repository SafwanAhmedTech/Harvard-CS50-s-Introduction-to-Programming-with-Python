def main():
    fraction = input('Enter fraction: ')
    percent = convert(fraction)
    print(gauge(percent))


def convert(fraction):
    try:
        top, bottom = fraction.split('/')
        top = int(top)
        bottom = int(bottom)
        if top < 0:
            raise ValueError
        elif bottom < 1:
            raise ValueError
        elif top > bottom:
            raise ValueError
        if bottom == 0:
            raise ZeroDivisionError
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

    fraction = top / bottom * 100
    percent = round(fraction)
    return percent

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
