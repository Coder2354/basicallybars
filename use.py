import progressbar
import colorama
from time import sleep

bar = progressbar.progressbar(color=colorama.Fore.CYAN, quantityDisplay="Amount", title="Example bar") # creates a new bar
for i in range(1, 11):
    progressbar.clearTerminal() # reset the terminal to update the bar
    bar.display(i, 10) # display the number i out of 10
    sleep(1) # wait a second (simulate an algoritm's delay)
    if i == 11:break
print("\nDone!")