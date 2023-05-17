import progressbar
import colorama
from time import sleep

for c in range(0, 4):
    for i in range(1, 51):
        upperbar = progressbar.progressbar(colour=colorama.Fore.GREEN, quantityDisplay="Percent", title="Overall", barType="large")
        bar = progressbar.progressbar(colour=colorama.Fore.CYAN, quantityDisplay="Amount", title="Task")
        upperbar.display(c, 4)
        print("")
        bar.display(i, 50)
        sleep(.2)
        progressbar.clearTerminal()
        if c == 4:
            break

print("Finish'd")