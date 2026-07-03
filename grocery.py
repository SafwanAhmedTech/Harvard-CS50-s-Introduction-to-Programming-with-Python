list = {}

while True:
    try:
        item = input()
        item = item.upper()
    except EOFError:
        break
    else:
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

list = sorted(list.items())

for key, value in list:
    print(value, key)
