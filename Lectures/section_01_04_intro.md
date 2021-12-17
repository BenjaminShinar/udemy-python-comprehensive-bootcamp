<!--
// cSpell:ignore
-->

[main](../README.md)

## Section 01: Introduction

<details>
<summary>
Python Introduction
</summary>

### High and Low Level Programming Languages

High level languages are understood by human, and require a compiler or interpreter to get a machine to read. python is such a language.

Low level languages are those which the computer can understand, they are harder to write, and express logic as cpu instructions. machine code and assembly are low level languages.

### Compilers and Interpreters

A compiler translates the **entire** source code into machine code before the execution, C and C++ are compiled languages.

an Interpreter translates the source code into the machine code **one line at a time**. this is done during the execution. python and Perl are interpreted languages

### What is Python

> - General purpose programming language.
> - High level programming language
> - Portable
> - Interpreted
> - Strongly typed (?)

python has many open source libraries available. with python, we can write web applications, android applications, games, use it for scientific purposes, system administration applications and console applications.

some examples are:

- youtube
- google
- dropbox
- reddit
- spotify
- instagram

</details>

## Section 02: Introduction To Command Line Interface

<details>
<summary>
Using the Command Line / Terminal
</summary>

The command line is a text based interface, also known as CLI, Console, Prompt, Terminal, cmd Or Shell.

### How to access command line interface

using the cli in various platforms:
windows:
_start menu -> all programs -> accessories -> Command Prompt_

mac OS:
_applications -> Utilities -> Terminal_

Linux (may be different for each linux release)
_applications -> Utilities -> Terminal_

### What you can do with command line

we can view files, directories (folders), do operations on files (copy, move, delete) and manipulate their contents

### Useful Commands

some nice commands (linux) we can use

- `whoami` - show computer and user
- `pwd` - print working directory
- `ls` - list files or folders in directory
- `mkdir` - create new folder
- `cp` - copy file
- `mv` - move/rename file
- `cd` - change directory

</details>

## Section 03: Python Installation and Setup

<details>
<summary>
Getting Python and Pycharm.
</summary>

### Installing Python on Windows

to check if python is installed,we run `python --version`, if we get a message. then we got python installed, otherwise, we need to install it from the official [python website](https://www.python.org).

### Installing Python3 on Macs

**SKIPPED!**

### Installing Pycharm on Windows, Changing Theme and Configurations

Pycharm is Python IDE (integrated development environment) by jetBrains, we can use it to create python applications, run, test, and debug it. we can get it from the [official website](https://www.jetbrains.com/pycharm/).

if we use Pycharm, we can change the theme by clicking

> - <kbd>File</kbd>
> - <kbd>Settings</kbd>
> - _Editor_
> - _Color Scheme_

Other configurations (still in the <kbd>File</kbd>-><kbd>settings</kbd>).

we create a project, and we can configure it specifically (use other settings than the global settings)

- Font type, Font size.
- _Project Interpreter_ - we need to add an interpreter, which is usually the python application, but we can use different versions if we want (like virtual env).

we start by testing our configuration. we create a python file "greeting.py".

```py
print("Hello World!")
```

we can run this file from the command line. or from the IDE.

```sh
python .\greeting.py
```

### Installing Pycharm on Macs, Configurations

**SKIPPED!**

### Installing Atom Text Editor

**SKIPPED!**

</details>

## Section 04: Interacting With Python

<details>
<summary>
Using the Python Shell (REPL -interactive console) and using python files.
</summary>

### Interacting using Python Shell

we access python shell by writing `python` on the terminal. this opens the python shell, which we recognize by the prompt changing to the **>>>** symbol. we can use the IDLE, which is an IDE that ships with python.

we can use the shell in an interactive way. we can create variables, change them, and so on

```py
7*7
print(7*7)
print("hello")
x = 5
print(x)
```

### Interacting using Python File

python files have the "py" extension. we can run them from the command line with `python file.py` or from the shell.

### Python Expressions

> - an expression is anything that has a value. they can be actual values or contain operators.

### Python Code Comments

two ways of marking comments, the single line comment with the hash symbol `#`. for multiline comment we use three quotation marks `'''` at the start and the end of the commented block.

```py
print(1)
#print(2) comment!
print(3)
'''
comment!
print(4) also comment!
'''
print(5)
```

we can write comment on the right side of the line to describe what the line does.

```py
print(5+5)#prints 10
```

### Python Code Indentation

python really cares about indentations. this controls code blocks, loops, and flow control.
there are no curly braces ("{}" or semi colons";"), we can use tabs and spaces, but the best practice is to stick with one of them (spaces), and indent each block by 4 spaces.

```py
x = 5
if (x>2):
    print("indent")
    print("still inside bloc")

    print("after empty line")
print("out of block")
```

### Python Variables

a variable is a holding container to store a value that can be referenced as required.
we can change the variable. they have a memory address. they have names, and they can store different data types.

naming rules:

- case sensitive.
- letters, number, $ and underscore.
- can't start with a number.
- can't be one of the [reserved keywords](https://www.w3schools.in/python-tutorial/keywords/).

we use either snake_case or camelCase to name or variables.

### Creating Variables

we can create variables in different ways. the most basic is direct assignment/creation `name = value`

some containers have a special symbol.

- list `x=[]`,`x=list()`
- dictionary `y={}`,`y=dict()`
- tuple `z=()`,`z=tuple()`

### Getting Input from Users

we get user input with the `input` function. we always get a string back, if we want a number, we need some casting.

```py
input1 = input("prompt what to do!\n")
print(type(input1), input1)
num =int(input1)
print(type(num), num)
```

</details>

[main](../README.md)
