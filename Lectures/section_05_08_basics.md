<!--
// cSpell:ignore maxsplit fromkeys
-->

[main](../README.md)

## Section 05: Python Operators

<details>
<summary>
Operators, types of operators, precedence and affinity(associativity).
</summary>

Operators are functionality that do something to values. the data the operators interacts with are _operands_.

Operator types:

- Arithmetic
- Assignment
- Comparison
- Logical
- Identity
- Membership
- Bitwise

### Python Arithmetic Operators

basic math operators. addition, subtraction, multiplication, division. but also modules (get reminder), power (exponents), and floor division (integer division, nearest whole number).

### Python Assignment Operators

operators used to assign values. they all build on the basic `=` operator. we have one option for each of the math operators, and five more for the bitwise operators of `AND`,`OR`,`XOR`,`shift left` and `shift right`.

they are shorthands to writing the complete form.

```py
x = 5
#x= x+5 option 1
x+=5 # option2

y = 0b100 # binary 4
# y= y<<1 option1
y<<=1 #option 2
```

### Python Comparison Operators

Operators that are used to compare values. equality, inequality, and ordering.

### Python Logical Operators

combine conditional statements, they work on boolean values (true or false). we have _boolean and_, _boolean or_, and _boolean not_.

we can create a truth table if we want.

### Python Identity Operators

operator to determine if to variables refer to the same objects. like checking the addresses of the inner values. different for literals.

```py
x = 4
y = 4
z = 5

print(x is y) # true
print(x is z) # false

l1 = [1]
l2 = [1]
print(l1 == l2) # true, equality
print(l1 is l2) # false, different objects
```

### Python Membership Operators

determine if a value is present in a container (list, tuple, dictionary, set).

### Binary Numbers

binary numbers in python. only used for integer numbers. not for floating point numbers. the `bin()` function returns a string of the binary representation. we can use the _0b_ prefix to make binary numbers.

```py
x =0b111
print(7==x)
print(x,bin(x)) #7,0b111
print(bin(-10)) #-0b1010
#print(bin(0.5)) #error
```

### Python Bitwise Operators

bitwise operations: `and`,`or`,`xor`. shifting to the left and the right. also the bitwise `not`, which uses two-complement arithmetics. so we can get negative values.

### Python Operator Precedence

the order of evaluation of operators. like the order of math sub expressions. the expressions with operators high on the precedence list are evaluated first. for operators with the same precedence value, left to right ordering is used.

- Parentheses
- Exponents (power)
- Multiplication, division, floor division, modulus
- Addition, Subtraction
- Bitwise Shift left, shift right
- Bitwise AND
- Bitwise XOR
- Bitwise OR
- Comparisons, identity, membership
- Logical NOT
- Logical AND
- Logical OR
- Assignments

most operators have left to right associativity.

</details>

## Section 06: Python Data Types

<details>
<summary>
Numbers, Strings and Boolean Values
</summary>

### Python Number Data Type

Integers and Floating point numbers. can be positive or negative. the division operator and the floor division will always return a floating point number, even if used with two integers.

```py
print(type(1)) #integer
print(type(1.0)) #float
```

### Python String Data Type

the text and characters type. there is not data type for a single character. we can use single quotes or double quotes, but we must match. we can have an empty string. we can use the backslash to escape charters.

characters have an index in the string. we can find the index of a sub string with the `.index()` method.

```py
print(type('a'))
print("double quotes?\" no problem!")
print("hello world".index('e')) #1
print("hello world".index('ld')) #9
```

### Python Boolean Data Type

boolean, true and false values.

```py
print((1==2),type (1==2)) # False
print((2<=2),type (2<=2)) # True
```

### Casting Data Types

Casting is converting values from one type to another. we can usually always cast to string, and some string values we can cast to numbers.

```py
print(int(5.0)) #5
print(int(6.99)) #6
print(float(-4)) #-4.0
print(str(7)) #"7"

print(int("-1")) #-1
print(int("1.0")) #error!
print(float("-1")) #-1.0
print(float('1.6')) #1.6
```

</details>

## Section 07: Python String Methods and Formatting

<details>
<summary>
Basic string methods
</summary>

strings are text.

### Python String Methods

[String methods](https://www.w3schools.com/python/python_strings_methods.asp)

- `len(<str>)` - length of string. counts white space.
- `.index(<sub str>)` - index of substring. error if doesn't exist.
  - we can pass the start and end positions as optional
- `find(<sub str>)` - index of substring, -1 if doesn't exist.
  - we can pass the start and end positions as optional
- `.capitalize()` - capitalize the first character, the rest are lower.
- `.lower()` - return lower case
- `.upper()` - return upper case
- `.islower()` - are all characters lower case?
- `.isupper()` - are all characters upper case?
- `.count(<sub str>)` - count appearances of sub string
  - we can pass the start and end positions as optional
- `.split(<separator>,<maxsplit)` - split text into list of substring,
  - default separator is white space. we can use _"\n"_ for new line.
  - we can decide on how many splits to do by passing _maxsplit_ integer, default is _-1_ for all occurrences.
- `replace(<sub str>,<replacement>)` - replace sub string.
  - we cana add _count_ parameter to limit how many replacement to do.

we already know we can use indexing to get specific characters in a string, and that the `+` operator does concatenation and the `*` operator repeats the string.

### Python String Formatting

the **f string**. We can have computations inside the string. all the computation happens during runtime.the syntax is `f"text {value} more text"`. when two strings are right next to each other, they are automatically concatenated.

```py
name = "blue"
age = 4
print(f"Hello, {name}. You are {age} years old.")
x=5
y=6
print(f"{x} + {y} is {x+y}")
```

when we want to use quotes inside our string (like a dictionary key) we need to be careful.

</details>

## Section 08: Python Data Structures

<details>
<summary>
Basic data types
</summary>

the four basic data structure in python:

- list
- Tuple
- Set
- Dictionary

### Python List

a collection data, can be of mixed types. items are ordered by the index, they can be changed and we can mutate the list. we use the square brackets `[]` to create a list, we can then access items by position. we can add and remove elements from a list.

#### Creating a Python List

we create a list with either a square brackets or with a list constructor. we can iterate over a list with a for loop. we can also print a list directly.

```py
ls1 = ["1",3,[]]
ls2 = list(("a",3,[])) #create a list from a tuple
ls3 =list("abc") #["a","b","c]

for x in ls2:
    print(x)
```

#### Accessing elements in a list

we can access the list elements with the index in the square brackets, remember that we use zero-based indexing. we can use negative index to start from the end of the list. we can also use slicing to access a range of elements inside the list. we can modify the list elements.

```py
l=[1,2,3,4]
print(l[0])
print(l[-1]) #last element
print(l[1:-1])
l[0]=7
print(l)
```

#### Python List Methods

[List methods](https://www.w3schools.com/python/python_lists_methods.asp)

- `len(<list>)` - length of list (number of items)
- `del(<list>)` - delete list
- `append(<element>)` - add item to end of the list.
- `insert(<index>,<element>)` add elements at a specific index. all the other elements are moved to the next position
- `.extend(<other list>)` - mutate the list by adding the contents of another list to it.
- `.remove(<element>)` - remove item by value.
- `.pop(<index>)` - remove item by index. return the value.
  - if we don't specify an index, it removes the last element.
- `.clear()` - mutate the list by removing all items.
- `.sort(<key>, reverse=bool)`- mutate the list by sorting it.
  - we can pass a function as the key parameter to control the sorting.
  - we can sort in reverse by passing a boolean value True to sort in reverse.
- `.count(<element>)` - count occurrences of element.
- `index(<element>)` - index of element in list

```py
def foo(n):
  return abs(n - 50)

ls = [100, 50, 65, 82, 23]
ls.sort(key = foo)
print(ls)
```

### Python Tuple

A tuple is an immutable list. we can't add or remove elements from it. we can create tuples with the round parentheses `()` or the tuple constructor. we can loop over the tuple with a for loop.

```py
x= ()
print(type(x))
y= tuple([1,2,3])
print(type(y))
```

unlike a list, we can't modify the tuple once it's created. however, this is only for the top most elements. if we have nested elements in the deeper portions of the tuple, we can modify them

```py
tpl = tuple([1,[]])
#tpl[0]=2 #error
tpl[1].append(1) #this is legal
#tpl[1]=[] #also an error
```

### Python SET

A collection (not ordered, not indexed) of unique values. you cannot modify the values inside it. we create a set with curly braces "{}" or the set constructor. a set can contain elements from different types.

we can loop over the set elements.

```py
fruits = {"grapes","apples","berries"}
for fruit in fruits:
    print(fruit)
```

[Set Methods](https://www.w3schools.com/python/python_sets_methods.asp)

- `.add(<element>)` - add a single element.
- `.update(<elements>)` - add multiple elements.
- `.remove(<element>)` - remove element, error if doesn't exist.
- `.discard(<element>)` - remove element, no error if doesn't exits.
- `.clear()` - remove all elements.
- `.union(<other set>)` - create a new set with all the elements from two sets.
- `.intersection(<other set>)` - create a new set with the shared elements from two sets.
- `.intersection_update(<other set>)` - keep only the elements shared in the two sets.
- `.symmetric_difference(<other_set>)` - create a new set with only the elements that aren't shared.
- `.symmetric_difference_update(<other_set>)` - keep only the elements that aren't shared in both sets.

### Python Dictionary

A dictionary is a key-value pair collection. the key must be unique, and it cannot be modified. the values are mutable. we create dictionaries with the curly braces with key value pairs, or use the dictionary constructor. in this cae we don't need quotes around the key name.

```py
car = {
    "brand": "range rover",
    "speed": 20
}
car2 =dict(key1="value", key2=11)
```

[Dictionary methods](https://www.w3schools.com/python/python_dictionaries_methods.asp)

- `.items()` - get an iterable for all items.
- `.keys()` - get all keys.
- `.values()` - get all values.
- `.get(<key>,<other value>)` - get element from key, will return `None` if doesn't exists.
  - we can specify the return value if it doesn't exist.
- `.update()` - add a key-value pair.
- `.clear()` - remove all elements
- `fromkeys(<keys>,<value>)` - create a new dictionary from the keys with those values (or `None` if no value was given).
- `.copy()` - return a copy of the dictionary.

</details>

[main](../README.md)
