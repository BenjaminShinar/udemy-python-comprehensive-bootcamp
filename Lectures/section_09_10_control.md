<!--
// cSpell:ignore
-->

[main](../README.md)

## Section 09: Python Control Flow Statements

<details>
<summary>
Control flow
</summary>

Changing the order of how the code runs, using conditions and repeating code.

### Conditional Statements

the _if statement_, with _else_ block, and the _elif_ (else if) block. we need to make sure we don't forget the colon (**:**) and that we indent properly.

```py
if condition:
    print(stuff)
```

we can also do a _if-else_ statement in a single line

```py
x = 7 if (10 < 5) else 10
print(x)
```

we can have if-elif-else blocks. there is no practical limit to the number of elif blocks.

```py
if condition1:
    print("condition1 is true")
elif condition2:
    print("condition1 is false, condition2 is true")
else:
    print("else block")
```

### Loops

loops perform actions again and again, either for a set amount of times, for a set amount of elements or until a condition is no longer met.

while loops continue running as long as a condition is true. we need to be careful of infinite loops.

```py
while(condition):
    #code inside while loop
    condition = false #now condition is false.
```

a for loop iterates over a sequence. the sequence can be a range or some iterable container like a list. we can use _break_ and _continue_ statements inside the loop to escape the loop or to skip to the next iteration without executing the rest of the code block.

```py
for fruit in ["grapes","berries","APPLES","oranges"]:
    print(fruit)
    if fruit.isupper():
        break # break from loop
```

we can have loops inside loops. the _continue_ and _break_ statements effect the loop they are part of.

```py
for x in [5,6,7]:
    for y in [10,11,12]:
        if y % x ==0:
            continue # go to next iteration
        print(x,y)
```

#### For Loop and else statement

we can add an else block that executes after the loop is completed. if we break from the loop at some time, it won't execute!

```py
for x in range(8):
    print(x)
    #break
else:
    print("loop is over")
```

### Range

the `range()` function create an iterable, we can pass the start and end elements, and the jump. by default we start at zero and increase by one. the starting element is inclusive and the ending element is exclusive.

```py
[x for x in range(5)] #0,1,2,3,4
[x for x in range(2,6)] #2,3,4,5
[x for x in range(2,6,2)] #2,4
```

</details>

## Section 10: Python Functions

<details>
<summary>
Functions
</summary>

> DRY - Don't Repeat Yourself

functions are code that can be reused. they can have parameters/arguments.

```py
type(len) # builtin_function_or_methods
def foo():
    pass
type(foo) #function
```

we create function with the `def` keyword, and then the function name, parentheses with the parameters, then colon and the function body in the next line. we can call/invoke/run the function by writing the function name with the parentheses and the given arguments.

parameter is the variable inside the function scope, while arguments are what the function is called with.

### Python Return Keyword Value

we can use function to return value (from some computation we did). we simply write the `return` keyword. if we don't specify a return value, then our function returns the _None_ value.

### Default Parameter Value

functions can have default parameter values. only the last argument can have default value. more accurately, we can not have a parameter without a default value after a default value.

we can use the parameter names to pass argument not in the positional order, but we cannot put any positional arguments after we started using named ones. this is called keyword Arguments.

```py
def foo(x,y,z=10,z2=100):
    print(x+y+z+z2)

foo(1,1)# 112
foo(1,1,2) #104
foo(1,1,2,5) #9
foo(1,2,z2=9)
```

### Functions Returning Other Functions

functions can return other function. we can save the function that we get back.

```py
def greeting(name):
    def say_hello():
        return f"hello {name}"
    return say_hello


jay = greeting("james")
print(jay())
dan = greeting("dan")
print(dan)
```

we can also assign functions to variable directly.

```py
len2 =len
len2([1,2,3]) #3
```

### Global and Local Variable Scopes

Variables declared inside a function have local scope. Variables declared outside have a global scope. w

```py
x =10 #global
def foo(x):
    print(x)
    x=7 #local x
    print(x)

foo(9)
print(x)
```

we can pull global variables into the local scope with the _global_ keyword. so we don't create a new variables. we refer to the global one.

```py
x1 = 10
x2 = 20

def bar(y):
    global x1
    x1 = y #using the global x1 and changing
    x2 = y #new x2 variable
    print(x1,x2)


print(x1,x2) #10,20
foo(7) #7,7
print(x1,x2) #7,20
```

### Nesting Functions

closure.

if we have nested functions, the inner functions can use the variable from the enclosing function. we can also refer to them with the `nonlocal` keyword. which acts similar to the `global` keyword.

```py
def foo(z,d=11):
    def bar():
        nonlocal z
        z+=d
        return z
    return bar

x = foo(5,1)
x() #6
x() #7
x() #8
```

### Function Pass Keyword

if we just want to have an empty block of code, like a scaffolding for now. we can write `pass` to appease the interpreter.

### Passing Functions as Arguments

we can pass function as arguments to other functions.

```py
def foo(b):
    return b +1

def bar(c):
    x=7
    return c(x)

print(bard(foo))
```

### VarArgs Parameter

passing an undeterminable number of parameters.

- one asterisk - tuple.
- two asterisks - dictionary.

python will try to capture the arguments based on their form. after getting the positional arguments, te rest of the arguments will become a tuple or key-value pairs.

```py
def total_number(a=7,*numbers, **phoneBook):
    print("My favorite number is " a)

    for num in numbers:
        print("num", num)
    for  name,phone_number in phoneBook.items():
        print(name, phone_number)

total_numbers(7,1,2,3,Jane=2222, John=4444, Angela=5555)
```

### Anonymous Functions

lambda,anonymous function, have only a single expression. we donn't need to have a return statement,

```py
a= lambda b: b+1
print(a(7))
```

we can have multiple arguments

```py
c = lambda x,y,z:x+y+z

print(c(6,7,8))
```

we can define lambda inside function, and return them from functions.

### Python DocStrings

document strings, display documentation in the code. we access the docstring with the \_\_doc\_\_. we define it withe using three quote marks.

```py
def add_numbers(x,y):
    ''' add ing three values

    param'''
    return x+y

add_numbers.__doc__
print(len.__doc__)
```

### Python Decorators

decorator allow us to add new functionality to existing objects (functions,method and classes). we use the `@` symbol and then the name of the decorator.

we can do this manually. like this:

```py
def my_decorator(function):
    def wrapper():
        foo = function()
        convert_uppercase=foo.upper()
        return convert_uppercase
    return wrapper

def bar():
    return "bar"


decorate = my_decorator(bar
print(decorate()))
```

but we can also use the built in decorator, with the `@` symbol

```py
@my_decorator
def foo():
    return "la

print(foo())
```

### Python Function Vs Python Method

a method is a function that is attached to some object. but most python libraries are objects, so all python functions are methods, except maybe some only built-in.

</details>

[main](../README.md)
