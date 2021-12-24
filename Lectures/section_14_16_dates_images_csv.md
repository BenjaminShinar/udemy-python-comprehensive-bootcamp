<!--
// cSpell:ignore
-->

[main](../README.md)

## Section 12: Working with Dates, Times, Calendars

<!-- <details> -->
<summary>
Datetime objects
</summary>

### Working with Date and Time

the **datetime** module, which we need to import. it has a **date** class, a **time** class, and a **datetime** class.

```py
from datetime import date
from datetime import time
from datetime import datetime

today = date.today() #date
print("today is",today,type(today))
print("date components:",today.day,today.month, today.year)
print("today weekday:",weekday()) #zero is monday

today2= datetime.now() #datetime
print("today2 is",today2,type(today2))
timeNow =datetime.time(today2)
print("datetime time:",timeNow, type(timeNow))
```

### Formatting Date and Time Objects

the `strftime` method to format datetime objects

| syntax | description                                    | example                 |
| ------ | ---------------------------------------------- | ----------------------- |
| `%a`   | weekday short                                  | "mon"                   |
| `%A`   | weekday full                                   | "monday"                |
| `%w`   | week day index - zero based                    | 0                       |
| `%d`   | day of month                                   | 17                      |
| `%b`   | month short name                               | Dec                     |
| `%B`   | month full name                                | December                |
| `%m`   | month number                                   | 12                      |
| `%y`   | year 2 digits                                  | 19                      |
| `%Y`   | year 4 digits                                  | 2019                    |
| `%H`   | hour, 24 hours format                          | 19                      |
| `% `   | hour, 12 hours format                          | 07                      |
| `%p`   | am/pm                                          | AM                      |
| `%M`   | minutes(00-59)                                 | 25                      |
| `%S`   | seconds (00-59)                                | 57                      |
| `%f`   | microsecond (000000-999999)                    | 656789                  |
| `%z`   | UTC offset                                     | +0100                   |
| `%Z`   | TimeZone                                       | CST                     |
| `%J`   | day of the year number (001-365)               | 365                     |
| `%U`   | week number of the the year, start with sunday | 52                      |
| `%W`   | week number of the the year, start with monday | 52                      |
| `%c`   | local version / format of date and time        | Mon Apr 8 13:05:22 2019 |
| `%x`   | local version / format of date                 | 04/8/19                 |
| `%X`   | local version / format of time                 | 14:20:00                |
| `%%`   | writing the `%` character                      | %                       |

```py
from datetime import datetime
today = datetime.now()
print(today)
print(today.strftime("year is %Y"))
print(today.strftime("today is %a, %d %B,%y))
```

the locale format is what the OS uses by default for our region and settings, we use the `%c`,`%x` and `%X` to use it.

### Datetime Calculations

### Working with Calendars

</details>

[main](../README.md)
