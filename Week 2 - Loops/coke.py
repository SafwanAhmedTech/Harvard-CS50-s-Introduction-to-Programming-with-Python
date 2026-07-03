amount_due = 50
while True:
    print(f'Amount due: {amount_due}')
    coin = int(input('Insert coin: '))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due -= coin
    if amount_due <= 0:
        temp = amount_due * -1
        print(f'Change owed: {temp}')
        break

