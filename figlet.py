from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts = figlet.getFonts()
font = ''
if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    f = sys.argv[2]
    if f not in fonts:
        sys.exit('Error')
    if sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit('Error')
figlet.setFont(font=f)
text = input('Input: ')
print(figlet.renderText(text))
