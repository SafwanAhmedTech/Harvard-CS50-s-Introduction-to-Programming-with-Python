import csv
import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        with open(sys.argv[2], 'w', newline='') as file:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                second, first = row['name'].split(',')
                second = second.strip()
                first = first.strip()
                writer.writerow({'first' : first, 'last' : second, 'house' : row['house']})


except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')




