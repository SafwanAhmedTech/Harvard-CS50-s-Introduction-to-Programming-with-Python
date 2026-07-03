equation = input('Enter arithmetic expression: ')
x, y, z = equation.split(' ')
x = float(x)
z = float(z)
answer = 0
if y == '+':
    answer = x + z
if y == '-':
    answer = x - z
if y == '*':
    answer = x * z
if y == '/':
    answer = x / z

answer = float(answer)
answer = round(answer, 1)
print(answer)


