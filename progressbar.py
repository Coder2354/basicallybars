import colorama
import os
import math
from sys import platform

def clearTerminal():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")
    else:
        print(f"Current OS ({platform}) can't be identified so unable to clear display.")

def lib_getBar(parsed, fullAmount, colour):
    percent = math.floor(100 * float(parsed)/float(fullAmount))
    output = f"[{colour}"
    i = 0
    for i in range(1, math.floor(percent/10)+1):
        output = f"{output}="
    for x in range(i, 10):
        output = f"{output} "
    return f"{output}{colorama.Style.RESET_ALL}]"

def lib_displayQuantity(mode, parsed, fullAmount):
    if mode == "Amount":
        return(f" ({parsed}/{fullAmount})")
    elif mode == "Percent":
        return(f" {math.floor(100 * float(parsed)/float(fullAmount))}%")
    elif mode == "Remaining":
        return(f" {fullAmount-parsed} remaining...")
    else:
        return("") # reset end="" params

class progressbar:
    def __init__(self, colour=colorama.Fore.WHITE, quantityDisplay="Percent", title=None):
        self.colour = colour
        self.quantityDisplay = quantityDisplay
        self.title = title
    def display(self, parsed, fullAmount):
        if self.title:
            print(f"{self.title}:")

            i = 0
            print(lib_getBar(parsed, fullAmount, self.colour), end="")
            print(lib_displayQuantity(self.quantityDisplay, parsed, fullAmount))