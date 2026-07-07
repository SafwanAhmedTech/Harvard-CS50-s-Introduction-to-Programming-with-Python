import sys
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1][-3:] != '.py':
    sys.exit('Not a Python file')

number = 0
try:
    with open(sys.argv[1]) as file:
        for row in file:
            if row.lstrip().startswith('#'):
                continue
            elif row.strip() == '':
                continue
            else:
                number += 1
    print(number)


except FileNotFoundError:
    sys.exit('File does not exist')
