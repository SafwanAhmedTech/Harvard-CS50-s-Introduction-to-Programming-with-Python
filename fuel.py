while True:
    try:
        fraction = input('Enter fraction: ')
        top, bottom = fraction.split('/')
        top = int(top)
        bottom = int(bottom)
        if top < 0:
            continue
        elif bottom < 1:
            continue
        elif top > bottom:
            continue
        else:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

fraction = top / bottom * 100
fraction = round(fraction)

if fraction <= 1:
    print('E')
elif fraction >= 99:
    print('F')
else:
    print(f'{fraction}%')
