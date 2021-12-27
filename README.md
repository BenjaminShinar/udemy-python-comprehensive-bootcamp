<!--
// cSpell:ignore bootcamp
-->

# Python Comprehensive Bootcamp

Repository for Udemy course [Python Comprehensive BootCamp Beginner To Professional](https://www.udemy.com/course/python-comprehensive-bootcamp-beginner-to-professional/).

1. [Introduction](Lectures/section_01_04_intro.md#Section-01:-Introduction)
2. [Introduction To Command Line Interface](Lectures/section_01_04_intro.md#Section-02:-Introduction-To-Command-Line-Interface)
3. [Python Installation and Setup](Lectures/section_01_04_intro.md#Section-03:-Python-Installation-and-Setup)
4. [Interacting With Python](Lectures/section_01_04_intro.md#Section-04:-Interacting-With-Python)
5. [Python Operators](Lectures/section_05_08_intro.md#Python-Operators)
6. [Python Data Types](Lectures/section_05_08_intro.md#Python-Data-Types)
7. [Python String Methods and Formatting](Lectures/section_05_08_basics.md#Python-String-Methods-and-Formatting)
8. [Python Data Structures](Lectures/section_05_08_intro.md#Python-Data-Structures)
9. [Python Control Flow Statements](Lectures/section_09_10_control.md#Python-Control-Flow-Statements)
10. [Python Functions](Lectures/section_09_10_control.md#Python-Functions)
11. [Object Oriented Programming](Lectures/section_11_13_oop_modules_files.md#Object-Oriented-Programming)
12. [Modules and Packages](Lectures/section_11_13_oop_modules_files.md#Modules-and_Packages)
13. [Working with External Filles](Lectures/section_11_13_oop_modules_files.md#Working-With-External-Files)
14. [Working With Dates, Time, Calenders](Lectures/section_14_16_dates_images_csv.md#Working-with-Dates,-Times,-Calendars)
15. [Working With Images](Lectures/section_14_16_dates_images_csv.md#Section-15:-Working-with-Images)
16. [Working With CSV and PDF]
17. [Errors And Exceptions Handling]
18. [Creating Basic Python Projects]
19. [Building Desktop GUI Apps]
20. [Web Scraping]
21. [Web Development using Django]
22. [Building a Web Application with Django]
23. [Adding Web Project To Version Control]
24. [Implementing Dynamic Data Display]
25. [Deploying Web App]
26. [Building an API from Scratch]
27. [Create a CRUD App with Python and SQL Server]
28. [Python and Data Science]
29. [Python and Machine Learning]
30. [General Takeaways](README.md#Takeaways)

## Takeaways

<!-- <details> -->
<summary>
Stuff Worth Remembering.
</summary>

### General Knowledge

- [Python Documentation](https://docs.python.org/3/)
- [Python reserved keywords](https://www.w3schools.in/python-tutorial/keywords/)
- `\_\_doc\_\_` to get the doc string
- the **abc** module fo abstract base class
- the **datetime** module
- the **calender** module
- the **PIL** module for images

### Useful Command Line Commands

- [Windows commands](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands).
- [Linux bash commands](https://ss64.com/bash/).

| Command                | Linux    | Windows         | Flags                        | Notes       |
| ---------------------- | -------- | --------------- | ---------------------------- | ----------- |
| Display name           | `whoami` | `whoami`        |                              |
| Display current folder | `pwd`    | `cd`            |                              |
| change directory       | `cd`     | `cd`            |                              |
| List folder / files    | `ls`     | `dir`           |                              |
| Create new folder      | `mkdir`  | `mkdir`         |                              |
| Copy file              | `cp`     | `copy`          |                              |
| Move file              | `mv`     | `move`          |                              | also rename |
| Delete file / folder   | `rm`     | `del`, `rmdir`, | `-r` - linux, `\S` - windows |

- [Python CLI Commands](https://docs.python.org/3/using/cmdline.html)

| Command | Syntax                   | Flags | Notes          |
| ------- | ------------------------ | ----- | -------------- |
| Version | `python --version`, `-v` |       | python version |

Python Interactive Shell commands:

| Command                   | Syntax                           | Flags | Notes                       |
| ------------------------- | -------------------------------- | ----- | --------------------------- |
| interactive help          | `help`,`help()`,`help(<object>)` |       |                             |
| exit shell                | `exit()`,`quit()`                |       |                             |
| import file               | `import <file>`                  |       | run the file ,no extension  |
| list objects in workspace | `dir()`                          |       | show all variables declared |

### Python Operators

[Operators](https://www.w3schools.com/python/python_operators.asp)
| Operator | Symbol | Example | Category | Notes |
| -------------- | ------ | ------------ | ---------- | --------------------- |
| Addition | `+` | `1+2` = 3 | Arithmetic | string concatenations |
| Subtraction | `-` | `2-1` = 1 | Arithmetic | |
| Multiplication | `*` | `4*2` =8 | Arithmetic | repeat string |
| Division | `/` | `5/2`=2.5 | Arithmetic |
| Modules | `%` | `10 % 3` = 1 | Arithmetic | reminder
| Power(pow) | `**` | `5**3` = 125 | Arithmetic |
| Floor Division | `//` | `5//2` = 2 | Arithmetic | integer division |
| Assignment | `=` | `x = 5` | Assignment | base form |
| Plus Assignment | `+=` | `x += 3`| Assignment | same as `x = x + 3` |
| Minus Assignment | `-=` | `x -= 3`| Assignment | same as `x = x - 3` |
| Multiplication Assignment | `*=` | `x *= 3`| Assignment | same as `x = x * 3` |
| Division Assignment | `/=` | `x /= 3`| Assignment | same as `x = x / 3` |
| Modules Assignment | `%=` | `x %= 3`| Assignment | same as `x = x % 3` |
| Floor Division Assignment | `//=` | `x //= 3`| Assignment | same as `x = x // 3`|
| Power Assignment | `**=` | `x **= 3`| Assignment | same as `x = x ** 3` |
| Bitwise AND Assignment | `&=` | `x &= 3`| Assignment | same as `x = x & 3` |
| Bitwise OR Assignment | `\|=` | `x \|= 3`| Assignment | same as `x = x | 3` |
| Bitwise XOR Assignment | `^=` | `x ^= 3`| Assignment | same as `x = x ^ 3` |
| Shift Right Assignment | `>>=` | `x >>= 3`| Assignment | same as `x = x >> 3` |
| Shift Left Assignment | `<<=` | `x <<= 3`| Assignment | same as `x = x << 3` |
| Equality | `==` | `5==6` = false | Comparison | don't confuse with assignment!|
| Inequality | `!=` | `5!=6` = true | Comparison | &ne;|
| Greater than | `>` | `5>6` = false | Comparison | &gt;|
| Lesser than | `<` | `5<6` = true | Comparison | &lt;|
| Greater than or equals | `>=` | `5>=5` = true | Comparison | &ge;|
| Lesser than or equals | `<=` | `5<=4` = false | Comparison | &le;|
| Boolean and | `and` | `true and false` = false |Logical | `&&` in other languages
| Boolean or | `or` | `true or false` = true |Logical | `\|\|` in other languages
| Boolean not | `not` | `not(false)` = true |Logical | `!` in other languages
| Is | `is` | `x is x` = true | Identity| | | reference equality
| Is not | `is not` | `x is not y` = true | Identity| reference equality
| In | `is` | `5 in [1,2,3]` = false | Membership | member in group |
| Not in | `not in` | `5 not in [1,2,3]` = true | Membership | member not in group |
| Bitwise And | `&` | `5&4` = 4| Bitwise |
| Bitwise Or | `\|` | `8\|7` = 15| Bitwise |
| Bitwise Xor | `^` | `10^5` = 15| Bitwise |
| Bitwise Not | `~` | `~7` = -8| Bitwise | | | Because of two Complement
| Left Shift | `<<` | `4<<2` = 16 | Bitwise | each left shift is like doubling
| Right Shift | `>>` | `15>>2` = 7 | Bitwise |

### strftime()

the `strftime` method to format datetime objects

| syntax | description                                            | example                 |
| ------ | ------------------------------------------------------ | ----------------------- |
| `%a`   | weekday short                                          | "mon"                   |
| `%A`   | weekday full                                           | "monday"                |
| `%w`   | week day index - zero based                            | 0                       |
| `%d`   | day of month                                           | 17                      |
| `%b`   | month short name                                       | Dec                     |
| `%B`   | month full name                                        | December                |
| `%m`   | month number                                           | 12                      |
| `%y`   | year 2 digits                                          | 19                      |
| `%Y`   | year 4 digits                                          | 2019                    |
| `%H`   | hour, 24 hours format (00-23)                          | 19                      |
| `% `   | hour, 12 hours format (00-12)                          | 07                      |
| `%p`   | am/pm                                                  | AM                      |
| `%M`   | minutes(00-59)                                         | 25                      |
| `%S`   | seconds (00-59)                                        | 57                      |
| `%f`   | microsecond (000000-999999)                            | 656789                  |
| `%z`   | UTC offset                                             | +0100                   |
| `%Z`   | TimeZone                                               | CST                     |
| `%J`   | day of the year number (001-365)                       | 365                     |
| `%U`   | week number of the the year, start with sunday (00-53) | 52                      |
| `%W`   | week number of the the year, start with monday (00-53  | 52                      |
| `%c`   | local version / format of date and time                | Mon Apr 8 13:05:22 2019 |
| `%x`   | local version / format of date                         | 04/8/19                 |
| `%X`   | local version / format of time                         | 14:20:00                |
| `%%`   | writing the `%` character                              | %                       |

### Important functions

- `bin()` - return string representation of the binary value of some value.
- `dir()` - get package stuff

### Common Pitfalls

- not using `if __name__ == "__main__":`.
- having code outside of functions.
- confusing the amount of underscore.

</details>
