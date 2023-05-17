# basicbar

<p>This is a small python library. (My first one!)
Its goal is to make algorithms easier to use, by
displaying visual feedback on the progress of the
algorithm! It is quite customisable and uses the
colorama library to add colours. WIP; feel free
to improve my terrible code.</p>
[Publishing to PyPI soon; stay tuned.]

# Use

**Create a new loading bar:**

> bar = basicbar.progressbar()

**Update & set values of that bar:**

> bar.display(x, y) # Note: "x" is the amount done in this is example while "y" is the full amount of things that have to be done

**Colo(u)rs:**

> from colorama import Fore # Colorama is a useful color library and is bundled with basicbar.<br>
> bar = basicbar.progressbar(color=fore.CYAN) # Create a progress bar with the loading color being cyan.

**Different loading indicators**

> - bar = basicbar.progressbar(quantityDisplay="Amount") # Default loading display, shows as "(6/10)"
> - bar = basicbar.progressbar(quantityDisplay="Percent") # Creates a bar with a loading display as a percentage like "60%"
> - bar = basicbar.progressbar(quantityDisplay="Remaining") # Creates a bar with a loading display like "4 remaining..."
> - Set the quantityDisplay paramater to anything else and it won't display; only the loading bar (Not really recomended)

**Create a loading effect:**

> from time import sleep<br>
> bar = basicbar.progressbar()<br>
> for x in range(0, 4):<br>
> &nbsp;&nbsp;&nbsp;&nbsp;bar.display(x, 4) # Display a bar that parses through imaginary data, with x being the amount of data finished and y being the total amount (4)<br>
> &nbsp;&nbsp;&nbsp;&nbsp;sleep(1)<br>
> &nbsp;&nbsp;&nbsp;&nbsp;basicbar.clearTerminal() # Reset the terminal's output to reprint the bar

**Create a larger bar:**
> bar = basicbar.progressbar(barType="large")

***Note: More features and examples coming soon.***
