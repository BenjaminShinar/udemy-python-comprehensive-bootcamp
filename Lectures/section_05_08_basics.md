<!--
// cSpell:ignore
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

<!-- <details> -->
<summary>
//TODO: add Summary
</summary>

### Python String Methods : Part 1

### Python String Methods : Part 2

### Python String Formatting : Part 1

### Python String Formatting : Part 2

</details>

## Section 08: Python Data Structures

<!-- <details> -->
<summary>
//TODO: add Summary
</summary>

### What are data structures

### Python List

### Creating a Python List

### Accessing elements in a list

### Python List Methods: Part 1

### Python List Methods: Part 2

### Python Tuple : Part 1

### Python Tuple : Part 2

### Python SET

### Python SET Methods

### Python Dictionary

### Python Dictionary Methods

### Creating a directory for Python Files

</details>

[main](../README.md)
