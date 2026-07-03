text = input('Enter: ')
new_text = ''
for i in range(len(text)):
    if text[i].isupper():
        new_text = new_text + '_' + text[i].lower()
    else:
        new_text = new_text + text[i]
print(new_text)
