import progressbar
import colorama
from time import sleep

for i in range(1, 101):
    bar = progressbar.progressbar(colour=colorama.Fore.YELLOW, showQuantity=True, title="Test bar")
    bar.display(i, 100)
    sleep(.2)
    progressbar.clearTerminal()