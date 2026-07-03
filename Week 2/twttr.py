text = input('Input: ')
new_text = ''
for n in range(len(text)):
    temp = text[n].lower()
    if temp == 'a' or temp == 'e' or temp == 'i' or temp == 'o' or temp =='u':
        continue
    else:
        new_text = new_text + text[n]

print(new_text)
