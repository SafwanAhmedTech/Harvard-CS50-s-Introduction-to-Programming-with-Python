import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

if sys.argv[1][-4:].lower() != '.jpg' and sys.argv[1][-4:].lower() != '.png' and sys.argv[1][-5:].lower() != '.jpeg':
    sys.exit('Invalid Input')
if sys.argv[2][-4:].lower() != '.jpg' and sys.argv[2][-4:].lower() != '.png' and sys.argv[2][-5:].lower() != '.jpeg':
    sys.exit('Invalid Output')

if sys.argv[1][-4:].lower() == '.jpeg':
    if sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
        sys.exit('Input and output have different extensions')
elif sys.argv[1][-3:].lower() != sys.argv[2][-3:].lower():
    sys.exit('Input and output have different extensions')

try:
    with Image.open(sys.argv[1]) as photo:
        with Image.open("shirt.png") as shirt:
            photo = ImageOps.fit(photo, shirt.size)
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])

except FileNotFoundError:
    sys.exit('Input does not exist')
