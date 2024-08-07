from pyfiglet import Figlet
from sys import argv ,exit
import random
figlet = Figlet()
if len(argv) == 1:
    i=input("Hello:")
    r=random.choice(figlet.getFonts())
    figlet.setFont(font=r)
    print(figlet.renderText(i))
elif argv[1] =="-f" and argv[2] in figlet.getFonts():
    i=input("Hello:")
    figlet.setFont(font=argv[2])
    print(figlet.renderText(i))
else:
    exit("Enter correctly")


