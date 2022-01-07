<!--
// cSpell:ignore randint fullscreen relx mainloop timedelta Pygame Filedialog
-->

[previous](section_14_16_dates_images_csv.md)\
[main](../README.md)

## Section 17: Errors and Exceptions Handling

<details>
<summary>
Exceptions and Errors.
</summary>

Runtime exceptions (errors), which can break the code:

lets start the python shell
we have an exception and the handler. like ZeroDivisionError or NameError

```py
print(7/0)
Print("upper case!")
print "syntax error"
number int("abc"))
```

| code                     | exception         | handler                                  |
| ------------------------ | ----------------- | ---------------------------------------- |
| `7/0`                    | ZeroDivisionError | _division by zero_                       |
| `Print("Uppercase!)`     | NameError         | _name 'Print' is not defined_            |
| `print "no parentheses"` | SyntaxError       | _missing parentheses in call to 'print'_ |
| `int("abc")`             | ValueError        | _invalid literal for int with base 10_   |

### Handling Exceptions

we can handle exception inside our code, usually python handles exception by exiting the program. we can decide the behavior with **try-except-finally** blocks. the _try_ block has the code than can raise an exception, the _except_ blocks handles the errors. _finally_ executes after either the try or the except block executes. the _else_ block executes only if there was no exception thrown.

### Implementing basic exception handling

let's start with a simple example.

```py
try:
    print (x)
except:
    print("variable not defined")
else:
    print("hello")
finally:
    print("finished")
```

another example, this time when we except a specified kind of exception and we create a block for it.

```py
b = "hello"
try:
    print(int(b))
except ValueError as e:
    print("value error!",e)
except:
    print("other exception!")
else:
    print("no error!")
finally:
    print("finished")

```

</details>

## Section 18: Creating Basic Python Projects

<details>
<summary>
Basic Python example projects
</summary>

### Number Guessing Game

- the computer generates a number, and the user needs to guess which it is. the program will tell the user if the number is larger or smaller than the target number.

in this simple example we won't handle exceptions

```py
import random

guesses =[]

targetNumber= random.randint(1,101)
playerGuess=int(input("guess a number between 1 and 100: "))
guesses.append(playerGuess)

while playerGuess != targetNumber:
    if playerGuess> targetNumber:
        print("too high!")
    else:
        print("too low!")
    playerGuess=int(input("guess a number between 1 and 100: "))
    guesses.append(playerGuess)

else:
    #this happens when the while block is false
    print("your guess was correct!")
    print("it took you %i guesses! these are your guesses" % len(guesses) )
    print(guesses)
```

### Random Number Generator

generating random numbers (with repetitions)

```py
import random

for i in range(1,27):
    print(random.randint(1,27))


```

### Lottery Number Simulator

a really bad way to do this.

```py
import random

lottery_numbers=[]
for i in range(0,6):
    number = random.randint(1,50)
    while number in lottery_numbers:
        number = random.randint(1,50)

    lottery_numbers.append(number)

lottery_numbers.sort()
print(lottery_numbers)

```

### Creating a Digital Clock

we use the **tkinter** for UI.it has a root with many widgets

```py
import datetime
import time
from tkinter import *
from tkinter import ttk
from tkinter import font

def quit(*args):
    root.destroy() #exit main loop

def clock_time():
    time=datetime.datetime.now()
    time =(time.strftime("%H:%M:%S"))
    txt.set(time)
    root.after(1000, clock_time)

root = Tk()
root.attributes("-fullscreen",False)
root.configure(background="black")
root.bind("x",quit)
root.after(1000, clock_time)

fnt= font.Font(family='Helvetica', size=120, weight='bold')
txt=StringVar()
lbl = ttk.Label(root, textVariable=txt,font=fnt,foreground='white', background='black')
lbl.place(relx=0.5,rely=0.5, anchor=CENTER)

root.mainloop()
```

### Creating a Countdown Timer

we will create another example, this time a count-down app.

```py
from tkinter import *
from tkinter import ttk
from tkinter import font

import datetime
import time

global endTime
endTime = datetime.datetime(2023,1,1,0,0)

def quit(*args):
    root.destroy() #exit main loop

def cant_wait():
    timeLeft= endTime - datetime.datetime.now()
    timeLeft=  timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
    txt.set(timeLeft)
    root.after(1000, cant_wait)

root = Tk()
root.attributes("-fullscreen",False)
root.configure(background="black")
root.bind("x",quit)
root.after(1000, cant_wait)

fnt= font.Font(family='Helvetica', size=90, weight='bold')
txt=StringVar()
lbl = ttk.Label(root, textVariable=txt,font=fnt,foreground='white', background='black')
lbl.place(relx=0.5,rely=0.5, anchor=CENTER)

root.mainloop()

```

</details>

## Section 19: Building Desktop GUI Apps

<details>
<summary>
Some project using Tkinter again
</summary>

### What is tkinter

tkinter allows us to create GUI applications, it's a cross platform and works with the Tk GUI toolkit (also available it most OS).
we check to see if it's installed from the shell, if we run this command, we will see a basic gui application.

```sh
python -m tkinter
```

### Building a Calculator

we will now start a project to build a calculator. we use the _frame_ objects as the base class.

Entry is a single line widget. we create buttons for the numbers, the mathematical operations and for some other stuff. we have a task (like a future). we have some functions in the class.

the driver code creates a Tk objects,

```py
calculator=Tk()
calculator.title("Calculator")
app = CalculatorApplication(calculator)
calculator.resizable(width=False,height=False)
calculator.mainloop()
```

### Building an MP3 Player

for the next project we will use the **Pygame** module, with the **Tkinter** module and the **filedialog** object.

we first install pygame, we should do this within our virtual environment.

```sh
pip install pygame
```

we also make use of the _geometry_ method for tkinter objects to set the size of the application.

### Building a Loan Calculator

another tkinter projects, once again with a class.

- Label Widget
- input objects
- the sticky argument has four possible values: N/S/E/W - _north, south, east,west_. it determines where the label appears inside the frame.
- Entry widget to get user input
- StringVar allows us to have a text that changes over time
- Action Buttons - compute and clear
</details>

[next](section_20_22_web_scraping_django.md)
