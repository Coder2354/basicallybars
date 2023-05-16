import progressbar
import colorama
from time import sleep

for c in range(0, 3):
    for i in range(1, 51):
        upperbar = progressbar.progressbar(colour=colorama.Fore.GREEN, quantityDisplay="Percent", title="Overall")
        bar = progressbar.progressbar(colour=colorama.Fore.YELLOW, quantityDisplay="Amount", title="Test bar")
        upperbar.display(c, 2)
        bar.display(i, 50)
        sleep(.2)
        progressbar.clearTerminal()
        if c == 2:
            break