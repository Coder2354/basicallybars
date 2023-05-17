import basicbar
from colorama import Fore
from time import sleep

bar = basicbar.progressbar(color=Fore.CYAN, quantityDisplay="Amount", title="Example bar") # creates a new bar
basicbar.progressbar()
for i in range(1, 11):
    basicbar.clearTerminal() # reset the terminal to update the bar
    bar.display(i, 10) # display the number i out of 10
    sleep(1) # wait a second (simulate an algoritm's delay)
    if i == 11:break
print("\nDone!")