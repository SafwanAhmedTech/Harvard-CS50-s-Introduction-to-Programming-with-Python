months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input('Date: ')
    if '/' in date:
        try:
            first, second, third = date.split('/')
        except ValueError:
            continue
        else:
            try:
                first = int(first)
                second = int(second)
            except ValueError:
                continue
            if first < 1 or first > 12:
                continue
            if second < 1 or second > 31:
                continue
            break
    else:
        try:
            first, second = date.split(',')
            month, number = first.split(' ')
        except ValueError:
            continue
        try:
            number = int(number)
        except ValueError:
            continue
        if number < 1 or number > 31:
            continue
        if month not in months:
            continue
        break

month = ''
day =  ''
year = ''

if '/' in date:
    month, day, year = date.split('/')
else:
    first, year = date.split(',')
    month, day = first.split(' ')
    month = months.index(month) + 1

month = int(month)
day = int(day)
year = year.strip()

print(f'{year}-{month:02}-{day:02}')


