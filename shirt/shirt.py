from sys import argv
from PIL import Image
import PIL
import sys

try:
    table=[]
    if len(argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if argv[1][-4:] != ".jpg" and argv[1][-5:] != ".jpeg" and argv[1][-4:] != ".png":
            sys.exit("Invalid input")
        elif argv[2][-4:] != ".jpg" and argv[2][-5:] != ".jpeg" and argv[2][-4:] != ".png":
            sys.exit("Invalid output")
        elif argv[1][-4:] != argv[2][-4:]:
            sys.exit("Input and output have different extensions")
        else:
            im1=Image.open(rf"{argv[1]}")
            im2=Image.open(r"shirt.png")
            size = im2.size
            im1=PIL.ImageOps.fit(im1,size)
            im1.paste(im2,box = (0, 0), mask = im2)
            im1.save(argv[2])

except FileNotFoundError:
    sys.exit(f"Could not read {argv[1]}")
except IndexError:
    pass
