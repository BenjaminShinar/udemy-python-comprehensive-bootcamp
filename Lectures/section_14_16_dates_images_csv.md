<!--
// cSpell:ignore timedelta formatmonth alender itermonthdays monthcalendar venv infile cymk splitext pypdf writerow writerows
-->

[previous](section_11_13_oop_modules_files.md)\
[main](../README.md)

## Section 14: Working with Dates, Times, Calendars

<details>
<summary>
Datetime objects and calender objects
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

the **timedelta** is a span (difference) type. we use it to calculate operators on datetime objects.

```py
from datetime import datetime
from datetime import timedelta
now = datetime.now()

print (str(today+timedelta(days=365)))

delta= timedelta(days=365,hours=7,minutes=5)
print(delta)
```

we can use timedelta to find the date in the future or the past.

```py
from datetime import datetime,timedelta

today = datetime.now()
x =today - timedelta(weeks=2)
z= strftime("%A %B %d, %Y")# weekday name, month name, day in month, four digit year
print(z)
```

another example

```py
from datetime import datetime,timedelta,date, time
today = date.today()
xmas = date(today.year, month=12,day=25)
timeToXmas = xmas - today
print(type(timeToXmas)) #timeDelta
print ("just " ,timeToXmas.day ," days to xmas")
```

### Working with Calendars

python has the **calender** module, it can show us a basic representation of a calender in different forms. we pass the first day of the week.

```py
import calender

cal = calender.TextCalender(calender.SUNDAY)

str = cal.formatmonth(2019,4)
print(str)

htmlCal=calender.HTMLCalender(calender.SUNDAY)
print(htmlCal.formatmonth(2020,5))
```

we can also iterate over the calender. the output is a little weird. any day that is part of the week (from the starting weekday) but not part of the month is marked with zero. so if we start the count on sunday, but the month of april 2019 starts at monday and ends on tuesday, we will see a leading 0 (sunday,31 March), then 1 to 30 and then trailing zeros to finish the week (which is already the month of May).\

```py
import calender

cal = calender.TextCalender(calender.SUNDAY)

for day in cal.itermonthdays(2019,4):
    print(day, type(day))
```

we can use the locale to get the proper configuration. this doesn't require us to instantiate a calender of our own.

```py
import calender

for month in calender.month_name:
    print(month)

for day in calender.day_name:
    print(day)
```

now we want to know when is the first friday of each month. so we create a monthly calendar for each month, and then we take the first two weeks. if friday of the first week is already in the month (and not the previous month), then the day won't be zero. if the friday of the first week is still in the previous month, we need to look at the next week of the month.

```py
import calender

for month in range(1,13): #[1...12]
    cal = calendar.monthcalendar(2019,m)
    wk1 = cal[0]
    wk2 = cal[1]

    if wk1[calendar.FRIDAY] !=0:
        meetingDay= wk1[calendar.FRIDAY]
    else:
        meetingDay= wk2[calendar.FRIDAY]
    print("%10s %d" %(calendar.month_name[m], meeting)) #10s is formatting of width
```

</details>

## Section 15: Working with Images

<details>
<summary>
Images
</summary>

**PIL** python image library. **Pillow** is an updated version.

the video suggest using a virtual environment,

```sh
python -m venv <env name> #create a virtual environment
source venv/bin/activate #unix
Scripts/activate #windows
python -m pip install --upgrade pip
pip install pillow
```

### Loading Images

getting information about an image file and showing it (using the default image displaying program)

```py
from PIL import Image

img = Image.open("file.jpg")

print(img.format) #jpg,bmp,png...
print(img.mode) #cymk, rgc
print(img.size) #dimension in pixels

img.show()
```

### Manipulating Images

we will now do some manipulation on the image

```py
img = Image.open("file.jpg"). convert('L') #makes it grey scale

img.show()
img.save("file_gs.jpg")
img = Image.open("file.jpg")
newImg = img.resize((450,500))
print(newImg.size)
newImg.save("file.png") #save as different format
newImg.rotate(45).show() # rotate and show the image
```

### Creating thumbnails

a thumbnail is smaller version of an image, we can create them from the full size images.

```py
from PIL import Image
import glob, os

size = 128,128 #tuple

for infile in glob("puppies/*jgp"):
    file, ext = os.path.splitext(infile) #split extension
    img =image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(file +".thumbnail","JPEG")

```

anti aliasing means to minimize the distortion when representing a high resolution image at a lower resolution

</details>

## Section 16: Working with CSV and PDF

<details>
<summary>
CSV and PDF files
</summary>

### Working with CSV files

csv - comma separated values, like spreadsheets or other forms of data. we can use excel to save a sheet as a csv file.

### Reading a csv file

we use the iris dataset. we use the **csv** module and the `csv.reader()` function

```py
import csv

with open("iris.csv","rt") as file: # read as text, as opposed to read as binary
    csv_rows = csv.reader(file)
    for row in csv_rows:
        print(row)

```

### Writing to a csv file

writing data to csv files. the example is lacking and it's not clear why there are spaces between lines.

```py
import csv
headers = ["month","1958","1959","1960"]
data = [
    ["JAN",1,2,3],
    ["FEB",1,2,3],
    ["MAR",1,2,3],
    ["APR",1,2,3],
    ["MAY",1,2,3],
    ["JUN",1,2,3],
    ["JUL",1,2,3],
    ["AUG",1,2,3],
    ["SEP",1,2,3],
    ["OCT",1,2,3],
    ["NOV",1,2,3],
    ["DEC",1,2,3],
]

filename= "years.csv"
with open(filename, 'w') as work:
    writer = csv.writer(work)
    writer.writerow(headers)
    writer.writerows(data)
```

### Working with PDF in Python

pdf stands for **portable document format**, originally created by adobe. we will se **pypdf2** library, which we need to install. again, we use a virtual environment.

```sh
python -m venv some_name
some_name\scripts\activate
pip install pypdf2
```

### Extracting pdf document information in Python

we can extract the pdf metadata, such as

- Author
- Creator
- Producer
- Subject
- Title
- Number of pages

```py
from PyPDF2 import PdfFileReader

with open(pdf_path,"rb") as f: #read binary
    pdf = PdfFileReader(f)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()

txt = f"""
Information about {pdf_path}

Author: {information.author}
Creator: {information.creator}
Producer: {information.producer}
Subject: {information.subject}
Title: {information.title}
Number of pages:{number_of_pages}
"""
print(txt)
```

### How to rotate pages in PDF

rotating a pdf document, like having scanned documents upside down. we can use python to fix the orientation

```py
from PyPDF2 import PdfFileReader,PdfFileWriter

def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)

    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_wrier.addPage(page_1)
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)
    pdf_writer.addPage(pdf_reader.getPage(2))

    with open("rotated_pages.pdf",wb) as fh:
        pdf_writer.write(fh)


```

### How to merge pdf documents

we might want to combine pdf files together. we can do this by reading several pdf files and writing them together.

```py
from PyPDF2 import PdfFileReader,PdfFileWriter

def merge_pdf(paths,output):
    pdf_writer= PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output,"wb") as out:
        pdf_writer.write(out)
```

### How to split pdf document pages

just like "merging", se use the reader and writer objects to split a pdf fie into files containing one page each.

```py
from PyPDF2 import PdfFileReader,PdfFileWriter

def merge_pdf(path,name_of_split):
    pdf_reader = PdfFileReader(path)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer= PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))

        output = f"{name_of_split}_{page}.pdf"
        with open(output,"wb") as output_pdf:
            pdf_writer.write(output_pdf)

    with open(output,"wb") as out:
        pdf_writer.write(out)
```

### How to add watermark to a PDF document

we need the watermark as a pdf itself. we can then use the _mergePage()_ method to create a overlay layer of one pdf on top of the other.

```py
from PyPDF2 import PdfFileReader,PdfFileWriter

def create_watermark(input_pdf,watermark_pdf,output_path):
    pdf_reader = PdfFileReader(watermark_pdf)
    watermark_page = pdf_reader.getPage(0)
    pdf_reader = PdfFileReader(input_pdf)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer= PdfFileWriter(output_path)
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

```

### How to encrypt a PDF document

encrypting a pdf with a password.

```py
from PyPDF2 import PdfFileReader,PdfFileWriter

def add_encryption(input_pdf,output_pdf,password):
    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer= PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        pdf_writer.addPage(page)

    pdf_writer.encrypt(user_pwd=password,owner_pwd=None,use_128bit=True)
    with open(output_pdf,"wb") as fh:
        pdf_writer.write(fh)
```

</details>

[next](section_17_19_exceptions_projects_gui.md)
