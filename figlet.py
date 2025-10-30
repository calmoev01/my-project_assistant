import sys
import random
from pyfiglet import Figlet



figlet = Figlet()
figlet.setFont(font='digital')
text = input("text :")
print(figlet.renderText(text))



