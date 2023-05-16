import colorama
import os
from sys import platform

def clearTerminal():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")
    else:
        print(f"Current OS ({platform}) can't be identified so unable to clear display.")

class progressbar:
    def __init__(self, colour=colorama.Fore.WHITE, showQuantity=True, title=None):
        self.colour = colour
        self.showQuantity = showQuantity
        self.title = title
    def display(self, parsed, fullAmount):
        if self.title:
            print(f"{self.title}:")
            print(f"[{self.colour}", end="")

            i = 0
            for i in range(1, divmod(parsed, round(fullAmount/10))[0]+1):
                print("=",end="")
            for x in range(i, 10):
                print(" ",end="")
            print(f"{colorama.Style.RESET_ALL}]", end="")

            if self.showQuantity:
                print(f" ({parsed}/{fullAmount})")
            else:
                print("") # reset end="" params