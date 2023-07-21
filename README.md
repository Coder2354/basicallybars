# basicbar

<p>This is a small python library. (My first one!)
Its goal is to make algorithms easier to use, by
displaying visual feedback on the progress of the
algorithm! It is quite customisable and uses the
colorama library to add colours. WIP; feel free
to improve my terrible code.</p>
[Publishing to PyPI soon; stay tuned.]

## Use

**Create a new loading bar:**

```
bar = basicbar.progressbar()
```

**Update & set values of that bar:**
```
bar.display(x, y) # Note: "x" is the amount done in this is example while "y" is the full amount of things that have to be done
```

**Colo(u)rs:**

```
from colorama import Fore # Colorama is the used color library and is bundled with basicbar.
bar = basicbar.progressbar(color=fore.CYAN) # Create a progress bar with the loading color being cyan.
```

**Different loading indicators**

```
default_bar = basicbar.progressbar(quantityDisplay="Amount") # Default loading display, shows as "(6/10)"
percent_bar = basicbar.progressbar(quantityDisplay="Percent") # Creates a bar with a loading display as a percentage like "60%"
remaining_bar = basicbar.progressbar(quantityDisplay="Remaining") # Creates a bar with a loading display like "4 remaining..."
```
>  Set the quantity_display paramater to anything else and it won't display; only the loading bar (Not really recommended)

**Basicbar in action:**

```
from time import sleep

bar = basicbar.progressbar()
for x in range(0, 4):
    bar.display(x, 4) # Display a bar that parses through imaginary data, with x being the amount of data finished and y being the total amount (4)
    sleep(1)
    basicbar.clearTerminal() # Reset the terminal's output to reprint the bar
```

***Note: More features and examples coming soon.***
