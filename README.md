# basicallybars: a beginner's attempt at a python library

![PyPI - License](https://img.shields.io/pypi/l/basicallybars) ![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/Coder2354/basicallybars?label=last%20release)

<p>This is a small python library. 
Its goal is to make algorithms easier to use, by
displaying visual feedback on the progress of the
algorithm! It's also quite customisable.
Yup, that's literally it. WIP; feel free
to improve my terrible code.</p>

Link to PyPi is [here](https://pypi.org/project/basicallybars/)

## Use

**Import :)**
```
from basicallybars import basicallybars
```

**Create a new loading bar:**

```
bar = basicallybars.progressbar()
```

**Update & set values of that bar:**
```
bar.display(x, y) # Note: "x" is the amount done in this is example while "y" is the full amount of things that have to be done
```

**Different loading indicators**

```
default_bar = basicallybars.progressbar(quantityDisplay="Amount") # Default loading display, shows as "(6/10)"
percent_bar = basicallybars.progressbar(quantityDisplay="Percent") # Creates a bar with a loading display as a percentage like "60%"
remaining_bar = basicallybars.progressbar(quantityDisplay="Remaining") # Creates a bar with a loading display like "4 remaining..."
```
>  Set the quantity_display paramater to anything else and it won't display; only the loading bar (Not really recommended)

**basicallybars in action:**

```
from time import sleep

bar = basicallybars.progressbar()
for x in range(0, 4):
    bar.display(x, 4) # Display a bar that parses through imaginary data, with x being the amount of data finished and y being the total amount (4)
    sleep(1)
    basicallybars.clearTerminal() # Reset the terminal's output to reprint the bar
```

***Note: More features and examples coming soon.***
