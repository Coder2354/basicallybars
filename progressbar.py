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

def lib_getBar(parsed, fullAmount, color, quantityDisplay, type="default"):
    percent = math.floor(100 * float(parsed)/float(fullAmount))
    if type == "large":
        output = f"|----------|\n|{color}"
    else:
        output = f"[{color}"
    i = 0
    for i in range(1, math.floor(percent/10)+1):
        output = f"{output}="
    for x in range(i, 10):
        output = f"{output} "
    
    if type == "large":
        return f"{output}{colorama.Style.RESET_ALL}| {lib_displayQuantity(quantityDisplay, parsed, fullAmount)}\n|----------|"
    else:
        return f"{output}{colorama.Style.RESET_ALL}] {lib_displayQuantity(quantityDisplay, parsed, fullAmount)}"

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
    def __init__(self, color=colorama.Fore.WHITE, quantityDisplay="Amount", title="New bar", barType="default"):
        self.color = color
        self.quantityDisplay = quantityDisplay
        self.title = title
        self.barType = barType
    def display(self, parsed, fullAmount):
        if self.title:
            print(f"{self.title}:")
        i = 0
        print(lib_getBar(parsed, fullAmount, self.color, self.quantityDisplay, type=self.barType), end="")